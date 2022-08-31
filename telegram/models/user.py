from telegram.databases.sqlite import User


class UserModel:

    @staticmethod
    async def create(message):
        return User.create(username=message.from_user.first_name)
