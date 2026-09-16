from src.buttons.button import Button


class ResetButton(Button):
    """Child of Button that resets inputs.

    Args:
        Button (class): Custom generic button class
    """

    def button_clicked(self) -> None:
        """If button is clicked: triggers reset action."""
        self._parent.input = ""
        self._parent.label.setText(self._parent.input)
        self._parent.tmp_input = ""
        self._parent.calc_label.setText(self._parent.tmp_input)
