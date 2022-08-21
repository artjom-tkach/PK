from aiogram import types

from telegram.models.user import UserModel
from telegram.views.start import StartView


class StartController:

    def __init__(self, bot, dispatcher, database):
        self.__bot = bot
        self.__dispatcher = dispatcher
        self.__database = database

        self.__handlers()

        super().__init__(self.__bot, self.__dispatcher, self.__database)

    def __handlers(self):
        @self.__dispatcher.message_handler(commands=['start'])
        async def start_handler(message: types.Message):
            """
            This handler will be called when user sends '/start' command
            """
            user = await UserModel(self.__database).create(message)

            view = StartView(self.__bot, user, message)

            await view.start_handler()
