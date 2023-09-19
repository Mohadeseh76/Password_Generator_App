# Password Generator App

The **Password Generator App** is a simple desktop application built using the Python tkinter library. It allows users to generate random passwords with customizable settings such as length and character types. This README file provides an overview of the project, its features, and instructions for running it on your computer.

![Screenshot 2023-09-19 172735](https://github.com/Mohadeseh76/To-Do_List/assets/141071219/be39e626-26e5-44d1-8aa8-080adaf47f8f)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **Password Generation**: The app generates random passwords based on user-defined criteria.
2. **Customizable Settings**: Users can specify the desired length and choose to include or exclude character types such as uppercase letters, lowercase letters, numbers, and symbols.
3. **Duplicate Character Exclusion**: Users can opt to exclude duplicate characters from the generated password.
4. **Copy to Clipboard**: The app provides a "Copy Password" button that allows users to quickly copy the generated password to their clipboard for easy use.

## Requirements

To run the Password Generator App, you need the following:

- Python 3.x installed on your computer.
- The `tkinter` library, which is typically included with Python by default.
- The `pyperclip` library for copying passwords to the clipboard.

## Installation

1. **Clone the Repository**: Begin by cloning this GitHub repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/password-generator-app.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required Python dependencies using pip:

   ```
   pip install pyperclip
   ```

## Usage

1. **Run the Application**: Execute the `password_generator.py` script to launch the Password Generator App.

   ```
   python password_generator.py
   ```

2. **Generate a Password**:

   - Check or uncheck the checkboxes to specify the character types you want to include in the generated password.
   - Use the "Password Length" dropdown to select the desired length of the password.
   - If you want to exclude duplicate characters, check the "Exclude Duplicate Characters" checkbox.

3. **Generate Password**:

   - Click the "GENERATE RANDOM PASSWORD!" button to generate a random password based on your settings.
   - The generated password will appear in the text box.

4. **Copy to Clipboard**:

   - Click the "Copy Password" button to copy the generated password to your clipboard.
   - You can now paste the password into any application or website that requires a password.


## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
