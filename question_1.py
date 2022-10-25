class Dialog:
    def __init__(self, position_x: int, position_y: int, show: bool) -> None:
        """
            Base class with three properties initialized at construction
            :param int position_x: Position X
            :param int position_y: Position Y
            :param bool show: Can the dialog show by default?
            :return: None
            :rtype: None
        """
        self.position_x = position_x
        self.position_y = position_y
        self.show = show

    @classmethod
    def show_default_message(cls) -> None:
        """
            Empty class method: Show default message
            :param: None
            :return: None
        """
        pass

    def render(self) -> None:
        """
            Empty instance method: Render dialog
            :param: None
            :return: None
        """
        pass
