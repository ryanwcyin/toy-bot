import logging
import os
import datetime
import pytz
import requests
from config import config
from utils.metaclass import SingletonType


class TGLogHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        self.token = config.telegram_token
        self.user_id = config.telegram_id
        self.url = "https://api.telegram.org/bot{}/sendMessage".format(self.token)

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        payload = {
            "text": msg.encode("utf8"),
            "chat_id": self.user_id
        }
        requests.post(self.url, payload)


class Logger(object, metaclass=SingletonType):
    # __metaclass__ = SingletonType   # python 2 Style
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

        now = datetime.datetime.now()
        dirname = os.path.join("logs")

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        file_handler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d") + ".log")

        stream_handler = TGLogHandler()

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

    def get_logger(self):
        return self._logger
