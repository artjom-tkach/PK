from telegram.views.user import UserView


class UnknownView:

    def __init__(self, bot, user, message):
        self.__bot = bot
        self.__user = user
        self.__message = message

        self.__user_view = UserView(self.__bot, self.__user, self.__message)

    async def unknown_handler(self):
        if await self.__user_view.is_valid():
            return await self.__bot.send_message(self.__message.from_user.id, 'What?')
