# Debugging Exercise: Python Calculator

This code is designed to be used as a debugging exercise, specifically to practice using a debugger with conditional breakpoints.

## Code Description

The Python code implements a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on randomly selected numbers from two predefined lists.

**Key Components:**

* **`add(n1, n2)`:** Returns the sum of `n1` and `n2`.
* **`sub(n1, n2)`:** Returns the difference of `n1` and `n2`.
* **`mul(n1, n2)`:** Returns the product of `n1` and `n2`.
* **`div(n1, n2)`:** Returns the quotient of `n1` and `n2`.
* **`menu()`:** Displays a menu of options (addition, subtraction, multiplication, division, and exit) and prompts the user to enter their choice. It includes error handling to ensure the user enters a valid integer.
* **Main loop:**
    * Calls the `menu()` function to get the user's choice.
    * Uses `randint` to select two random numbers from `C.numberListA` and `C.numberListB`.
    * Prints the indices of the chosen numbers.
    * Performs the selected arithmetic operation using a `match` statement.
    * Prints the result of the operation.
    * The loop continues until the user chooses the "Exit" option.





## How to Use This as a Debugging Exercise

**Set up your debugging environment:**
Use a Python IDE (like VS Code, PyCharm, or others) or the built-in pdb debugger.

**Don't modify the code ! Make it works by using debugger only !** 

## Breakpoint condition example
Simple condition
* `n2==0`

Mutiple condition:
* `n2==0 or not isinstance(...)`


## Insert breakpoints:
* **Use conditional breakpoints**:
This is the crucial part of the exercise. Set conditions on your breakpoints to make the program pause only when specific conditions are met.
* **Modify variables**: Many debuggers allow you to change the values of variables while the program is paused at a breakpoint.

    ### **Place breakpoints at key lines in the code, such as**:

    * At the beginning of each of the arithmetic functions (add, sub, mul, div) with a conditional breakpoint to stop execution if n1 or n2 is not in the right type
    * Inside the while loop in the menu() function, place a log type breakpoint
    * Break only when indexN1 or indexN2 is outside the expected range (to check for potential index errors, although the provided code is unlikely to produce an index error).
    * Break in the div function only if n2 is 0. (Important: The provided code does not handle division by zero. You could add a conditional breakpoint and/or code to handle this.)
    * ...



