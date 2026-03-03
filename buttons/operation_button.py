from buttons.button import Button


class OperationButton(Button):
    """_summary_

    Args:
        Button (_type_): _description_
    """

    def button_clicked(self) -> None:
        """_summary_"""
        self._parent.input += self.text()
        self._parent.label.setText(self._parent.input)
        self._parent.has_result = False
