from telegram.views.keyboards.buy_product import BuyProductKeyboard
from telegram.views.view import View


class BuyProductView(View):

    def __init__(self, bot):
        self.bot = bot

        super().__init__(bot)

    async def get_parents_categories(self, user, categories, category_callback):
        if await self.is_valid(user):
            texts = {
                'en': 'Choose category of product.',
                'ru': 'Выберите категорию товара.'
            }

            await self.bot.send_message(
                user.user_id, self.get_text(texts, user.language_code),
                reply_markup=await BuyProductKeyboard.get_parents_categories(
                    categories,
                    category_callback,
                    language=user.language_code
                )
            )

    async def get_children_categories(self, query, user, categories, category_callback):
        if await self.is_valid(user):
            texts = {
                'en': f'Choose subcategory of <b>{categories[0].parent.title_en.capitalize()}.</b>',
                'ru': f'Выберите подкатегорию <b>{categories[0].parent.title_ru.capitalize()}.</b>'
            }

            await query.message.edit_text(
                self.get_text(texts, user.language_code),
                reply_markup=await BuyProductKeyboard.get_children_categories(categories, category_callback,
                                                                              language=user.language_code)
            )
