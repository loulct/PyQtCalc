from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import QPushButton

from src.const import Buttons


class Button(QPushButton):
    """Custom generic button class.

    Args:
        QPushButton (class): Qt Button.
    """

    def __init__(self, parent, text: str, color: str | None = None):
        """__init__

        Args:
            parent (CalcApp): Parent app/window.
            text (str): Label of button.
            color (str | None, optional): Color of label content. Defaults to None.
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
        """If button is clicked: inputs content of button's label inside the eval."""
        if self._parent.has_result:
            self._parent.tmp_input = ""
            self._parent.calc_label.setText(self._parent.tmp_input)
            self._parent.input = ""
            self._parent.label.setText(self._parent.input)
            self._parent.has_result = False
        self._parent.input += self.text()
        self._parent.label.setText(self._parent.input)
