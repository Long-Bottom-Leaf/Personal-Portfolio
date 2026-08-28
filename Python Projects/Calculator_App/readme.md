# Calculator

A command-line calculator application built with Python. The project started with basic arithmetic operations and was expanded to include advanced mathematics, financial calculations, input validation, error handling, and unit testing.

## Features

### Basic Calculations

* Addition
* Subtraction
* Multiplication
* Division
* Support for calculations using more than two numbers

### Advanced Calculations

* Square roots
* Powers/exponents
* Percentages
* Absolute values

### Financial Calculations

* Simple interest
* Compound interest
* Interest calculation submenu
* Total amount and interest earned displayed for financial calculations

### Input Validation & Error Handling

* Validates menu choices
* Validates numeric input
* Validates minimum numbers required for basic operations
* Validates positive compounding periods
* Handles division by zero
* Handles square roots of negative numbers
* Re-prompts users when invalid numeric input is entered

### Testing

The project includes unit tests using Python's built-in `unittest` framework.

Tests cover:

* Basic mathematical functions
* Multiple-number calculations
* Division by zero
* Advanced mathematical functions
* Financial calculations
* Input validators
* User input validation with mocked input

## Requirements

* Python 3.x
* No external dependencies are required

## How to Run

Clone the repository and navigate to the calculator project directory.

Run the application with:

```bash
python main.py
```

The calculator will display the main menu:

```text
==== Calculator ====

--- Basic Operations ---
1. Add
2. Subtract
3. Multiply
4. Divide

--- Advanced Operations ---
5. Square Root
6. Power
7. Percent
8. Absolute Value

--- Financial Calculations ---
9. Interest

10. Exit
```

Enter the number corresponding to the calculation you want to perform.

## Examples

### Addition

```text
Enter choice: 1
Enter numbers separated by spaces: 10 20 30

10.0 + 20.0 + 30.0 = 60.0
```

### Square Root

```text
Enter choice: 5
Enter number: 25

Square Root: 5.0
```

### Compound Interest

```text
Enter choice: 9

==== Interest Calculator ====

1. Simple Interest
2. Compound Interest

Enter choice: 2
Enter principal: 1000
Enter interest rate (%): 5
Enter time (years): 10
Enter compounding periods per year: 12

Interest Earned: $647.01
Total Amount: $1647.01
```

## Running Tests

From the project root, run:

```bash
python -m unittest discover
```

The test suite will automatically discover and run the project's unit tests.

## Project Structure

```text
Calculator/
│
├── functions/
│   └── math_functions.py
│
├── tests/
│   ├── test_advanced_functions.py
│   ├── test_basic_functions.py
│   ├── test_financial_functions.py
│   └── test_validators.py
│
├── utils/
│   ├── error_messages.py
│   └── validators.py
│
├── main.py
└── README.md
```

## Technologies

* Python
* `math`
* `unittest`
* `unittest.mock`

## Project Goals

This project was created to practice and demonstrate:

* Python functions
* Modular project organization
* Input validation
* Exception handling
* Unit testing
* Command-line application design
* Code refactoring
* Basic financial calculations

## Future Improvements

Possible future improvements could include:

* Additional financial calculations
* More advanced mathematical functions
* Calculation history
* Saving previous calculations
* A graphical user interface
* More extensive automated testing
