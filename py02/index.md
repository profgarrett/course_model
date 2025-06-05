# Python Sequence

## Learning Outcomes: Python Sequences and Collections

By the end of this section, you will be able to:

- **Lists**:  Create, access, modify, and delete elements; use list methods; perform slicing and indexing.

  ```python
  # Create a list
  numbers = [10, 20, 30]
  print(numbers[0], numbers[-1])  # Access first and last
  numbers[1] = 99  # Modify
  numbers.append(40)  # Add
  del numbers[0]  # Delete
  print(numbers[1:3])  # Slicing
  ```

- **Numpy Arrays**: Create arrays; perform elementwise operations and broadcasting; aggregate (sum, mean, std, etc.); use boolean indexing and filtering.

  ```python
  import numpy as np
  arr = np.array([1, 2, 3])
  print(arr + 5)  # Elementwise
  print(arr.mean(), arr.std())
  print(arr2)
  print(arr[arr > 1])  # Boolean indexing
  ```

- **Dictionaries**: Store key-value pairs; access, add, update, and delete entries; iterate over keys/values/items

  ```python
  d = {'a': 1, 'b': 2}
  d['c'] = 3  # Add
  d['a'] = 10  # Update
  del d['b']  # Delete
  for k, v in d.items():
      print(k, v)
  ```


- **Tuples**: Understand immutability; create and access tuples; use tuples for multiple return values.

  ```python
  t = (1, 2, 3)
  print(t[0])
  # t[1] = 5  # Error: tuples are immutable
  def min_max(lst):
      return min(lst), max(lst)
  lo, hi = min_max([3, 1, 4])
  print(lo, hi)
  ```

- **Sets**: Store unique values; perform set operations (union, intersection, difference); remove duplicates from data.

  ```python
  s = {1, 2, 3, 2}
  s.add(4)
  print(s)
  t = {3, 4, 5}
  print(s | t)  # Union
  print(s & t)  # Intersection
  print(s - t)  # Difference
  unique = set([1, 2, 2, 3])
  print(unique)
  ```


- **General**: Choose the appropriate data structure for a task; Understand differences in performance and use-cases.

## Reading Link

[Whirlwind Tour: Built-in Data Structures](https://jakevdp.github.io/WhirlwindTourOfPython/06-built-in-data-structures.html)

## Practice Problems

- [Python Sequences and Collections Practice](template.ipynb)
