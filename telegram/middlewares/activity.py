from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from telegram.models.user import UserModel


class ActivityMiddleware(BaseMiddleware):

    def __init__(self, database):
        self.__database = database

        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        """
        This handler is called when dispatcher receives a message
        :param message:
        :param data:
        """
        await UserModel(self.__database).update_activity(message)
