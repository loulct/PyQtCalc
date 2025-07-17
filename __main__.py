"""Main python file of Calc module."""

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QScrollArea,
    QFormLayout,
    QGroupBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QCloseEvent, QKeySequence, QShortcut
from sys import argv
from logging import Logger, getLogger, basicConfig, INFO
from typing import Union

class CalcApp(QMainWindow):
    """_summary_

    Args:
        BaseMenuMainWindow (_type_): _description_
    """

    def __init__(self, parent_app: QApplication, logger: Logger, title: str):
        """_summary_

        Args:
            parent_app (QApplication): _description_
            logger (Logger): _description_
            title (str): _description_
        """
        super().__init__()

        self.logger = logger

        self.setWindowTitle(title)

        self.parent_app = parent_app

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&File")
        self.quit_button = QAction("Quit", self)
        self.file_menu.addAction(self.quit_button)

        self.quit_button.triggered.connect(self.quit_app)
        self.quit_button.setShortcut(QKeySequence("Ctrl+q"))

        self.tmp_input = ""
        self.input = ""
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
                ACButton(self, "AC", "red"),
                DeleteButton(self, "del", "red"),
                Button(self, "("),
                Button(self, ")"),
            ],
            [
                Button(self, "1"),
                Button(self, "2"),
                Button(self, "3"),
                CalcButton(self, "/"),
            ],
            [
                Button(self, "4"),
                Button(self, "5"),
                Button(self, "6"),
                CalcButton(self, "*"),
            ],
            [
                Button(self, "7"),
                Button(self, "8"),
                Button(self, "9"),
                CalcButton(self, "-"),
            ],
            [
                Button(self, "."),
                Button(self, "0"),
                ResultButton(self, "="),
                CalcButton(self, "+"),
            ],
        ]

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        for line in widgets:
            for column in line:
                h_layout.addWidget(column)
            v_layout.addLayout(h_layout)
            h_layout = QHBoxLayout()

        self.history_button = QAction("History", self)
        self.history_button.setCheckable(True)
        self.file_menu.insertAction(self.quit_button, self.history_button)
        self.history_button.triggered.connect(self.show_history)
        self.history_button.setShortcut(QKeySequence("Ctrl+h"))

        container = QWidget()
        container.setLayout(v_layout)

        self.history_window = HistoryWindow(self, "History")

        self.setCentralWidget(container)
        self.show()

    def show_history(self) -> None:
        """_summary_"""
        if self.history_window.isVisible():
            self.history_window.hide()
        else:
            self.history_window.show()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """_summary_

        Args:
            a0 (QCloseEvent): _description_
        """
        self.quit_app()

    def quit_app(self) -> None:
        """_summary_

        Args:
            a0 (QCloseEvent): _description_
        """
        self.parent_app.quit()


class HistoryWindow(QWidget):
    """_summary_

    Args:
        QWidget (_type_): _description_
    """

    def __init__(self, parent: CalcApp, title: str):
        """_summary_

        Args:
            title (str): _description_
        """
        super().__init__()
        self._parent = parent

        self.setWindowTitle(title)
        self.setMinimumWidth(300)
        self.setMaximumHeight(400)

        self.form_layout = QFormLayout()

        self.group_box = QGroupBox("History")
        self.group_box.setLayout(self.form_layout)

        self._scroll = QScrollArea()
        self._scroll.setWidget(self.group_box)
        self._scroll.setWidgetResizable(True)
        self._scroll.setFixedHeight(400)

        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self._scroll)

        self.shortcut_history = QShortcut(QKeySequence("Ctrl+h"), self)
        self.shortcut_quit = QShortcut(QKeySequence("Ctrl+q"), self)

        self.shortcut_history.activated.connect(self.show_history)
        self.shortcut_quit.activated.connect(self._parent.quit_app)

    def show_history(self):
        """_summary_"""
        if self.shortcut_history.isEnabled():
            self._parent.history_button.setChecked(False)
        self._parent.show_history()

    def update_history(self):
        """_summary_"""
        calc = QLabel(self._parent.history[-1]["calc"])

        result = QLabel(self._parent.history[-1]["result"])
        result.setAlignment(Qt.AlignmentFlag.AlignRight)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)

        self.form_layout.insertRow(0, calc)
        self.form_layout.insertRow(1, QLabel("="), result)
        self.form_layout.insertRow(2, separator)

        self.group_box.setLayout(self.form_layout)


class Button(QPushButton):
    """_summary_

    Args:
        QPushButton (_type_): _description_
    """

    def __init__(self, parent: CalcApp, text: str, color: Union[str, None] = None):
        """_summary_

        Args:
            parent (CalcApp): _description_
            text (str): _description_
            color (Union[str, None], optional): _description_. Defaults to None.
        """
        super().__init__(text=text)
        self._parent = parent
        self._text = text
        if color is not None:
            self.setStyleSheet("QPushButton { " + f"color: {color}" + " }")
        self.clicked.connect(self.button_clicked)

        if self._text not in "ACdel":
            self._shortcut = QShortcut(QKeySequence(self._text), self)
            self._shortcut.activated.connect(self.button_clicked)

    def button_clicked(self) -> None:
        """_summary_"""
        if self._parent.has_result:
            self._parent.tmp_input = ""
            self._parent.calc_label.setText(self._parent.tmp_input)
            self._parent.input = ""
            self._parent.label.setText(self._parent.input)
            self._parent.has_result = False
        self._parent.input += self.text()
        self._parent.label.setText(self._parent.input)


class CalcButton(Button):
    """_summary_

    Args:
        Button (_type_): _description_
    """

    def button_clicked(self) -> None:
        """_summary_"""
        self._parent.input += self.text()
        self._parent.label.setText(self._parent.input)
        self._parent.has_result = False


class ACButton(Button):
    """_summary_

    Args:
        Button (_type_): _description_
    """

    def button_clicked(self) -> None:
        """_summary_"""
        self._parent.input = ""
        self._parent.label.setText(self._parent.input)
        self._parent.tmp_input = ""
        self._parent.calc_label.setText(self._parent.tmp_input)


class DeleteButton(Button):
    """_summary_

    Args:
        Button (_type_): _description_
    """

    def __init__(self, parent: CalcApp, text: str, color: str = None):
        super().__init__(parent, text, color)
        self.del_shortcut = QShortcut(QKeySequence.StandardKey.Delete, self)
        self.back_shortcut = QShortcut(QKeySequence.StandardKey.Back, self)
        self.del_shortcut.activated.connect(self.button_clicked)
        self.back_shortcut.activated.connect(self.button_clicked)

    def button_clicked(self) -> None:
        """_summary_"""
        self._parent.input = self._parent.input[:-1]
        self._parent.label.setText(self._parent.input)


class ResultButton(Button):
    """_summary_

    Args:
        Button (_type_): _description_
    """

    def __init__(self, parent: CalcApp, text: str, color: str = None):
        super().__init__(parent, text, color)
        self._shortcut = QShortcut(
            QKeySequence.StandardKey.InsertParagraphSeparator, self
        )
        self._shortcut.activated.connect(self.button_clicked)

    def button_clicked(self) -> None:
        """
        if self._parent.input == "()()":
            raise TypeError(f"{self._parent.input} 'tuple' object is not callable")
        if "()" in self._parent.input:
            raise TypeError(f"{self._parent.input} object is not callable")
        if self._parent.input == "Ellipsis" or self._parent.input == "()":
            raise SyntaxError(f"{self._parent.input}")
        """
        self._parent.tmp_input = self._parent.input
        try:
            self._parent.input = str(eval(self._parent.input))
        except (SyntaxError, TypeError) as err:
            self._parent.logger.error(f"{err}")
            self._parent.tmp_input = ""
            self._parent.calc_label.setText("ERR")
            self._parent.input = ""
            self._parent.label.setText(self._parent.input)
        else:
            self._parent.calc_label.setText(self._parent.tmp_input)
            self._parent.label.setText(self._parent.input)
            self._parent.has_result = True
            self._parent.history.append(
                {"calc": self._parent.tmp_input, "result": self._parent.input}
            )
            self._parent.logger.info(f"{self._parent.history}")
            self._parent.history_window.update_history()


app = QApplication(argv)

logger = getLogger(__name__)
basicConfig(filename="app.log", level=INFO)

window = CalcApp(parent_app=app, logger=logger, title="Calculator")

app.exec()
