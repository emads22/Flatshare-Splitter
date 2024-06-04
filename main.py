
class Bill:
    """
    Object that contains data about a bill, Such as total amount and periods of the bill.
    """

    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill) -> None:
        pass


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amounts, and the period of the bill.
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill) -> None:
        pass
