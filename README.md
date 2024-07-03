# Python-workout

> IDE used is pycharm Community Edition

## Python

Python is a versatile, high-level programming language known for its readability and ease of use. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python has a vast ecosystem of libraries and frameworks, making it suitable for web development, data analysis, artificial intelligence, and more.

## Types of programs

- **Interactive Program:** These programs require continuous user interaction to function. They often involve user inputs via a graphical user interface (GUI) or command line interface (CLI). Examples include text editors, web browsers, and games.

- **Non-Interactive Programs:** These programs run without requiring real-time user input. They typically perform tasks automatically once executed, such as batch scripts, background services, and automated data processing jobs.

## Python interpreter

The Python interpreter is a program that reads and executes Python code. It can be used interactively via the command line, where users can type and run Python commands in real-time. The interpreter also executes scripts, allowing for batch processing and automation. Its interactive mode is especially useful for testing, debugging, and learning Python.

## Install Python in linux

```sh
sudo apt update
sudo apt install python3
```

## Install PyCharm in linux

```sh
sudo snap install pycharm-community --classic
```

## Difference Between Lists and Tuples in Python

| Feature                   | Lists                      | Tuples                                           |
| ------------------------- | -------------------------- | ------------------------------------------------ |
| **Mutability**            | Mutable (can be changed)   | Immutable (cannot be changed)                    |
| **Syntax**                | Square brackets `[]`       | Parentheses `()`                                 |
| **Methods**               | Extensive set of methods   | Limited set of methods                           |
| **Immutability Benefits** | Not suitable for hash keys | Can be used as hash keys (e.g., in dictionaries) |

### Syntax for Lists

```python
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list)

```

### Syntax for Tuple

```python
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list)

```

## Loops in Python

### While Loop

A `while` loop in Python repeatedly executes a block of code as long as a specified condition is true.

### Syntax

```python
while condition:
    # Code to execute
```

### For Loop

A `for` loop in Python iterates over a sequence (such as a list, tuple, dictionary, set, or string) and executes a block of code for each item in the sequence.

### Syntax

```python
for item in sequence:
    # Code to execute
```

# Common Error Types in Python Methods

1. **SyntaxError**

   - Error Message: `SyntaxError: invalid syntax`

2. **TypeError**

   - Error Message: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

3. **ValueError**

   - Error Message: `ValueError: math domain error`

4. **IndexError**

   - Error Message: `IndexError: list index out of range`

5. **KeyError**

   - Error Message: `KeyError: 'age'`

6. **AttributeError**

   - Error Message: `AttributeError: 'MyClass' object has no attribute 'some_method'`

7. **ImportError**

   - Error Message: `ImportError: No module named 'non_existent_module'`

8. **NameError**

   - Error Message: `NameError: name 'unknown_variable' is not defined`

9. **ZeroDivisionError**

   - Error Message: `ZeroDivisionError: division by zero`

10. **FileNotFoundError**
    - Error Message: `FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'`

# Strings in Python

In Python, a string is a sequence of characters enclosed within either single quotes `' '` or double quotes `" "`. Strings are immutable, meaning their contents cannot be changed after creation.

### Single-line Strings

```python
str1 = 'Hello, World!'
str2 = "Python Programming"
```

## F-strings (Formatted String Literals) in Python

F-strings provide a convenient way to embed Python expressions inside string literals. They were introduced in Python 3.6 and offer a more readable.

### Syntax

To create an f-string, prefix the string with `f` or `F` and use curly braces `{}` to evaluate expressions:

```python
name = "Ram"
age = 30

# Example of f-string
message = f"My name is {name} and I am {age} years old."
print(message)
# Output: "My name is Ram and I am 30 years old."
```

## Using enumerate() Function in for Loop

The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object. This allows you to loop over the iterable and have an automatic counter for the index position.

### Syntax

```python
for index, value in enumerate(iterable):
    # Code to execute
```

## textfiles

### Writing to a Text File

- To write to a text file, you can use the `open` function with the mode set to `'w'` (write) or `'a'` (append). Here’s how you can do it:

```python
# Writing to a text file (this will overwrite the file if it exists)
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')

# Appending to a text file (this will add content to the file if it exists)
with open('example.txt', 'a') as file:
    file.write('Appending a new line.\n')
```

### Reading from a Text File

 To read from a text file, you can use the `open` function with the mode set to `'r'` (read). Here’s how you can do it:

```python
# Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```



