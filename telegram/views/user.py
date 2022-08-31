class UserView:

    def __init__(self, bot, user, message):
        self.__bot = bot
        self.__user = user
        self.__message = message

    async def is_empty(self):
        return not self.__user

    async def is_blocked(self):
        return self.__user['is_blocked'] == 1

    async def is_valid(self):
        if await self.is_empty():
            send_text = {
                'en': 'The feature is temporarily unavailable. Please report this to the administrator.',
                'ru': 'Функция временно не доступна. Пожалуйста, сообщите об этом администратору.',
                'uk': 'Функція тимчасово недоступна. Будь ласка, повідомте про це адміністратора.'
            }
            await self.__bot.send_message(
                self.__message.from_user.id,
                send_text.get(
                    self.__message.from_user.language_code, send_text['en']
                )
            )

        elif await self.is_blocked():
            send_text = {
                'en': 'You have been blocked.',
                'ru': 'Вы были заблокированы.',
                'uk': 'Ви були заблоковані.'
            }
            await self.__bot.send_message(
                self.__message.from_user.id,
                send_text.get(
                    self.__user['language_code'], send_text['en']
                )
            )

        else:
            return True
