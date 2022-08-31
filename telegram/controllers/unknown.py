from aiogram import types

from telegram.models.user import UserModel
from telegram.views.unknown import UnknownView


class UnknownController:

    def __init__(self, bot, dispatcher, database):
        self.bot = bot
        self.dispatcher = dispatcher
        self.database = database

        self.set_handlers()

    def set_handlers(self):
        @self.dispatcher.message_handler()
        async def unknown_handler(message: types.Message):
            """
            This handler will be called unknown command
            """
            user = await UserModel(self.database).get(message.from_user.id)

            view = UnknownView(self.bot, user, message)

            await view.unknown_handler()
