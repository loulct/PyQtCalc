"""Main python file of Calc module."""

from logging import INFO, Logger, basicConfig, getLogger
from sys import argv

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QVBoxLayout,
    QWidget,
)

from src.buttons.button import Button
from src.buttons.delete_button import DeleteButton
from src.buttons.operation_button import OperationButton
from src.buttons.reset_button import ResetButton
from src.buttons.result_button import ResultButton
from src.const import Buttons, Colors, Global, History, Numbers
from src.history.history import HistoryWindow


class CalcApp(QMainWindow):
    """Calculator app main window class.

    Args:
        QMainWindow (class): Qt Main window class.
    """

    def __init__(self, parent_app: QApplication, logger: Logger, title: str):
        """__init__

        Args:
            parent_app (QApplication): Parent application.
            logger (Logger): Instance of Logger.
            title (str): App title.
        """
        super().__init__()

        self.logger = logger

        self.setWindowTitle(title)

        self.parent_app = parent_app

        self.menu: QMenuBar | None = self.menuBar()
        self.file_menu: QMenu | None = (
            self.menu.addMenu(Global.MENU_TITLE) if self.menu else None
        )
        self.quit_button = QAction(Global.QUIT_LABEL, self)
        self.file_menu.addAction(self.quit_button) if self.file_menu else None

        self.quit_button.triggered.connect(self.quit_app)
        self.quit_button.setShortcut(QKeySequence(Global.QUIT_SHORTCUT))

        self.tmp_input: str = ""
        self.input: str = ""
        self.has_result = False
        self.history = []
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.calc_label = QLabel()
        self.calc_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        widgets = [
            [self.calc_label],
            [self.label],
            [
                ResetButton(self, Buttons.RESET_LABEL, Colors.RED),
                DeleteButton(self, Buttons.DELETE_LABEL, Colors.RED),
                Button(self, Buttons.LEFT_BRACKET_LABEL),
                Button(self, Buttons.RIGHT_BRACKET_LABEL),
            ],
            [
                Button(self, Numbers.ONE),
                Button(self, Numbers.TWO),
                Button(self, Numbers.THREE),
                OperationButton(self, Buttons.DIVIDE_LABEL),
            ],
            [
                Button(self, Numbers.FOUR),
                Button(self, Numbers.FIVE),
                Button(self, Numbers.SIX),
                OperationButton(self, Buttons.MULTIPLY_LABEL),
            ],
            [
                Button(self, Numbers.SEVEN),
                Button(self, Numbers.EIGHT),
                Button(self, Numbers.NINE),
                OperationButton(self, Buttons.MINUS_LABEL),
            ],
            [
                Button(self, Buttons.DOT_LABEL),
                Button(self, Numbers.ZERO),
                ResultButton(self, Buttons.EQUAL_LABEL),
                OperationButton(self, Buttons.ADD_LABEL),
            ],
        ]

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        for line in widgets:
            for column in line:
                h_layout.addWidget(column)
            v_layout.addLayout(h_layout)
            h_layout = QHBoxLayout()

        self.history_button = QAction(History.HISTORY_LABEL, self)
        self.history_button.setCheckable(True)
        self.file_menu.insertAction(
            self.quit_button, self.history_button
        ) if self.file_menu else None
        self.history_button.triggered.connect(self.show_history)
        self.history_button.setShortcut(QKeySequence(History.HISTORY_SHORTCUT))

        container = QWidget()
        container.setLayout(v_layout)

        self.history_window = HistoryWindow(self, History.HISTORY_LABEL)

        self.setCentralWidget(container)
        self.show()

    def show_history(self) -> None:
        """Toggle history window."""
        if self.history_window.isVisible():
            self.history_window.hide()
        else:
            self.history_window.show()

    def closeEvent(self, a0) -> None:
        """Triggers when event of type closing is called.

        Args:
            a0 (QCloseEvent): Qt event.
        """
        self.quit_app()

    def quit_app(self) -> None:
        """End process.

        Args:
            a0 (QCloseEvent): Qt event.
        """
        self.parent_app.quit()


app = QApplication(argv)

logger = getLogger(__name__)
basicConfig(filename=Global.LOG_FILENAME, level=INFO)

window = CalcApp(parent_app=app, logger=logger, title=Global.APP_TITLE)

app.exec()
