class View:

    def __init__(self, bot):
        self.bot = bot

    async def is_valid(self, user):
        if bool(user.is_blocked):
            texts = {
                'en': 'You are blocked.',
                'ru': 'Вы заблокированы.'
            }
            await self.bot.send_message(user.user_id, await self.get_text(texts, user.language_code))

            return False

        return True

    async def get_text(self, texts, language='en'):
        return texts.get(language, texts['en'])
