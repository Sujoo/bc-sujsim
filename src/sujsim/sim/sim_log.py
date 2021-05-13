from enum import Enum, auto


class LogType(Enum):
    LOG_NONE = auto()
    LOG_SPELL = auto()
    LOG_MANA = auto()
    LOG_BUFF = auto()
    LOG_DOT = auto()
    LOG_DEBUG = auto()
    LOG_WAIT = auto()


class LogEntry:
    def __init__(self,
                 log_type: LogType,
                 text: str,
                 time: float):
        self.log_type = log_type
        self.text = text
        self.time = time

    def __repr__(self):
        return '[{}] {}: {}'.format(round(self.time, 2), self.log_type.name, self.text)