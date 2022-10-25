from question_1 import Dialog


class WindowsDialog(Dialog):

    def __init__(
            self, position_x: int, position_y: int, show: bool, is_rounded: bool, width: float,
            height: float
    ) -> None:
        """
            Derived class with three additional  properties and inherits from base class
            :param int position_x: Position X
            :param int position_y: Position Y
            :param bool show: Can the dialog show by default
            :param bool is_rounded: Is rounded
            :param float width: Width
            :param float height: Height
            :return: None
            :rtype: None
        """
        super().__init__(position_x, position_y, show)
        self.is_rounded = is_rounded
        self.width = width
        self.height = height

    @classmethod
    def show_default_message(cls) -> None:
        print("The windows dialog default message")

    def render(self) -> None:
        print(
            f"The windows dialog was created with these dimensions: width -> {self.width}, height -> {self.height}\n"
            f"In this position: x -> {self.position_x}, y -> {self.position_y}\n"
            f"Other settings: show -> {self.show}, is_rounded -> {self.is_rounded}"
        )



