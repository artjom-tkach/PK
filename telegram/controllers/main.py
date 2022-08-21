import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .start import StartController
from .unknown import UnknownController
from databases.sqlite3.sqlite3 import Sqlite3
from ..middlewares.throttling import ThrottlingMiddleware
from ..middlewares.activity import ActivityMiddleware


class MainController(StartController, UnknownController):

    def __init__(self, token):
        logging.basicConfig(level=logging.INFO)

        self.__bot = Bot(token=token)
        self.__dispatcher = Dispatcher(self.__bot, storage=MemoryStorage())
        self.__database = Sqlite3()

        super().__init__(self.__bot, self.__dispatcher, self.__database)

        # Middlewares
        self.__dispatcher.middleware.setup(ThrottlingMiddleware(limit=5))
        self.__dispatcher.middleware.setup(ActivityMiddleware(self.__database))

        executor.start_polling(self.__dispatcher, skip_updates=True)
