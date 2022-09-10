from aiogram import types
from aiogram.utils.callback_data import CallbackData

from telegram.models.category import CategoryModel
from telegram.models.user import UserModel
from telegram.views.buy_product import BuyProductView
from telegram.views.keyboards.buy_product import BuyProductKeyboard


class BuyProductController:
    # Callback
    category_callback = CallbackData('category', 'action', 'category_id')

    def __init__(self, bot, dispatcher):
        self.bot = bot
        self.dispatcher = dispatcher

        # Set view
        self.view = BuyProductView(bot)

        # Set handlers
        self.set_handlers()

    def set_handlers(self):
        @self.dispatcher.message_handler(
            lambda message: message.text in BuyProductKeyboard.buttons['buy_product'].values(),
            state='*')
        async def get_parents_categories(message: types.Message):
            user = await UserModel.get(message.from_user.id)
            categories = await CategoryModel.get_parents(is_active=True)

            await self.view.get_parents_categories(user, categories, self.category_callback)

        @self.dispatcher.callback_query_handler(self.category_callback.filter(action='choose'))
        async def get_children_categories_or_products(query: types.CallbackQuery, callback_data: dict):
            user = await UserModel.get(query['from']['id'])
            categories = await CategoryModel.get_children(callback_data['category_id'], is_active=True)

            if categories:
                return await self.view.get_children_categories(query, user, categories, self.category_callback)

            # await self.view.choose_children_category_handler(query, user, category_id, category_title, self.category_callback)
