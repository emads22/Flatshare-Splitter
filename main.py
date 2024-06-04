from app_utils import Bill, Flatmate, PdfReport


def validate_float(prompt):
    """
    Prompt the user to enter a positive floating-point number.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        float: The validated positive floating-point number.

    Raises:
        ValueError: If the input is not a valid float or is a negative number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("\n-- Invalid input. Please enter a positive number. --\n")


def validate_int(prompt):
    """
    Prompt the user to enter a positive integer.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        int: The validated positive integer.

    Raises:
        ValueError: If the input is not a valid integer or is a negative number.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("\n-- Invalid input. Please enter a positive integer. --\n")


def main():
    """
    Main function to prompt the user for bill and flatmate information, 
    calculate each flatmate's share of the bill, and generate a PDF report.

    Prompts the user for:
        - Total bill amount (validated as a positive float).
        - Bill period (formatted as a title case string).
        - First flatmate's name and number of days stayed (validated as a positive integer).
        - Second flatmate's name and number of days stayed (validated as a positive integer).

    Prints each flatmate's share of the bill and generates a PDF report.
    """
    # Prompt user for input
    bill_amount = validate_float("\n\n- Enter the total bill amount: ")
    bill_period = input(
        "\n- Enter the bill period (e.g., 'March 2024'): ").title()

    # Get details for the first flatmate
    name1 = input("\n\n- Enter the first flatmate's name: ").title()
    days1 = validate_int(f'  Enter the number of days "{
        name1}" stayed in the house: ')

    # Get details for the second flatmate
    name2 = input("\n\n- Enter the second flatmate's name: ").title()
    days2 = validate_int(f'  Enter the number of days "{
        name2}" stayed in the house: ')

    # Create Bill and Flatmate instances
    the_bill = Bill(amount=bill_amount, period=bill_period)
    flatmate1 = Flatmate(name=name1, days_in_house=days1)
    flatmate2 = Flatmate(name=name2, days_in_house=days2)

    # Print the payment information
    print(f'\n\n>> {flatmate1.name} pays ${flatmate1.pays(bill=the_bill,
          flatmate=flatmate2)}')
    print(f'\n>> {flatmate2.name} pays ${flatmate2.pays(bill=the_bill,
          flatmate=flatmate1)}')

    # Generate the PDF report
    report = PdfReport(flatmate1, flatmate2, the_bill)
    report.generate()


if __name__ == "__main__":
    try:
        main()
        print(f"\n\n--- PDF Flatmates Bill generated successfully. ---\n\n")
    except Exception as e:
        print(f"\n\n--- An error occured: {e} ---\n\n")
