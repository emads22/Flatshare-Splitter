from fpdf import FPDF
from constants import *


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

    def pays(self, bill: Bill, flatmate: 'Flatmate') -> float:
        # We put single quotes around Flatmate ('Flatmate') in the type hint for the flatmate parameter to indicate that it's a string literal representing the class name, rather than an instance of the Flatmate class itself cz here the Flatmate class has not yet been fully defined, so we can't use it as a type hint directly.

        # Calculate the weight of this flatmate's share of the bill
        # This is done by dividing the number of days this flatmate was in the house
        # by the total number of days both flatmates were in the house
        weight = self.days_in_house / \
            (self.days_in_house + flatmate.days_in_house)

        # Calculate the amount this flatmate needs to pay
        # This is done by multiplying the total bill amount by the weight calculated above
        amount_to_pay = bill.amount * weight

        return round(amount_to_pay, 2)


class PdfReport(FPDF):
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amounts, and the period of the bill.
    """

    def __init__(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill) -> None:  # 12 pt = 16 px
        super().__init__(orientation='P', unit='pt', format='A4')
        self.flatmate1 = flatmate1
        self.flatmate2 = flatmate2
        self.bill = bill

    def generate(self) -> None:
        # Start a new page in the PDF
        self.add_page()

        # Set the font for the header
        self.set_font(family='Arial', style='B', size=24)

        # Add image (commented out, uncomment to use)
        # self.image(str(BILL_LOGO), w=40)

        # Set position to the right of the image (commented out, uncomment to use)
        # self.set_xy(35, 8)  # x should be the width of the image + some spacing, y should be the same as image y

        # Add the main title of the document
        self.cell(w=0, h=80, txt="Flatmates Bill", align='C', ln=1)

        # Add the period label and value
        self.set_font_size(22)  # Set font size for the period label
        self.cell(w=100, h=40, txt=f"Period:", ln=0)
        self.set_font(family='Courier')  # Set font for the period value
        self.cell(w=150, h=40, txt=f"{self.bill.period.title()}", ln=1)
        self.ln()  # Add a line break

        # Add the body of flatmates names and respective payment amounts
        self.set_font(family='Arial', size=20)  # Set font for 1st name
        self.cell(w=100, h=40, txt=f"- {self.flatmate1.name}:", ln=0)
        self.set_font(family='Courier')  # Set font for the payment value
        self.cell(w=100, h=40, txt=f"${self.flatmate1.pays(
            self.bill, self.flatmate2)}", ln=1)

        self.set_font(family='Arial')  # Reset font for 2nd name
        self.cell(w=100, h=40, txt=f"- {self.flatmate2.name}:", ln=0)
        self.set_font(family='Courier')  # Set font for the payment value
        self.cell(w=100, h=40, txt=f"${self.flatmate2.pays(
            self.bill, self.flatmate1)}", ln=1)

        # Reset font to Arial for further content if needed
        self.set_font(family='Arial')

        # Define the output file path based on the bill period
        filename = self.bill.period.title().replace(" ", "_")
        output_filepath = BILLS / f'{filename}_Bill.pdf'

        # Save the PDF to the specified file path
        self.output(str(output_filepath))


def main():
    the_bill = Bill(amount=120, period='March 2024')
    john = Flatmate(name='John', days_in_house=20)
    mary = Flatmate(name='Mary', days_in_house=25)

    print(f'\n- John pays ${john.pays(bill=the_bill, flatmate=mary):.2f}')
    print(f'\n- Mary pays ${mary.pays(bill=the_bill, flatmate=mary):.2f}')

    report = PdfReport(john, mary, the_bill)
    report.generate()


if __name__ == "__main__":
    main()
