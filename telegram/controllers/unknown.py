from aiogram import types

from telegram.models.user import UserModel
from telegram.views.unknown import UnknownView


class UnknownController:

    def __init__(self, bot, dispatcher, database):
        self.__bot = bot
        self.__dispatcher = dispatcher
        self.__database = database

        self.__handlers()

    def __handlers(self):
        @self.__dispatcher.message_handler()
        async def unknown_handler(message: types.Message):
            """
            This handler will be called unknown command
            """
            user = await UserModel(self.__database).get(message.from_user.id)

            view = UnknownView(self.__bot, user, message)

            await view.unknown_handler()
