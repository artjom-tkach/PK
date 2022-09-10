from telegram.views.keyboards.start import StartKeyboard
from telegram.views.view import View


class StartView(View):

    def __init__(self, bot):
        self.bot = bot

        super().__init__(bot)

    async def start(self, user):
        if await self.is_valid(user):
            texts = {
                'en': 'Welcome!',
                'ru': 'Добро пожаловать!'
            }
            await self.bot.send_message(
                user.user_id, self.get_text(texts, user.language_code),
                reply_markup=StartKeyboard.get_main_menu(user.language_code)
            )
