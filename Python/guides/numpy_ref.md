# 🔢 NumPy Reference Guide

> 🟢 **Level:** Beginner  ·  **Prerequisites:** [Python Language Basics](python_language_basics_ref.md)

**NumPy** ("Numerical Python") is the foundation of scientific computing in Python — nearly every data scientist uses it, and libraries like Pandas are built on top of it. This guide covers **arrays**, how to **create** them, **indexing & slicing**, fast **vectorized math (ufuncs)**, and **sorting**.

> Why not just use lists? A NumPy **array** stores one data type in a compact block of memory, so operations run far faster than looping over a Python list.

## 📚 Table of Contents

* [🚀 Getting Started](#-getting-started)
* [🆚 Arrays vs. Lists](#-arrays-vs-lists)
* [🏗️ Creating Arrays](#-creating-arrays)
* [🧊 Array Attributes](#-array-attributes)
* [🎲 Random Numbers & Seeds](#-random-numbers--seeds)
* [🎯 Indexing Arrays](#-indexing-arrays)
* [✂️ Slicing Arrays](#-slicing-arrays)
* [🎨 Fancy Indexing](#-fancy-indexing)
* [⚡ Universal Functions (ufuncs)](#-universal-functions-ufuncs)
* [📊 Aggregations](#-aggregations)
* [🔃 Sorting Arrays](#-sorting-arrays)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🚀 Getting Started

Install once, then import with the universal alias `np`:

```bash
pip install numpy
```
```python
import numpy as np
np.__version__
```

> Pro Tip: Import NumPy **once per session** (at the top), not in every cell.

---

## 🆚 Arrays vs. Lists

- A Python **list** can be *heterogeneous* (mixed types) and stores extra info about each element — flexible but slow for math.
- A NumPy **array** holds a **single data type**, so it skips the per-element type checking and runs much faster.
- If you build an array from mixed types, NumPy **upcasts** to the most flexible type (e.g. ints + floats → all floats; add a string → generic objects).

```python
np.array([1, 4, 2, 5, 3])        # int array
np.array([4.1, 3, 6])            # upcast to float
np.array(["a", 1, 3.2])          # upcast to generic object
np.array([1, 2, 3, 4], dtype='float')   # force a type
```

> Note: You lose no *values* going from list → array, only (possibly) the distinct data types.

---

## 🏗️ Creating Arrays

| Function                              | Creates                                         |
|---------------------------------------|-------------------------------------------------|
| `np.zeros(shape, dtype)`              | Array filled with 0                             |
| `np.ones(shape, dtype)`               | Array filled with 1                             |
| `np.full(shape, value)`               | Array filled with a chosen value                |
| `np.arange(start, stop, step)`        | Evenly spaced values (stop-exclusive)           |
| `np.linspace(start, stop, num)`       | `num` evenly spaced values (stop-inclusive)     |
| `np.eye(n)`                           | Identity matrix (1s on the diagonal)            |
| `np.random.randint(max, size)`        | Random integers                                 |

```python
np.zeros(10, dtype=int)          # ten zeros
np.ones((3, 5), dtype=float)     # 3×5 of ones
np.full((3, 5), 3.14)            # 3×5 of 3.14
np.arange(0, 20, 2)              # 0,2,4,…,18
np.linspace(0, 1, 5)            # 0., 0.25, 0.5, 0.75, 1.
np.eye(3, k=1)                   # 1s one slot above the diagonal
```

---

## 🧊 Array Attributes

A **multidimensional array** is an array of arrays. Inspect its shape with these attributes:

```python
x = np.random.randint(10, size=(3, 4, 5))
x.ndim     # number of dimensions → 3
x.shape    # size of each dimension → (3, 4, 5)
x.size     # total number of elements → 60
x.dtype    # data type of elements
```

---

## 🎲 Random Numbers & Seeds

Random results change every run — unless you **set a seed** for reproducibility.

```python
np.random.random((3, 3))      # different every time
np.random.seed(100)           # fix the seed…
np.random.random((3, 3))      # …now reproducible
```

> Note: `np.random.seed()` only affects the **cell/run** it's in — set it again if you need repeatability later.

---

## 🎯 Indexing Arrays

Arrays are **zero-indexed**, like lists. Add a comma per dimension:

```python
x1 = np.random.randint(10, size=6)        # 1D
x1[0]        # first
x1[-1]       # last

x2 = np.random.randint(10, size=(3, 4))   # 2D → [row, col]
x2[0, 1]     # row 0, column 1

x3 = np.random.randint(10, size=(3, 4, 5))# 3D → [depth, row, col]
x3[1, 1, 2]
```

---

## ✂️ Slicing Arrays

Syntax: `array[start:stop:step]`. Defaults: `start=0`, `stop=end`, `step=1`. **Stop is exclusive.**

```python
x = np.arange(10)
x[:5]        # first five
x[5:]        # from index 5 on
x[4:7]       # 4,5,6
x[::2]       # every other element
x[1::2]      # every other, starting at 1
```

For **multiple dimensions**, separate slices with a comma:

```python
x2 = np.random.randint(10, size=(3, 4))
x2[:2, :3]   # first 2 rows, first 3 cols
x2[1:2, :]   # just row 1, all cols
x2[:, 0]     # every row, column 0
```

---

## 🎨 Fancy Indexing

Pass a **list or array of indices** in the brackets to pull elements in any order or shape:

```python
x = np.random.randint(100, size=10)
ind = [3, 7, 4]
x[ind]                       # → the elements at positions 3, 7, 4

ind = np.array([[3, 7], [4, 5]])
x[ind]                       # result takes the SHAPE of the index array
```

> Pro Tip: Fancy indexing is perfect for reordering data or selecting a specific set of rows/columns at once.

---

## ⚡ Universal Functions (ufuncs)

Python is an **interpreted** language, so element-by-element loops are slow — for each element it must check the type and look up the right operation. **ufuncs** apply one **vectorized** operation to the whole array at compiled speed.

```python
values = np.random.randint(1, 10, size=5)

# Slow: explicit Python loop
def reciprocals(values):
    out = np.empty(len(values))
    for i in range(len(values)):
        out[i] = 1.0 / values[i]
    return out

# Fast: vectorized ufunc — same result, dramatically faster
1.0 / values
```

Common ufuncs: `+ - * / **`, `np.sqrt`, `np.exp`, `np.log`, `np.sin`, `np.abs`.

> Note: **Interpreted** ≈ translated one line at a time; **compiled** ≈ translated all at once ahead of time (faster). ufuncs push work down to compiled code.

---

## 📊 Aggregations

Summarize an array — optionally along one `axis`:

```python
a = np.random.randint(10, size=(3, 4))
a.sum()          # total of all elements
a.min(), a.max() # extremes
a.mean()         # average
a.sum(axis=0)    # sum down each column
a.sum(axis=1)    # sum across each row
```

> Pro Tip: `axis=0` collapses **rows** (works down columns); `axis=1` collapses **columns** (works across rows).

---

## 🔃 Sorting Arrays

```python
x = np.array([3, 1, 2])
np.sort(x)        # returns a sorted copy → [1, 2, 3]
x.sort()          # sorts in place
np.argsort(x)     # indices that would sort the array
```

For 2D arrays, sort along an axis: `np.sort(a, axis=0)` (each column) or `axis=1` (each row).

---

## 🧠 Common Commands

| Command                    | What it does                        |
|----------------------------|-------------------------------------|
| `np.array(list)`           | Build an array from a list          |
| `np.arange(a, b, step)`    | Range of values                     |
| `np.zeros/ones/full`       | Pre-filled arrays                   |
| `arr.reshape(r, c)`        | Change dimensions                   |
| `arr.ndim/.shape/.size`    | Inspect structure                   |
| `np.random.seed(n)`        | Make randomness reproducible        |
| `np.sort(arr)`             | Sorted copy                         |
| `arr.sum(axis=…)`          | Aggregate along an axis             |

---

## 📚 Glossary

| Term          | Definition                                                  | When it matters                   |
|---------------|------------------------------------------------------------|-----------------------------------|
| Array (ndarray) | Compact, single-type, N-dimensional grid of values       | Core NumPy object                 |
| dtype         | The data type of an array's elements                       | Memory + upcasting behavior       |
| Upcasting     | Promoting mixed values to the most flexible common type    | Building arrays from mixed data   |
| ufunc         | Vectorized function applied element-wise at compiled speed | Fast math on whole arrays         |
| Axis          | A dimension to operate along (0 = rows, 1 = columns)       | Aggregations, sorting             |
| Fancy indexing| Indexing with an array/list of positions                   | Reordering, bulk selection        |
| Seed          | Fixed starting point for the random generator              | Reproducible results              |

---

🧠 **Pro Tips:**
* Reach for **vectorized operations** instead of Python loops — they're faster and shorter.
* Set a **random seed** whenever you need reproducible experiments.
* Watch your **axis**: many bugs come from summing/sorting along the wrong one.

🔗 Helpful Links:
* https://numpy.org/doc/stable/
* https://numpy.org/doc/stable/user/absolute_beginners.html
* https://numpy.org/doc/stable/reference/routines.array-creation.html
