from aiogram import types

from telegram.models.user import UserModel
from telegram.views.start import StartView


class StartController:

    def __init__(self, bot, dispatcher):
        self.bot = bot
        self.dispatcher = dispatcher

        # Set view
        self.view = StartView(bot)

        # Set handlers
        self.set_handlers()

    def set_handlers(self):
        @self.dispatcher.message_handler(commands=['start'])
        async def start_handler(message: types.Message):
            """
            This handler will be called when user sends '/start' command
            """
            user = await UserModel.get_or_create(message)

            await self.view.start_handler(user)
