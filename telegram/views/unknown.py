from telegram.views.view import View


class UnknownView(View):

    def __init__(self, bot):
        self.bot = bot

        super().__init__(bot)

    async def unknown(self, user):
        if await self.is_valid(user):
            texts = {
                'en': 'I don\'t know this command.',
                'ru': 'Я не знаю такой команды.'
            }
            await self.bot.send_message(user.user_id, self.get_text(texts, user.language_code))
