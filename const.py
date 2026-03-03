from enum import StrEnum, IntEnum


class WindowSettings(IntEnum):
    WIDTH = 300
    HEIGHT = 400


class Global(StrEnum):
    APP_TITLE = "Calculator"
    QUIT_LABEL = "Quit"
    QUIT_SHORTCUT = "Ctrl+q"
    MENU_TITLE = "&File"
    LOG_FILENAME = "app.log"


class Numbers(StrEnum):
    ZERO = "0"  # auto() ?
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"


class Colors(StrEnum):
    RED = "red"


class Buttons(StrEnum):
    RESET_LABEL = "AC"
    DELETE_LABEL = "del"
    EQUAL_LABEL = "="
    MULTIPLY_LABEL = ""
    ADD_LABEL = "+"
    MINUS_LABEL = "-"
    LEFT_BRACKET_LABEL = "("
    RIGHT_BRACKET_LABEL = ")"
    DIVIDE_LABEL = "/"
    DOT_LABEL = "."


class ResultValues(StrEnum):
    ERROR_VALUE = "ERR"


class History(StrEnum):
    HISTORY_LABEL = "History"
    CALC_KEY = "calc"
    RESULT_KEY = "result"
    HISTORY_SHORTCUT = "Ctrl+h"
