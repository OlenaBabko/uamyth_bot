import logging


class NotErrorFilter(logging.Filter):
    """
    Filter out log records with level ERROR or higher.
    """

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno < logging.ERROR


class UnicodeFormatter(logging.Formatter):
    def format(self, record):
        record.msg = record.getMessage()
        if isinstance(record.msg, str):
            record.msg = record.msg.encode("utf-8").decode("unicode_escape")
        return super().format(record)
