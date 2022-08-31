import logging

from telegram.controllers.main import MainController

logging.basicConfig(level=logging.INFO)

token = '5376576671:AAHJxZmwwIfykzX5MZkS4QjaP6p5-ywQvPU'
MainController(token)
