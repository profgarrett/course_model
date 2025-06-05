# Python Control Flow

## Learning Outcomes: Python Control Flow

By the end of this section, you will be able to:

- Use `if`, `elif`, and `else` statements to control the flow of a Python program based on conditions.
- Write boolean expressions to compare values and make decisions.
- Iterate over lists, arrays, and ranges using `for` loops.
- Use `for` loops to process and analyze numbers in arrays or lists.
- Apply conditional logic inside loops to filter or transform data.
- Use the `break` and `continue` statements to control loop execution.
- Understand and use the `range()` function for numeric iteration.


## Example Code

### If, Elif, Else Statements

```python
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
```

### Boolean Expressions

```python
n = 5
print(n > 3)      # True
print(n == 5)     # True
print(n != 2)     # True
```

### For Loops Over Lists/Arrays/Ranges

```python
nums = [1, 2, 3, 4]
for num in nums:
    print(num)

for i in range(5):
    print(i)
```

### For Loops to Process Numbers in Arrays/Lists

```python
squares = []
for n in [1, 2, 3, 4]:
    squares.append(n ** 2)
print(squares)
```

### Conditional Logic Inside Loops

```python
nums = [1, 2, 3, 4, 5]
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)
```

### Break and Continue

```python
for n in range(10):
    if n == 5:
        break  # Stop the loop when n is 5
    if n % 2 == 0:
        continue  # Skip even numbers
    print(n)
```

### Using range()

```python
for i in range(3, 8):
    print(i)
```

### Combining Loops and Conditionals for Data Analysis

```python
# Print all numbers greater than 10 in a list
arr = [4, 12, 7, 15, 3]
for n in arr:
    if n > 10:
        print(n)
```


## Practice Problems

- [Python Practice](template.ipynb)
