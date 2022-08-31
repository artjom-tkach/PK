from aiogram import types

from telegram.models.user import UserModel
from telegram.views.start import StartView


class StartController:

    def __init__(self, bot, dispatcher, database):
        self.bot = bot
        self.dispatcher = dispatcher
        self.database = database

        # Set handlers
        self.set_handlers()

    def set_handlers(self):
        @self.dispatcher.message_handler(commands=['start'])
        async def start_handler(message: types.Message):
            """
            This handler will be called when user sends '/start' command
            """
            user = await UserModel(self.database).create(message)

            view = StartView(self.bot, user, message)

            await view.start_handler()
