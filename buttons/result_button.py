from buttons.button import Button
from PyQt6.QtGui import QKeySequence, QShortcut

from const import ResultValues, History


class ResultButton(Button):
    """_summary_

    Args:
        Button (_type_): _description_
    """

    def __init__(self, parent, text: str, color: str | None= None):
        super().__init__(parent, text, color)
        self._shortcut = QShortcut(QKeySequence.StandardKey.InsertParagraphSeparator, self)
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
            self._parent.calc_label.setText(ResultValues.ERROR_VALUE)
            self._parent.input = ""
            self._parent.label.setText(self._parent.input)
        else:
            self._parent.calc_label.setText(self._parent.tmp_input)
            self._parent.label.setText(self._parent.input)
            self._parent.has_result = True
            self._parent.history.append(
                {
                    History.CALC_KEY: self._parent.tmp_input,
                    History.RESULT_KEY: self._parent.input,
                }
            )
            self._parent.logger.info(f"{self._parent.history}")
            self._parent.history_window.update_history()
