import sys
from typing import TextIO

from loguru import Contextualizer


class Logger:
    def debug(self, message, *, name: str = None, error: dict = None, http: dict = None) -> None:
        ...

    def info(self, message, *, name: str = None, error: dict = None, http: dict = None) -> None:
        ...

    def warn(self, message, *, name: str = None, error: dict = None, http: dict = None) -> None:
        ...

    def error(self, message, *, name: str = None, error: dict = None, http: dict = None) -> None:
        ...

    def critical(self, message, *, name: str = None, error: dict = None, http: dict = None) -> None:
        ...

    def exception(self, message, *, name: str = None, error: dict = None, http: dict = None) -> None:
        ...

    def contextualize(self, *, name: str = None, error: dict = None, http: dict = None) -> Contextualizer:
        ...


logger: Logger


def setup_logger(
    log_level: str = "INFO",
    sink: TextIO = sys.stdout,
) -> Logger:
    ...
