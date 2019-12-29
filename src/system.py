from datetime import date


class Date:
    def __init__(self, option: str) -> None:
        self._option = option

    def show(self) -> str:
        if self._option == "today":
            return str(date.today())
        raise ValueError(f"{self._option} value is not recognized!")

    def name(self) -> str:
        return self._option
