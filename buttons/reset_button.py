from buttons.button import Button


class ResetButton(Button):
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
