from aiogram import types

from telegram.models.user import UserModel
from telegram.views.unknown import UnknownView


class UnknownController:

    def __init__(self, bot, dispatcher):
        self.bot = bot
        self.dispatcher = dispatcher

        # Set view
        self.view = UnknownView(bot)

        # Set handlers
        self.set_handlers()

    def set_handlers(self):
        @self.dispatcher.message_handler()
        async def unknown_handler(message: types.Message):
            """
            This handler will be called unknown command
            """
            user = await UserModel.get(message)

            await self.view.unknown_handler(user)
