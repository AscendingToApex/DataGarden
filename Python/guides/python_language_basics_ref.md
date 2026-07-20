# 🐍 Python Language Basics Reference Guide

A beginner-friendly tour of core Python: how programs are built from **objects**, the **built-in data types**, the four essential **data structures** (list, dict, set, tuple), and the building blocks of logic — **control flow**, **functions**, **iteration**, and **object-oriented programming**.

> New to Python? Read top to bottom. Already comfortable? Jump to any section from the table of contents.

## 📚 Table of Contents

* [🌱 What Is Python?](#-what-is-python)
* [📦 Packages & pip](#-packages--pip)
* [🧱 Data Are Objects](#-data-are-objects)
* [🔤 Built-in Data Types](#-built-in-data-types)
* [🏷️ Variables & Assignment](#-variables--assignment)
* [📋 Lists](#-lists)
* [📖 Dictionaries](#-dictionaries)
* [🎯 Sets](#-sets)
* [📌 Tuples](#-tuples)
* [🔀 Control Flow](#-control-flow)
* [🔁 Loops & Iteration](#-loops--iteration)
* [🧩 Functions](#-functions)
* [🏗️ Object-Oriented Programming](#-object-oriented-programming)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🌱 What Is Python?

- A **high-level**, general-purpose language (named after *Monty Python*, not the snake).
- Free and open source, with a huge ecosystem of third-party libraries.
- The most in-demand language for data science — not because it was built for it, but because of libraries like **NumPy**, **Pandas**, and **Matplotlib**.

> Note: Python was *not* originally designed for numerical computing. Its power for data work comes from the libraries built on top of it.

---

## 📦 Packages & pip

A **package** is extra Python code that isn't part of base Python. Packages bundle **modules** (individual `.py` scripts) you can reuse.

### Installing packages
```bash
pip install pandas              # latest version
pip install "Flask==0.9"        # a specific version
pip install "Flask>=0.8"        # a minimum version
pip install --upgrade pandas    # update to newest
pip uninstall pandas            # remove
```

### Importing packages
```python
import numpy as np              # whole package, aliased as np
from numpy import array         # just one function (a little more efficient)
```

> Pro Tip: By convention, put **all imports at the top** of your script or notebook. In cloud tools like Google Colab you re-import each session, so keeping them together makes restarts painless.

---

## 🧱 Data Are Objects

Everything in Python is an **object** — think of objects as labeled boxes on your computer's memory shelves. Every object carries four things:

| Property          | What it means                                   |
|-------------------|-------------------------------------------------|
| **Type**          | What the object *is* and what it can do         |
| **Unique ID**     | Where the box sits in memory                    |
| **Value**         | The data it holds                               |
| **Reference count** | How many names currently point to it          |

> Note: Python is **strongly typed** — even a *mutable* object cannot silently change its type.

---

## 🔤 Built-in Data Types

| Name        | Type        | Mutable | Example                     |
|-------------|-------------|---------|-----------------------------|
| Boolean     | `bool`      | no      | `True`, `False`             |
| Integer     | `int`       | no      | `1`, `4`, `37_000`          |
| Float       | `float`     | no      | `3.14`                      |
| Complex     | `complex`   | no      | `3j`, `5+4j`                |
| String      | `str`       | no      | `'hello'`                   |
| List        | `list`      | **yes** | `['who', 'what', 'where']`  |
| Tuple       | `tuple`     | no      | `(8, 5, 6)`                 |
| Set         | `set`       | **yes** | `{3, 6, 7}`                 |
| Frozen set  | `frozenset` | no      | `frozenset(['a', 'b'])`     |
| Dictionary  | `dict`      | **yes** | `{'game': 'Tetris'}`        |

**Mutability** = whether the value can change after it's created. Mutable types can be edited in place; immutable types cannot.

```python
a = 2          # int
b = 5.0        # float
x = "Hello!"   # str
print(type(a), type(b), type(x))
```

> Pro Tip: Use `type(obj)` to check any object's type, and `help(obj)` to list what it can do.

---

## 🏷️ Variables & Assignment

A **variable** is a name that stands in for a value: `name = value`.

- Identifiers must start with a letter or underscore and are **case-sensitive** (`age` ≠ `Age`).
- **Order matters** — define a variable before you use it (top→bottom, left→right).

```python
first = 1
second = 2
third = first + second   # variables can build on each other
print(third)             # 3
```

> Note: **Literals** are hard-coded constants written directly in code (`10`, `"Hello"`). **Variables** are named placeholders you can reassign.

---

## 📋 Lists

An **ordered**, **mutable** collection that can hold mixed types. Created with square brackets `[ ]`.

```python
primes = [2, 3, 5, 7, 11]
misc   = [1, 'foo', 2.71828, None]   # heterogeneous is allowed
nested = [[1, 2, 3], [4, 5, 6]]      # lists of lists
```

### Indexing & slicing (zero-based!)
```python
primes[0]      # 2  → first item
primes[-1]     # 11 → last item
primes[0:3]    # [2, 3, 5] → slice is end-exclusive
primes[:3]     # first three
primes[2:]     # from index 2 to the end
```

> Note: Python is **zero-indexed** — `primes[4]` is the *fifth* item. This trips up beginners constantly, so pay attention to it.

### Adding & changing items
```python
primes.append(13)          # add one item to the end (in place)
primes.extend([17, 19])    # add each item of another list
primes + [23, 29]          # returns a NEW combined list (original unchanged)
primes[0] = 1              # change a single value by index
len(primes)                # count the items
```

> Pro Tip: `append(other_list)` adds the whole list as a *single nested element*; `extend(other_list)` adds its items one by one. That difference bites people often.

---

## 📖 Dictionaries

A **mapping** from **keys** to **values** — like a real dictionary mapping words to definitions. Created with curly braces `{ }` and `key: value` pairs.

```python
physicists = {'Albert Einstein': 1879,
              'Marie Curie': 1867}

physicists['Marie Curie']            # 1867 → look up by key
physicists['Nikola Tesla'] = 1856    # add or update a key
del physicists['Marie Curie']        # remove a pair
```

### Looping through a dictionary
```python
for key in physicists:               # iterates over KEYS by default
    print(key, physicists[key])

for value in physicists.values():    # iterate over VALUES
    print(value)

for key, value in physicists.items():# both at once
    print(key, value)
```

### Nested dictionaries
```python
family = {
    'father': {'name': 'Mark', 'age': 54},
    'mother': {'name': 'Debi', 'age': 52},
}
family['father']['name']   # 'Mark'
```

> Note: Index a dict by its **key**, never a numeric position — `physicists[0]` raises a `KeyError` unless `0` is an actual key.

---

## 🎯 Sets

An **unordered**, **mutable** collection of **unique** values. Great for membership tests and removing duplicates.

```python
s = {42, 3.14, 'data'}
s.add(7)
'data' in s               # True → fast membership check
set([1, 1, 2, 2, 3])      # {1, 2, 3} → duplicates dropped
```

---

## 📌 Tuples

Like a list but **immutable** — once created it can't change. Created with parentheses `( )`. Useful for fixed collections and as dictionary keys.

```python
point = (42, 3.14, 'data')
point[0]           # 42 → indexing works like a list
x, y, z = point    # unpack into separate variables
```

---

## 🔀 Control Flow

Run code conditionally with `if` / `elif` / `else`. Indentation (4 spaces) defines the block.

```python
score = 82
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
```

Common comparison and logical operators:

| Operator                | Meaning                    |
|-------------------------|----------------------------|
| `==`, `!=`              | equal, not equal           |
| `<`, `>`, `<=`, `>=`    | comparisons                |
| `and`, `or`, `not`      | combine/negate conditions  |
| `in`, `not in`          | membership                 |

---

## 🔁 Loops & Iteration

### `for` loop — repeat over a collection
```python
for prime in primes:        # preferred: iterate items directly
    print(prime)

for i in range(5):          # 0,1,2,3,4
    print(i)

for i, val in enumerate(primes):   # index + value together
    print(i, val)
```

### `while` loop — repeat until a condition is false
```python
n = 0
while n < 5:
    print(n)
    n += 1
```

### List comprehensions — build a list in one line
```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(10) if x % 2 == 0]
```

> Pro Tip: Prefer iterating a collection directly (`for item in items`) over `for i in range(len(items))`. It's cleaner and less error-prone.

---

## 🧩 Functions

Reusable blocks of logic. Define with `def`, return a value with `return`.

```python
def greet(name, greeting="Hello"):   # greeting has a default value
    return f"{greeting}, {name}!"

greet("Alice")                 # 'Hello, Alice!'
greet("Bob", greeting="Hi")    # 'Hi, Bob!' → keyword argument
```

- **Parameters** are the names in the definition; **arguments** are the values you pass in.
- **Positional** arguments are matched by order; **keyword** arguments by name.
- A function with no explicit `return` returns `None`.

```python
add = lambda a, b: a + b       # a small anonymous (lambda) function
add(2, 3)                      # 5
```

> Note: A **method** is just a function that belongs to an object, called with dot syntax: `my_list.append(4)`.

---

## 🏗️ Object-Oriented Programming

A **class** is a blueprint; an **object** (instance) is a thing built from it. Classes bundle **data (attributes)** with **behavior (methods)**.

```python
class Dog:
    def __init__(self, name, age):   # constructor: runs when created
        self.name = name             # attribute
        self.age = age

    def bark(self):                  # method
        return f"{self.name} says woof!"

rex = Dog("Rex", 3)      # create an instance
rex.name                 # 'Rex'
rex.bark()               # 'Rex says woof!'
```

- `self` refers to the specific instance the method is acting on.
- `__init__` is the **constructor**, called automatically when you create the object.

> Pro Tip: You use OOP constantly without realizing it — every `df.head()` or `array.reshape()` is a method call on an object.

---

## 🧠 Common Commands

| Command                 | What it does                              |
|-------------------------|-------------------------------------------|
| `print(x)`              | Display a value                           |
| `type(x)`               | Show an object's type                     |
| `len(x)`                | Count items in a collection               |
| `help(x)`               | Show docs and available methods           |
| `range(n)`              | Generate `0 … n-1`                        |
| `enumerate(seq)`        | Loop with index + value                   |
| `x.append(v)`           | Add an item to a list                     |
| `d.keys()` / `.values()`| Dict keys / values                        |
| `d.items()`             | Dict key-value pairs                      |

---

## 📚 Glossary

| Term          | Definition                                              | When it matters                         |
|---------------|---------------------------------------------------------|-----------------------------------------|
| Object        | A typed box in memory holding a value                   | Everything in Python is one             |
| Mutable       | Can be changed in place after creation                  | list, dict, set                         |
| Immutable     | Cannot be changed after creation                        | int, str, tuple                         |
| Zero-indexed  | Counting starts at 0                                     | All indexing and slicing                |
| Method        | A function attached to an object                        | `list.append()`, `df.head()`            |
| Comprehension | Concise one-line way to build a list/dict/set           | Transforming collections                |
| Class         | Blueprint for creating objects                          | Structuring reusable code               |
| Instance      | A concrete object built from a class                    | `rex = Dog(...)`                        |

---

🧠 **Pro Tips:**
* When stuck, reach for `type()` and `help()` before searching the web.
* Choose the right container: **list** (ordered, editable), **tuple** (fixed), **set** (unique), **dict** (labeled lookup).
* Write small functions that do one thing — they're easier to test and reuse.

🔗 Helpful Links:
* https://docs.python.org/3/tutorial/
* https://realpython.com/python-first-steps/
* https://docs.python.org/3/library/stdtypes.html
