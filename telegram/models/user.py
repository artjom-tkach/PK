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
    async def get(message):
        return User.get(user_id=message.from_user.id)

    async def get_or_create(self, message):
        user = User.get_or_none(user_id=message.from_user.id)

        if not user:
            return await self.create(message)

        return user

    @staticmethod
    async def update_activity(message):
        query = User.update({User.acted_at: datetime.datetime.now()}).where(User.user_id == message.from_user.id)
        query.execute()
