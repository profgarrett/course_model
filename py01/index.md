# Python Basics

- Symbols
	- Comments start with #
	- Equality ==
	- Assignment =
	- Exponents **
	- Modulo %
	- Integer division //
	- Order of operations (PEMDAS)

- Basic Types
	- Floating point number (e.g., 3.14)
	- Integer number (e.g., 1)
	- What quotes to use for text values: 'single' or "double"
	`Backtick` is not used for strings
	- What is a Boolean: True or False
	- What is an invalid Boolean: T/TRUE/true (not valid in Python)

- Challenging Concepts
	- Keyboard shortcuts to select all and run all code in file (varies by editor, e.g., Ctrl then Shift+Enter in Jupyter)
	- Three different averages: mean, median, mode

- Lists
	- Create a list: [1, 2, 3]
	- Access 1st item from list: list[0]
	- Access last item from list: list[-1]
	- Lists are 0-based
	- Difference between list and numpy array
	- What is the library for tables? pandas (DataFrame)

## Practice Problems

### Symbols and Operators

1. Write a comment explaining what the following line does:

   ```python
   x = 5 ** 2 % 3
   ```

2. Check if 7 is equal to 7.0 in Python. What is the result?

3. Use the assignment operator to store the value 10 in a variable named `score`.

4. What is the result of `8 % 3`? Try it in Python.

5. Write a line of code that checks if 15 is not equal to 20.

6. Use the exponent operator to calculate 2 to the power of 8.

7. Write a comment describing what the modulo operator does.

8. Combine operators: What is the result of `3 * 2 ** 2 + 1`?

9. Write a line of code that checks if a variable `a` is greater than or equal to 5.

10. What is the result of `10 // 3`? (Try integer division.)

### Basic Types

1. Assign a floating point number to a variable and print its type.

   ```python
   y = 2.5
   print(type(y))
   ```

2. Try to use a backtick for a string. What happens?

   ```python
   # Try: `hello`
   # Now try: 'hello' or "hello"
   ```

3. Assign True and false to variables. Which is valid in Python?

   ```python
   a = True
   b = false  # What happens?
   ```

4. Assign an integer to a variable and print its type.

5. Assign a string to a variable using double quotes, then print it.

6. What happens if you try to assign 1.0 to an integer variable and then use it in arithmetic?

7. Assign the value None to a variable. What type is it?

8. Try to assign a variable with a space in its name. What error do you get?

9. Assign a boolean value to a variable and use it in an if statement.

10. What happens if you use a single quote inside a string defined with single quotes?

### Order of Operations

1. Predict the result of this expression, then check in Python:

   ```python
   result = 2 + 3 * 4 ** 2
   print(result)
   ```

2. Add parentheses to the previous expression to make addition happen first.

3. What is the result of `10 - 2 * 3 + 4 / 2`?

4. Write an expression that uses all four basic operators (+, -, *, /) and parentheses.

5. What is the result of `2 ** 3 ** 2`? (Try it in Python and explain.)

6. Use parentheses to change the order of operations in `5 + 2 * 10` so that addition happens first.

7. What is the result of `100 / 10 * 2`? Does the order matter?

8. Try `7 + 3 * 2 // 2` and explain the result.

9. Write an expression that evaluates to 0 using only numbers and operators.

10. What is the result of `-3 ** 2`? How can you get 9 instead?

### Lists

1. Create a list of three numbers. Print the first and last item.

   ```python
   my_list = [10, 20, 30]
   print(my_list[0])
   print(my_list[-1])
   ```

2. What happens if you try to access my_list[3]?

3. Create a list of five strings. Print the third string.

4. Change the second item in a list to 99.

5. Append a new value to a list and print the list.

6. Remove the first item from a list and print the result.

7. Use a for loop to print each item in a list.

8. Create a list of numbers from 1 to 10 using `range` and convert it to a list.

9. Use slicing to print the first three items of a list.

10. What is the result of `list[::-1]`? Try it on a list.

11. Check if a value exists in a list using the `in` keyword.

12. Concatenate two lists and print the result.

13. Multiply a list by 3. What happens?

14. Use a list comprehension to create a list of squares from 1 to 5.

15. What is the difference between a list and a tuple?

### Numpy Arrays

1. Convert a list to a numpy array and add 5 to every element.

   ```python
   import numpy as np
   arr = np.array([1, 2, 3])
   print(arr + 5)
   ```

2. What is the difference between a list and a numpy array when you multiply by 2?

   ```python
   print([1, 2, 3] * 2)
   print(np.array([1, 2, 3]) * 2)
   ```

3. Create a numpy array of zeros with length 5.

4. Create a numpy array of numbers from 0 to 9.

5. Use numpy to calculate the mean of an array.

6. Use numpy to calculate the standard deviation of an array.

7. Add two numpy arrays elementwise.

8. Multiply two numpy arrays elementwise.

9. Use boolean indexing to select all elements greater than 3 in an array.

10. What happens if you try to add a list and a numpy array?

11. Reshape a numpy array from shape (10,) to (2, 5).

12. Use numpy to create a 2D array (matrix) and print its shape.

13. Use numpy to sum all elements in a 2D array.

14. Use numpy to find the maximum value in an array.

15. What is the difference between `np.mean(arr)` and `arr.mean()`?

## End of Chapter Review

1. Write a function that takes a list of numbers and returns the mean, median, and mode.
2. Given a list of numbers, print only the even numbers.
3. Create a list of 10 random integers between 1 and 100. Find the largest and smallest values.
4. Write a function that reverses a list without using `[::-1]`.
5. Given two lists of the same length, create a new list containing the sum of corresponding elements.
6. Explain the difference between using `==` and `is` in Python.
7. What happens if you try to use a variable before assigning it a value?
8. Write a program that counts how many times each value appears in a list.
9. Use numpy to generate 1000 random numbers and plot a histogram (hint: use matplotlib).
10. Write a function that takes a list and returns a new list with only unique values.

## Problems

- [Python Basics Template](template.ipynb)
