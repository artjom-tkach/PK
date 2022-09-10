import datetime

from telegram.databases.sqlite import User


class UserModel:

    @staticmethod
    async def create(message):
        return User.create(
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            language_code=message.from_user.language_code
        )

    @staticmethod
    async def get(user_id):
        return User.get(user_id=user_id)

    @staticmethod
    async def get_or_create(message):
        try:
            return User.get(user_id=message.from_user.id)
        except User.DoesNotExist:
            return User.create(
                user_id=message.from_user.id,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username,
                language_code=message.from_user.language_code
            )

    @staticmethod
    async def update_acted_at(message):
        query = User.update({User.acted_at: datetime.datetime.now()}).where(User.user_id == message.from_user.id)
        query.execute()

    @staticmethod
    async def update_username(message):
        query = User.update({User.username: message.from_user.username}).where(User.user_id == message.from_user.id)
        query.execute()

    @staticmethod
    async def update_username_and_acted_at(message):
        query = User.update({User.username: message.from_user.username, User.acted_at: datetime.datetime.now()}).where(
            User.user_id == message.from_user.id)
        query.execute()
