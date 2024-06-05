# Flatmates Bill

## Overview
Flatmates Bill is a Python CLI (Command-Line Interface) application designed to fairly split the utility bill among flatmates based on the number of days they stayed in the house during the billing period. The application leverages Object-Oriented Programming (OOP) principles to enhance modularity and maintainability.

The application also shares the generated PDF report using the Filestack API. However, users can modify the code to use any other cloud service for file sharing.

## Features
- **Bill Calculation**: Calculate the share of the bill each flatmate needs to pay based on their days of stay.
- **PDF Report Generation**: Generate a PDF report summarizing the bill details and each flatmate's share.
- **User Input Validation**: Ensure that user inputs are correctly formatted and valid.
- **File Sharing**: Share the generated PDF report using the Filestack API.
- **Customizable File Sharing**: Shares the generated PDF report using the Filestack API, with the option to modify the code for using other cloud services.
- **Error Handling**: Gracefully handle errors during the file-sharing process.

## Setup
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/emads22/Flatmates-Bill.git
    ```
2. **Navigate to the Project Folder**:
    ```sh
    cd path/to/project-folder
    ```
3. **Ensure Python 3.x is Installed**: Check your Python version using:
    ```sh
    python --version
    ```
4. **Install Required Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
5. **Configure Necessary Parameters in `constants.py`**:
   - Edit `constants.py` to set any required constants for the project, such as `FILESTACK_API_KEY`.

## Usage
1. **Run the Script**:
    ```sh
    python main.py
    ```
2. **Enter Bill Details**:
   - Follow the prompts to enter the total bill amount, bill period, and each flatmate's name and days stayed.
3. **View Calculation Results**:
   - The script will calculate and print each flatmate's share of the bill.
4. **Generate PDF Report**:
   - A PDF report will be generated summarizing the bill details and each flatmate's share.
5. **Share the PDF Report**:
   - The generated PDF report will be uploaded using the Filestack API, and a URL link to the report will be provided.
   - If an error occurs during the file-sharing process, an error message will be displayed.

## Example
Here’s an example of how to use the Flatmates Bill application:

1. **Run the script**:
    ```sh
    python main.py
    ```
2. **Input the following when prompted**:
    - **Total Bill Amount**: `$300`
    - **Bill Period**: `May 2024`
    - **Flatmate 1 Name**: `Alice`
    - **Days Stayed by Alice**: `20`
    - **Flatmate 2 Name**: `Bob`
    - **Days Stayed by Bob**: `10`
3. **The script will output**:
    ```sh
    Alice pays: $200.00
    Bob pays: $100.00
    ```
4. **Check the project directory for a PDF report named `May_2024_Bill.pdf`**.
5. **The terminal will display a URL to the shared PDF report**:
    ```sh
    --- PDF Flatmates Bill generated successfully.
    You can find it here: "https://cdn.filestackcontent.com/your-uploaded-file-url" ---
    ```

## Files Description
- **main.py**: The main script that runs the application, handles user input, calculates bill shares, and generates the PDF report.
- **app_utils.py**: Contains utility functions for validating user input (float, integer, date).
- **constants.py**: Defines constants used throughout the project, such as file paths and API keys.
- **classes.py**: Defines the core classes for the application:
  - `Bill`: Represents the bill with total amount and billing period.
  - `Flatmate`: Represents a flatmate with name and days stayed in the house, and calculates their share of the bill.
  - `PdfReport`: Generates a PDF report of the bill and flatmates' shares.
  - `FileShare`: Handles sharing the PDF report using the Filestack API.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.