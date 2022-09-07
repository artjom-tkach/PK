from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from telegram.views.view import View


class Keyboard:
    buttons = {
        'buy_product': {
            'en': 'Buy product ™',
            'ru': 'Купить товар ™'
        }
    }

    def get_main_menu(self, language='en'):
        keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(KeyboardButton(View.get_text(self.buttons['buy_product'], language)))
        return keyboard
