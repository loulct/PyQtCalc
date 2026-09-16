from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import QPushButton

from src.const import Buttons


class Button(QPushButton):
    """_summary_

    Args:
        QPushButton (_type_): _description_
    """

    def __init__(self, parent, text: str, color: str | None = None):
        """_summary_

        Args:
            parent (CalcApp): _description_
            text (str): _description_
            color (str | None, optional): _description_. Defaults to None.
        """
        super().__init__(text=text)
        self._parent = parent
        self._text = text
        if color is not None:
            self.setStyleSheet("QPushButton { " + f"color: {color}" + " }")
        self.clicked.connect(self.button_clicked)

        if self._text not in Buttons.RESET_LABEL + Buttons.DELETE_LABEL:
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
