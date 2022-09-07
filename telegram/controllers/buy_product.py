from aiogram import types

from telegram.models.user import UserModel
from telegram.views.buy_product import BuyProductView
from telegram.views.keyboards.buy_product import BuyProductKeyboard


class BuyProductController:

    def __init__(self, bot, dispatcher):
        self.bot = bot
        self.dispatcher = dispatcher

        # Set view
        self.view = BuyProductView(bot)

        # Set handlers
        self.set_handlers()

    def set_handlers(self):
        @self.dispatcher.message_handler(lambda message: message.text in BuyProductKeyboard.buttons['buy_product'].values(),
                                         state='*')
        async def buy_product_handler(message: types.Message):
            user = await UserModel.get(message)
            await self.view.buy_product_handler(user)
