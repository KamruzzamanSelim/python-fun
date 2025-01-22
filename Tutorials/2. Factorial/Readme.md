Here's the complete script and the `README.md` for your GitHub repository:

### Python Script (`factorial_calculator.py`)

```python
while True:
    number = int(input("Enter Your Number: "))
    if number <= 0:  # Check if the number is less than or equal to zero
        print("Bye")
        break  # Exit the loop
    elif number == 1:  # Check if the number is 1
        print("Your Factorial is: 1")
    else:  # Calculate factorial for numbers greater than 1
        product = 1
        for i in range(1, number + 1):
            product *= i
        print("Your Factorial is:", product)
```

### README File (`README.md`)

```markdown
# Factorial Calculator

This repository contains a simple Python script that calculates the factorial of a number entered by the user. The program demonstrates basic control flow and iteration in Python.

## Features

- Prompts the user to input a number.
- Calculates the factorial of numbers greater than 1.
- Handles edge cases for numbers less than or equal to 0.
- Exits gracefully when the user enters a non-positive number.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/factorial-calculator.git
   cd factorial-calculator
   ```

2. Run the script:
   ```bash
   python factorial_calculator.py
   ```

3. Follow the prompts:
   - Enter a positive integer to calculate its factorial.
   - Enter `0` or a negative number to exit the program.

## Example

```plaintext
Enter Your Number: 5
Your Factorial is: 120

Enter Your Number: 1
Your Factorial is: 1

Enter Your Number: -1
Bye
```

## Requirements

- Python 3.x

## How It Works

1. The script continuously prompts the user for input.
2. If the user enters a number less than or equal to 0, the program prints "Bye" and exits.
3. If the number is 1, the program outputs `1` as the factorial.
4. For numbers greater than 1, the program calculates the factorial using a loop and displays the result.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Steps to Add to GitHub
1. Create a new GitHub repository.
2. Add the `factorial_calculator.py` file and `README.md` to the repository.
3. Commit the files with a meaningful message, such as `Initial commit with script and README`.
4. Push the code to your GitHub repository. 

Let me know if you need further assistance!