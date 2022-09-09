from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.models.category import CategoryModel
from telegram.views.keyboards.keyboard import Keyboard
from telegram.views.view import View


class BuyProductKeyboard(Keyboard):
    @staticmethod
    def get_parents_categories(category_callback, language='en'):
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons = []

        categories = CategoryModel.get_all(is_active=True)

        for category in categories:
            # Language titles
            titles = {
                'en': category.title_en,
                'ru': category.title_ru
            }

            # Get title for language
            category.title = View.get_text(titles, language)

            # Create button in keyboard with choose callback
            buttons.append(InlineKeyboardButton(
                category.title,
                callback_data=category_callback.new(action='choose', category_id=category.id))
            )

        return keyboard.add(*buttons)
