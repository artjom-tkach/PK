from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Controllers
from telegram.controllers.start import StartController
from telegram.controllers.buy_product import BuyProductController
from telegram.controllers.unknown import UnknownController

# Middlewares
from telegram.middlewares.activity import ActivityMiddleware
from telegram.middlewares.throttling import ThrottlingMiddleware


class MainController:
    controllers = {}
    middlewares = {}

    def __init__(self, token):
        self.bot = Bot(token=token, parse_mode='HTML')
        self.dispatcher = Dispatcher(self.bot, storage=MemoryStorage())

        # Set controllers
        self.set_controllers(StartController, BuyProductController, UnknownController)

        # Set middlewares
        self.set_middlewares(ActivityMiddleware, ThrottlingMiddleware)

        print(f'Active controllers: {self.controllers}')
        print(f'Active middlewares: {self.middlewares}')

        executor.start_polling(self.dispatcher, skip_updates=True)

    def set_controllers(self, *controllers):
        for controller in controllers:
            self.controllers[controller.__name__] = controller(self.bot, self.dispatcher)

    def set_middlewares(self, *middlewares):
        for middleware in middlewares:
            middleware_obj = middleware()
            self.middlewares[middleware.__name__] = middleware_obj
            self.dispatcher.middleware.setup(middleware_obj)
