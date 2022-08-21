import datetime
import pytz


class UserModel:
    __table_name = 'Users'
    __timezone = 'Europe/Berlin'

    def __init__(self, sqlite3):
        self.__sqlite3 = sqlite3

    async def get(self, user_id):
        return self.__sqlite3.select(table_name=self.__table_name, select_fields='*', where_fields=[{
            'field': 'user_id',
            'value': user_id,
            'operator': '='
        }], limit_field=1)

    async def create(self, message):
        user = await self.get(message.from_user.id)

        if not user:
            user = self.__sqlite3.insert(table_name=self.__table_name, insert_fields={
                'user_id': message.from_user.id,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
                'username': message.from_user.username,
                'language_code': message.from_user.language_code,
                'created_at': datetime.datetime.now(pytz.timezone(self.__timezone)).strftime('%d.%m.%Y %H:%M:%S')
            }, get_select=True)

        return user

    async def update_activity(self, message):
        return self.__sqlite3.update(
            table_name=self.__table_name,
            update_fields={
                'acted_at': datetime.datetime.now(pytz.timezone(self.__timezone)).strftime('%d.%m.%Y %H:%M:%S'),
                'username': message.from_user.username
            },
            where_fields=[{
                'field': 'user_id',
                'value': message.from_user.id,
                'operator': '='
            }]
        )
