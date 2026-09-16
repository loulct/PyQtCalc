from PyQt6.QtGui import QKeySequence, QShortcut

from src.buttons.button import Button


class DeleteButton(Button):
    """Child of Button that remove latest appended input.

    Args:
        Button (_type_): Custom generic button class.
    """

    def __init__(self, parent, text: str, color: str | None = None):
        super().__init__(parent, text, color)
        self.del_shortcut = QShortcut(QKeySequence.StandardKey.Delete, self)
        self.back_shortcut = QShortcut(QKeySequence.StandardKey.Back, self)
        self.del_shortcut.activated.connect(self.button_clicked)
        self.back_shortcut.activated.connect(self.button_clicked)

    def button_clicked(self) -> None:
        """If button is clicked: remove latest input."""
        self._parent.input = self._parent.input[:-1]
        self._parent.label.setText(self._parent.input)
