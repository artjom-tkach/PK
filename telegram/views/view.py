import bleach


class View:

    def __init__(self, bot):
        self.bot = bot

    async def is_valid(self, user):
        if bool(user.is_blocked):
            texts = {
                'en': 'You are blocked.',
                'ru': 'Вы заблокированы.'
            }
            await self.bot.send_message(user.user_id, self.get_text(texts, user.language_code))

            return False

        return True

    @staticmethod
    def get_with_tags(text, tags=None):
        return bleach.clean(text, tags=tags)

    @staticmethod
    def get_text(texts, language='en'):
        return View.get_with_tags(texts.get(language, texts['en']), ['b', 'i', 'a', 'code', 'pre'])
