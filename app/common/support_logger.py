import logging
import threading

import time
from celery.app.log import TaskFormatter

thread_local = threading.local()


def get_support_info():
    return thread_local.support_info if hasattr(thread_local, "support_info") else ""


class SupportFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format(self, record):
        record.support_info = str(get_support_info())
        return super().format(record)


class SupportTaskFormatter(TaskFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format(self, record):
        record.support_info = str(get_support_info())
        # print(f"SupportTaskFormatter: {record.support_info}", flush=True)
        return super().format(record)

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt is None:
            datefmt = "%d/%b/%Y:%H:%M:%S %z"  # "%Y-%m-%d %H:%M:%S"
        s = time.strftime(datefmt, ct)
        return s


def setup(logger: logging.Logger, formatter: logging.Formatter):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
