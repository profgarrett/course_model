
# Python

Textbook: [How to Think like a Data Scientist](https://runestone.academy/ns/books/published/httlads/index.html)

## Chapter 1:  Introduction

Outcomes:
- Differentiate data science v. statistics
- Identify different steps along different data science pipelines
- Be able to identify if you are in a performance zone or learning zone and transition between them as necessary.

Key Terms:
- **Data Science** - combines technical, domain, and statistical skills   
- **Data Science Pipeline** - the series of steps to analyze data and communicate data meaning to stakeholders.    Consists of getting data, EDA, data cleaning, rescaling, creating training/test splits, model building, model testing, and polishing/presenting
- **Learning Zone** - A time to practice old skills, try new skills with the ability to learn or fail without repercussions.    
- **Performance Zone** - A time to utilize and execute skills with minimal mistakes to achieve optimal results.

# Chapter 2: Exploring the Data Science Pipeline via Descriptive Statistics

[link](https://runestone.academy/ns/books/published/httlads/Statistics/toctree.html#exploring-the-data-science-pipeline-via-descriptive-statistics)

Learning Goals

(https://runestone.academy/ns/books/published/httlads/Statistics/introduction.html#learning-goals "Permalink to this heading")

- Distinguish between descriptive and inferential statistics.
- Describe different types of data (continuous/discrete, and numeric/text) 
- Learn to apply the various measures of central tendency and the measures of variability.
- Extrapolate measures of central tendencies and measures of variability of a given data set.
- Combine different datasets and use them to extract new data.
- Compare and contrast data from various datasets using visual representations.
- Learn to create and use spreadsheet pivot tables.

Terms:
* Normal distribution, 
* Variance, standard deviation
* Range, min/max
* Median, mean, mode
* Correlation, correlation matrix

Datasets
* World happiness report [link](https://runestone.academy/ns/books/published/httlads/Statistics/cs1_exploring_happiness.html)
* Doing business - world bank [link](https://runestone.academy/ns/books/published/httlads/Statistics/cs2_exploring_business_data.html)

# Chapter 3: Optimization with Solver

NA

# Chapter 4: Python and Jupyter Notebooks

- Review the fundamental constructs of programming in Python.
- Learn to use a type of programming notebook that mixes text and code
- Use the fundamentals of programming in Python.    
- Learn to use the Markdown language.
- Learn to set up a Jupyter Notebook 

### Python
- Variables: string, int, float, boolean, function
	- `print(type(my_var))`
- Math operations: + - / * ** () %
- Boolean operations: `== <= < != and or not`
- String functions:
	- `\n` newline
	- `"""triple multiline quotes"""`
	- sequences: `[] + * in len slicing [:]`
	- functions: `lower`, `upper`, `startswith`, `endswith`, `split`, `title`, `join`
- Conditionals:  `if elif else`
- Lists: 
	- indexing: `[1] [-1] []*2`
	- use `range` to create lists
	- 
	- functions: `min max sum append`
- For loops
	- `for i in range:`
- Dictionaries `{key = value, ...}`
- Functions `def f(): ... return (1)`
- Map function `map(function, data)`
- Lambda ` lambda parameters : expression`
- List comprehensions:
	-`[new_item for old_item in my_list]`
	- `new_values = x*2 for x in my_list]
	- Filter: `[new for old in my_list if old == 1]`
- Opening files 
	- `with open(filename, 'r') as md:`
- Random 
	- `import random`
	- `random.randrange(10, 20)`


**Booleans:** A Boolean is a data type in Python that has either a value of `True` or `False`. Booleans can be used with logical operators to form complex logical questions which determine the condition for the task to be executed.

**Characters:** A character is a single letter, number or symbol that you can type with one key on a keyboard.

**Conditional Statements:** A conditional statement, also known as an if-statement, is a control structure that runs particular blocks of code only under certain conditions.

**Dictionaries:** Dictionaries are a data type that is comprised of key-value pairs where the keys are used to retrieve the values.

**for loops:** A `for` loop is used to iterate over a sequential collection of elements. It is used when you want to repeat the same task a certain number of times.

**Fruitful Functions:** Fruitful functions are functions which have a return value.

**Functions:** Functions are a reusable block of code that are created to execute a specific task or set of tasks. They are defined using the keyword `def` and may optionally have one or more parameters or and optionally a return value.

**Lambda Function:** The Lambda function is a simple one-line function that can be used to do computations without writing multiple lines of code.

**Lists:** Lists are a data type consisting of a sequential collection of values that may or may not have the same data type.

**List Comprehension:** List comprehensions are a concise way to create a list from another list using specifications.

**Logical Operators:** Logical operators are rational operators (`and`, `or` and `not`) used in the comparison of two or more statements to return Boolean values.

**Map Functions:** The map function is a function that allows for every item in a list to be used as a parameter to a function. It takes a function and a list as parameters and assigns each item in the list as an input parameter to the function.

**Mutable:** A data type is said to be mutable when its value can be changed or overwritten without requiring a new memory location to be assigned.

**Range:** Range is a Python function used to specify a counting sequence starting from one number and ending to the second one. It can be used with parameters to specify how the counting goes on.

**Return Value:** A return value is the output a function gives that is not directly printed but is passed along. Return values are necessary when writing a function whose output is reused. You may only have zero or one return values, not more.

**Strings:** Strings are a data type that has a sequential collection of zero of characters that are enclosed in single, double or triple quotes.

**Variables:** A variable is a value holder that needs to have a name and an allocated memory location. Variables in Python are dynamically typed, i.e. Python will automatically recognize the data type if the value changes its data type.

**Parameter:** Parameters are the input(s) that a function takes in when it requires one to execute its task. Parameters are defined when the function is defined. You may have zero or more parameters.

### Jupyter Notebooks

Install Anaconda
Run jupyter
- Markdown
- Code cells
# Chapter 5: Learning Pandas

- Learn how to create and manipulate a `DataFrame`.
- Learn how to use data from multiple `DataFrames`.
- Be able to use Jupyter Notebooks and Pandas.    
- Be able to import data into a `DataFrame`.    
- Be able to manipulate `DataFrames` to gain specific information.

Text Cells
- `shift+return` to confirm changes
- `**Bold**`

Code cells
- Use `print()` or place a variable on the last line to see output.

Panda exercises
- Movies: read_csv, dropna, head, 
- Preqreq: filter, budget lookup, 
- iloc, loc, use to_numeric to create a index

Keywords

`import`: Import lets programmers use packages, libraries or modules that have already been programmed.

`<DataFrame>[<string>]`: return the series corresponding to the given column (<string>).

`<DataFrame>[<list of strings>]`: returns a given set of columns as a `DataFrame`.

`<DataFrame>[<series/list of Boolean>]`: If the index in the given list is `True` then it returns the row from that same index in the `DataFrame`.

`<DataFrame>.loc[ ]`: Uses explicit indexing to return a `DataFrame` containing those indices and the values associated with them.

`<DataFrame>.loc[<string1>:<string2>]`: This takes in a range of explicit indices and returns a `DataFrame` containing those indices and the values associated with them.

`<DataFrame>.loc[<string>]`: Uses an explicit index and return the row(s) for that index value.

`<DataFrame>.loc[<list/series of strings>]`: Returns a new `DataFrame` containing the labels given in the list of strings.

`<DataFrame>.iloc[ ]`: Uses implicit indexing to return a `DataFrame` containing those indices and the values associated with them.

`<DataFrame>.iloc[<index, range of indices>]`: This takes in an implicit index (or a range of implicit indices) and returns a `DataFrame` containing those indices and the values associated with them.

`<DataFrame>.set_index [<string)>]`: Sets an existing column(s) with the <string> name as the index of the `DataFrame`.

`<DataFrame>.head(<numeric>)`: Returns the first <numeric> element(s). If no parameter (<numeric>) is set then it will return the first five elements.

`<pandas>.DataFrame(<data>)`: Used to create a `DataFrame` with the given data.

`<pandas>.read_csv()`: Used to read a csv file into a `DataFrame`.

`<DataFrame>.set_index(<column>)`: Gets the values of the given column and sets them as indices. The output will be sorted in accending order based on the new indices.

`<pandas>.to_numeric()`: Converts what is inside the parenthesis into neumeric values.

`<series>.str.startswith(<string>)`: `.str.startswith()` (in pandas) checks if a series contains a string(s) that starts with the given prarameter (<string>), and returns a boolean value (True or False).

`<data frame>.sort_index()`: Sorts the different objects in the `DataFrame`. By default, the `DataFrame` is sorted based on the first column in accending order.

# Chapter 6: EDA

Outcomes/Goals
- Visualize, analyze, and describe data in various formats
- Extract data from different sources
- Summarizes the data of a large data set
- Use Pandas to analyze and describe data    
- Visualize data with histograms and scatter plots
- Graph data on a map using web API
- Extract, clean, and save data from web documents
