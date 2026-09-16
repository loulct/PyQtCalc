from src.buttons.button import Button


class OperationButton(Button):
    """Child of Button that appends new inputs.

    Args:
        Button (class): Custom generic button class.
    """

    def button_clicked(self) -> None:
        """If button is clicked: appends input to eval"""
        self._parent.input += self.text()
        self._parent.label.setText(self._parent.input)
        self._parent.has_result = False
