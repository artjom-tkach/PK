from telegram.views.user import UserView


class StartView:

    def __init__(self, bot, user, message):
        self.__bot = bot
        self.__user = user
        self.__message = message

    async def start_handler(self):
        user_view = UserView(self.__bot, self.__user, self.__message)

        if await user_view.is_valid():
            send_text = {
                'en': 'Welcome!',
                'ru': 'Добро пожаловать!',
                'uk': 'Ласкаво просимо!'
            }

            return await self.__bot.send_message(
                self.__message.from_user.id,
                send_text.get(self.__user['language_code'], 'en')
            )
