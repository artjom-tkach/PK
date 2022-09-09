from telegram.views.keyboards.buy_product import BuyProductKeyboard
from telegram.views.view import View


class BuyProductView(View):

    def __init__(self, bot):
        self.bot = bot

        super().__init__(bot)

    async def buy_product_handler(self, user, category_callback):
        if await self.is_valid(user):
            texts = {
                'en': 'Choose category of product.',
                'ru': 'Выберите категорию товара.'
            }

            await self.bot.send_message(
                user.user_id, self.get_text(texts, user.language_code),
                reply_markup=BuyProductKeyboard.get_categories(category_callback, language=user.language_code)
            )
