from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.models.category import CategoryModel
from telegram.views.keyboards.keyboard import Keyboard
from telegram.views.view import View


class BuyProductKeyboard(Keyboard):
    @staticmethod
    async def get_parents_categories(categories, category_callback, language='en'):
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons = []

        if not categories:
            # If not available categories
            text = {
                'en': 'No categories available.',
                'ru': 'Нет доступных категорий.'
            }
            buttons.append(InlineKeyboardButton(View.get_text(text, language), callback_data='pass'))

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

    @staticmethod
    async def get_children_categories(categories, category_callback, language='en'):
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons = []

        if not categories:
            # If not available categories
            text = {
                'en': 'No subcategories available.',
                'ru': 'Нет доступных подкатегорий.'
            }
            buttons.append(InlineKeyboardButton(View.get_text(text, language), callback_data='pass'))

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
