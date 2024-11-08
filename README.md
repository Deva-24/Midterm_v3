# Python Calculator Project

This is a feature-rich Python calculator designed to demonstrate principles of Object-Oriented Programming (OOP), error handling, persistence, and software configuration. The calculator supports various arithmetic operations, history tracking, file I/O operations, and more. It also features undo/redo functionality for improved user interaction.

## Features

### Supported Operations:
- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Operations**: Power, Root
- **History**: View past calculations, clear history, undo/redo operations.
- **File Operations**: Save and load history from CSV files.
- **Configuration**: Customizable precision, history size, and max input values via environment variables.

### Commands:
- **Basic Operations**: `add`, `subtract`, `multiply`, `divide`
- **Advanced Operations**: `power`, `root`
- **History Commands**: 
  - `history` – Shows all past calculations.
  - `clear` – Clears the calculation history.
  - `undo` – Undo the last operation.
  - `redo` – Redo the last undone operation.
- **File Operations**:
  - `save` – Save the history to a file.
  - `load` – Load history from a file.
- **Exit**: `exit` – Exits the calculator program.

## Setup

### Prerequisites
Make sure you have Python 3.7+ installed. To install the necessary dependencies, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>



Configuration
You can customize the behavior of the calculator by modifying environment variables or updating the CalculatorConfig class. Available settings include:

CALCULATOR_BASE_DIR: Directory to save logs and history files.
CALCULATOR_MAX_HISTORY_SIZE: Maximum size of the calculation history.
CALCULATOR_AUTO_SAVE: Whether to automatically save history after each operation.
CALCULATOR_PRECISION: Decimal precision for results.
CALCULATOR_MAX_INPUT_VALUE: Maximum allowable input value.
CALCULATOR_DEFAULT_ENCODING: Default encoding for files.


Example of setting environment variables:
export CALCULATOR_MAX_HISTORY_SIZE=50
export CALCULATOR_PRECISION=2


Run the Calculator CLI:
python main.py


File structure:

├── app/
│   ├── calculator.py         # Contains the Calculator class with methods for operations
│   ├── operations.py         # Contains the Operations class for various calculations
│   └── config.py             # Configuration for the calculator (precision, history, etc.)
├── tests/
│   ├── test_calculator.py    # Unit tests for the Calculator class
│   ├── test_operations.py    # Unit tests for the Operations class
├── main.py                   # Main entry point for the command-line interface
├── requirements.txt          # List of required Python dependencies
└── README.md                 # This file


Feel free to fork the repository and submit issues and pull requests. Contributions are welcome!