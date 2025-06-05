# Python Functions

## Learning Outcomes

By the end of this section, you will be able to:

- Load data into a pandas DataFrame from a csv file
- Understand a pandas Series 
- Understand a pandas DataFrame.
- Access a series in a DataFrame
- Use an index in a DataFrame
- Manipulations:
    - Filter rows in a DataFrame based on conditions.
    - Sort DataFrame rows by one or more columns.
    - Join (merge) DataFrames using common columns or indices.
    - Add, modify, or remove columns in a DataFrame (mutate values).

## Code Examples

**Load data into a pandas DataFrame from a csv file:**

_Load a CSV file into a DataFrame for analysis._

```python
import pandas as pd
df = pd.read_csv('data.csv')
```

**Understand a pandas Series:**

_A one-dimensional labeled array._

```python
s = pd.Series([1, 2, 3])
print(s)
```

**Understand a pandas DataFrame:**

_A two-dimensional table of data with columns and rows._

```python
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
```

**Access a series in a DataFrame:**

_Select a single column from a DataFrame._

```python
print(df['A'])
```

**Use an index in a DataFrame:**

_Access rows by label or position._

```python
print(df.loc[0])  # Access row by label
print(df.iloc[0]) # Access row by position
```

**Filter rows in a DataFrame based on conditions:**

_Select rows that meet a condition._

```python
filtered = df[df['A'] > 1]
print(filtered)
```

**Sort DataFrame rows by one or more columns:**

_Order rows by column values._

```python
sorted_df = df.sort_values('B')
print(sorted_df)
```

**Join (merge) DataFrames using common columns or indices:**

_Combine two DataFrames by a shared column._

```python
df2 = pd.DataFrame({'A': [2, 3], 'C': [5, 6]})
merged = pd.merge(df, df2, on='A', how='inner')
print(merged)
```

**Add, modify, or remove columns in a DataFrame (mutate values):**

_Change the columns in a DataFrame._

```python
df['C'] = df['A'] + df['B']  # Add/modify
print(df)
del df['C']                  # Remove
```


## Practice Problems

- [Python Practice](template.ipynb)
