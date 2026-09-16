from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import (
    QFormLayout,
    QFrame,
    QGroupBox,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from src.const import Buttons, Global, History, WindowSettings


class HistoryWindow(QWidget):
    """_summary_

    Args:
        QWidget (_type_): _description_
    """

    def __init__(self, parent, title: str):
        """_summary_

        Args:
            title (str): _description_
        """
        super().__init__()
        self._parent = parent

        self.setWindowTitle(title)
        self.setMinimumWidth(WindowSettings.WIDTH)
        self.setMaximumHeight(WindowSettings.HEIGHT)

        self.form_layout = QFormLayout()

        self.group_box = QGroupBox(History.HISTORY_LABEL)
        self.group_box.setLayout(self.form_layout)

        self._scroll = QScrollArea()
        self._scroll.setWidget(self.group_box)
        self._scroll.setWidgetResizable(True)
        self._scroll.setFixedHeight(WindowSettings.HEIGHT)

        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self._scroll)

        self.shortcut_history = QShortcut(QKeySequence(History.HISTORY_SHORTCUT), self)
        self.shortcut_quit = QShortcut(QKeySequence(Global.QUIT_SHORTCUT), self)

        self.shortcut_history.activated.connect(self.show_history)
        self.shortcut_quit.activated.connect(self._parent.quit_app)

    def show_history(self):
        """_summary_"""
        if self.shortcut_history.isEnabled():
            self._parent.history_button.setChecked(False)
        self._parent.show_history()

    def update_history(self):
        """_summary_"""
        calc = QLabel(self._parent.history[-1][History.CALC_KEY])

        result = QLabel(self._parent.history[-1][History.RESULT_KEY])
        result.setAlignment(Qt.AlignmentFlag.AlignRight)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)

        self.form_layout.insertRow(0, calc)
        self.form_layout.insertRow(1, QLabel(Buttons.EQUAL_LABEL), result)
        self.form_layout.insertRow(2, separator)

        self.group_box.setLayout(self.form_layout)
