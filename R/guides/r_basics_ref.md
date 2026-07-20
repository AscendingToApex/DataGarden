# 📊 R Basics Reference Guide

> 🟢 **Level:** Beginner  ·  **Prerequisites:** none

**R** is a language built for statistics and data analysis, most often used through **RStudio**. This beginner-friendly guide covers the essentials: **variables and vectors**, **operators**, **packages**, **loading/saving data**, **special values**, **factors**, **data frames**, **lists**, and **formulas**.

> Coming from Python? Two things to rewire immediately: R uses **`<-`** for assignment and **indexes from 1**, not 0.

## 📚 Table of Contents

* [➕ Arithmetic & Variables](#-arithmetic--variables)
* [🧰 Built-in Functions](#-built-in-functions)
* [🔗 Vectors](#-vectors)
* [🔣 Comparison & Logical Operators](#-comparison--logical-operators)
* [🎯 Logical Indexing](#-logical-indexing)
* [📦 Packages](#-packages)
* [📁 Working Directory & Data I/O](#-working-directory--data-io)
* [❓ Special Values](#-special-values)
* [🏷️ Variable Classes](#-variable-classes)
* [🗂️ Factors](#-factors)
* [🧾 Data Frames](#-data-frames)
* [📋 Lists](#-lists)
* [➗ Formulas](#-formulas)
* [🆘 Getting Help](#-getting-help)
* [📚 Glossary](#-glossary)

---

## ➕ Arithmetic & Variables

Arithmetic works like most languages. Assign with the **assignment operator `<-`** (or `->`):

```r
10 + 2           # 12
Sales <- 350     # assign 350 to Sales
Sales            # 350
```

**Variable name rules:** start with a letter or a period, case-sensitive, may contain `.`, `_`, and letters; can't be reserved words.

---

## 🧰 Built-in Functions

```r
sqrt(x)          # square root
abs(x)           # absolute value
c(x, y, z)       # combine values into a vector
length(vec)      # number of elements
nchar(string)    # number of characters
```

---

## 🔗 Vectors

A **vector** is an ordered collection created with `c()`. **R indexes starting at 1.**

```r
sales.by.month <- c(0, 100, 200, 50, 0, 0, 0, 0, 0)
sales.by.month[1]     # first element (not [0]!)
length(sales.by.month)
```

You can name vector elements:

```r
profit <- c("Q1" = 3.1, "Q2" = 0.1, "Q3" = -1.4, "Q4" = 1.1)
# or
profit <- c(3.1, 0.1, -1.4, 1.1)
names(profit) <- c("Q1", "Q2", "Q3", "Q4")
```

---

## 🔣 Comparison & Logical Operators

| Operation | Operator | Example | Result |
|-----------|----------|---------|--------|
| less than | `<` | `2 < 3` | TRUE |
| less than or equal | `<=` | `2 <= 2` | TRUE |
| greater than | `>` | `2 > 3` | FALSE |
| greater than or equal | `>=` | `2 >= 2` | TRUE |
| equal to | `==` | `2 == 3` | FALSE |
| not equal to | `!=` | `2 != 3` | TRUE |
| not | `!` | `!(1==1)` | FALSE |
| or | `\|` | `(1==1) \| (2==3)` | TRUE |
| and | `&` | `(1==1) & (2==3)` | FALSE |

---

## 🎯 Logical Indexing

Subset a vector by a condition — one of R's most useful patterns:

```r
months <- c("January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December")
sales.by.month <- c(0, 100, 200, 50, 0, 0, 0, 0, 0, 0, 0, 0)

months[sales.by.month > 0]    # "February" "March" "April"
```

---

## 📦 Packages

A package must be **installed** before it's **loaded**, and **loaded** before it's **used**.

```r
install.packages("lsr")              # install once
library("foreign")                   # load (good form: at the top of the script)
detach("package:foreign", unload = TRUE)   # unload
```

> Pro Tip: In RStudio you can install via the **Packages panel → Install** and load by checking the box, but scripting `library(...)` at the top keeps your work reproducible.

---

## 📁 Working Directory & Data I/O

```r
setwd("../data")                       # set the working directory

# R workspace files (.Rdata)
load("booksales.Rdata")                # load
save.image(file = "myfile.Rdata")      # save everything in the workspace
save(file = "subset.Rdata", list = c("data", "handy"))   # save specific variables

# CSV (tidyverse)
library(readr)
books <- read_csv(file = "booksales.csv")   # header = TRUE by default
print(books)
```

> Note: RStudio's **Import Dataset** button (Environment panel) gives a point-and-click alternative for CSVs.

---

## ❓ Special Values

| Value | Meaning |
|-------|---------|
| `Inf` / `-Inf` | Infinity (e.g., a positive number ÷ 0) |
| `NaN` | "Not a Number" — mathematically undefined (e.g., 0/0) |
| `NA` | Missing — a value *should* be here but isn't (real-world data gaps) |
| `NULL` | No value at all — genuinely absent |

> Note: `NaN` means we know it's undefined; `NA` means we don't know the value; `NULL` means there is no value whatsoever.

---

## 🏷️ Variable Classes

R tracks three levels of type information:

- **`class()`** — high-level, meaningful distinction (e.g., recognizing a *date* vs. a plain string). The one you'll use most.
- **`mode()`** — the storage format (text vs. numeric).
- **`typeof()`** — low-level (integer vs. double). Rarely needed.

---

## 🗂️ Factors

**Factors** are R's way to represent a **nominal (categorical)** variable:

```r
group <- c(1, 1, 1, 2, 2, 2, 3, 3, 3)
group <- as.factor(group)
levels(group) <- c("group 1", "group 2", "group 3")
class(group)     # "factor"
```

---

## 🧾 Data Frames

A **data frame** is R's table (rows × columns) — what `read_csv` returns, or build one directly:

```r
df <- data.frame(name = c("Ann", "Ben"), age = c(25, 30))
df$age               # pull a column with $
names(df)            # variable (column) names
```

---

## 📋 Lists

A **list** can hold elements of different types (even other lists):

```r
person <- list(age = 34, nerd = TRUE, parents = c("Joe", "Liz"))
person$nerd                 # look up a value
person$children <- "Alex"   # add an element
print(person)
```

---

## ➗ Formulas

A **formula** (using the tilde `~`) specifies a relationship between variables — the backbone of R's modeling functions:

```r
out ~ pred            # outcome explained by one predictor
out ~ pred1 + pred2   # two predictors
out ~ pred1 * pred2   # predictors plus their interaction
~ var1 + var2         # one-sided formula
```

---

## 🆘 Getting Help

```r
help("mean")            # documentation for a function
help.search("mean")     # fuzzy search across help
?mean                   # shorthand for help()
```

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| `<-` | Assignment operator | Assigning values |
| Vector | Ordered collection from `c()` | The basic R data structure |
| Factor | Categorical (nominal) variable | Grouping, modeling |
| Data frame | Table of rows and columns | The main analysis object |
| List | Mixed-type collection | Flexible grouping |
| Formula | `y ~ x` relationship spec | Statistical models |
| NA / NaN / NULL | Missing / undefined / absent | Handling real-world data |

---

🧠 **Pro Tips:**
* Remember R is **1-indexed** and assigns with **`<-`** — the two most common gotchas.
* Put `library(...)` calls at the **top** of the script for reproducibility.
* Use `class()` to understand a variable before you try to operate on it.

🔗 Helpful Links:
* https://www.r-project.org/
* https://r4ds.hadley.nz/ (R for Data Science)
* https://rstudio.github.io/cheatsheets/
