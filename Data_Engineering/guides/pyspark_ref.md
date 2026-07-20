# ⚡ PySpark Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [Pandas](../../Python/guides/pandas_ref.md), [SQL DML](../../SQL/guides/data_manipulation_language_ref.md)

**Apache Spark** is a distributed engine for processing data too big for one machine, and **PySpark** is its Python API. This beginner-friendly guide covers the core ideas — the **SparkSession**, the two data abstractions (**RDDs** and **DataFrames**), common **transformations vs. actions**, and **Spark SQL**.

> When to reach for Spark: your data no longer fits comfortably in Pandas/memory, or you need to run the same computation across a cluster. For small data, plain Pandas is simpler and faster.

## 📚 Table of Contents

* [🚀 Getting Started](#-getting-started)
* [🧠 Core Concepts](#-core-concepts)
* [🪨 RDDs](#-rdds)
* [🔀 Transformations vs. Actions](#-transformations-vs-actions)
* [🗃️ DataFrames](#-dataframes)
* [🔍 Common DataFrame Operations](#-common-dataframe-operations)
* [🗄️ Spark SQL](#-spark-sql)
* [🐼 PySpark vs. Pandas](#-pyspark-vs-pandas)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🚀 Getting Started

```bash
pip install pyspark
```

Every PySpark program starts with a **SparkSession** — the entry point to Spark:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

sc = spark.sparkContext    # lower-level entry point (for RDDs)
```

---

## 🧠 Core Concepts

- **Distributed computing** — Spark splits data into **partitions** spread across a cluster and processes them in parallel.
- **Lazy evaluation** — transformations aren't executed until an **action** is called, letting Spark optimize the whole plan.
- **Immutability** — RDDs/DataFrames aren't modified in place; each operation returns a new one.

---

## 🪨 RDDs

An **RDD** (Resilient Distributed Dataset) is Spark's original low-level abstraction — a fault-tolerant, distributed collection of objects.

```python
rdd = sc.parallelize([1, 2, 3, 4, 5])        # create from a Python list
rdd = sc.textFile("data.txt")                # create from a file

rdd.map(lambda x: x * 2)                      # transform each element
rdd.filter(lambda x: x > 2)                   # keep matching elements
rdd.collect()                                 # action: bring results to the driver
```

> Note: Prefer **DataFrames** over raw RDDs for most work — they're higher-level, easier to read, and Spark can optimize them (via the Catalyst optimizer). Reach for RDDs only when you need fine-grained control.

---

## 🔀 Transformations vs. Actions

This distinction is the heart of Spark:

| | **Transformations** | **Actions** |
|---|---------------------|-------------|
| What | Define a new dataset from an existing one | Trigger computation and return/save a result |
| Evaluation | **Lazy** (queued, not run) | **Eager** (runs the whole plan) |
| Examples | `map`, `filter`, `flatMap`, `groupBy`, `select`, `join` | `collect`, `count`, `take`, `first`, `show`, `save` |

```python
result = rdd.map(lambda x: x * 2).filter(lambda x: x > 4)   # nothing runs yet
result.collect()                                            # NOW Spark executes
```

> Pro Tip: Because transformations are lazy, a long chain costs nothing until an action fires — so avoid sprinkling in unnecessary actions like `count()` while debugging large jobs.

---

## 🗃️ DataFrames

A Spark **DataFrame** is a distributed table with named columns — conceptually like a Pandas DataFrame or SQL table, but spread across a cluster.

```python
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df = spark.read.json("data.json")
df = spark.read.parquet("data.parquet")     # columnar, efficient

df.printSchema()      # column names & types
df.show(5)            # display first 5 rows
df.count()            # number of rows
```

---

## 🔍 Common DataFrame Operations

```python
from pyspark.sql import functions as F

df.select("name", "age")                       # choose columns
df.filter(df["age"] > 30)                      # filter rows (or df.where(...))
df.withColumn("age2", df["age"] * 2)           # add/replace a column
df.groupBy("dept").agg(F.avg("salary"))        # group + aggregate
df.orderBy(F.col("age").desc())                # sort
df.join(other, on="id", how="left")            # join
df.write.parquet("out.parquet")               # save (an action)
```

---

## 🗄️ Spark SQL

Register a DataFrame as a temporary view and query it with plain SQL:

```python
df.createOrReplaceTempView("people")

result = spark.sql("""
    SELECT dept, AVG(salary) AS avg_salary
    FROM people
    WHERE age > 30
    GROUP BY dept
    ORDER BY avg_salary DESC
""")
result.show()
```

> Pro Tip: The DataFrame API and Spark SQL are interchangeable and run through the same optimizer — use whichever is clearer for the task.

---

## 🐼 PySpark vs. Pandas

| | **Pandas** | **PySpark** |
|---|-----------|-------------|
| Scale | Single machine, in-memory | Distributed cluster, big data |
| Evaluation | Eager | Lazy (until an action) |
| Best for | Small/medium data, quick analysis | Data too big for memory, ETL at scale |
| Mutability | Mutable | Immutable |

> Note: Convert a (small enough!) Spark DataFrame to Pandas with `df.toPandas()` — but only when the result fits in the driver's memory, since it pulls everything to one machine.

---

## 🧠 Common Commands

| Command | What it does |
|---------|--------------|
| `SparkSession.builder.getOrCreate()` | Start Spark |
| `spark.read.csv(path, header=True)` | Load a DataFrame |
| `df.show(n)` / `df.printSchema()` | Inspect data |
| `df.select(...)` / `df.filter(...)` | Choose columns / rows |
| `df.groupBy(...).agg(...)` | Aggregate |
| `df.join(other, on=, how=)` | Join DataFrames |
| `df.createOrReplaceTempView(name)` | Enable Spark SQL |
| `spark.sql("...")` | Run a SQL query |
| `df.write.parquet(path)` | Save results |

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| SparkSession | The entry point to Spark | Every PySpark program |
| RDD | Low-level distributed collection | Fine-grained control |
| DataFrame | Distributed named-column table | Most Spark work |
| Transformation | Lazy operation defining a new dataset | Building a plan |
| Action | Eager operation that triggers execution | Getting results |
| Partition | A chunk of data on one node | Parallelism/performance |
| Lazy evaluation | Deferring work until an action | Spark's optimization model |

---

🧠 **Pro Tips:**
* Prefer **DataFrames + Spark SQL** over raw RDDs — clearer and better optimized.
* Remember Spark is **lazy**: nothing runs until an **action** like `show()` or `collect()`.
* Only `toPandas()` / `collect()` data that **fits in memory** — it all lands on one machine.

🔗 Helpful Links:
* https://spark.apache.org/docs/latest/api/python/
* https://spark.apache.org/docs/latest/sql-programming-guide.html
* https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html
