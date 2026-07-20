# 📥 Data Collection & Ingestion Reference Guide

> 🟢 **Level:** Beginner  ·  **Prerequisites:** [Pandas](../../Python/guides/pandas_ref.md)

Before you can analyze anything, you have to **get the data in**. This guide is a practical map of how to load data into a Pandas DataFrame from **flat files**, **spreadsheets**, **statistical formats**, **databases**, the **cloud**, the **web**, and **APIs**.

> The goal of every method below is the same: end up with a clean **DataFrame** you can work with.

## 📚 Table of Contents

* [🚀 Getting Started](#-getting-started)
* [🗂️ Context Managers (Safe File Handling)](#-context-managers-safe-file-handling)
* [📄 Flat Files (.txt / .csv)](#-flat-files-txt--csv)
* [📊 Excel](#-excel)
* [📈 Statistical Formats (SAS / Stata / HDF5 / MATLAB)](#-statistical-formats-sas--stata--hdf5--matlab)
* [🗄️ Databases (SQL)](#-databases-sql)
* [☁️ Cloud Sources (Redshift, S3, Dropbox)](#-cloud-sources-redshift-s3-dropbox)
* [🌐 HTML Tables](#-html-tables)
* [🕸️ Web Scraping](#-web-scraping)
* [🔌 APIs & JSON](#-apis--json)
* [🔍 Extracting with Regex](#-extracting-with-regex)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🚀 Getting Started

```python
import pandas as pd
import numpy as np
```

---

## 🗂️ Context Managers (Safe File Handling)

Use a `with` block to open files — it **automatically closes** the file even if an error occurs:

```python
with open('data.txt', 'r') as f:
    contents = f.read()
# file is closed here, automatically
```

> Pro Tip: Always prefer `with open(...)` over a bare `open(...)`. Forgetting to `close()` a file leaks resources.

---

## 📄 Flat Files (.txt / .csv)

The everyday workhorse:

```python
df = pd.read_csv('data.csv')                  # comma-separated
df = pd.read_csv('data.tsv', sep='\t')        # tab-separated
df = pd.read_csv('data.csv', usecols=['a','b'], nrows=1000)
df.to_csv('out.csv', index=False)             # write back out
```

---

## 📊 Excel

```python
df = pd.read_excel('book.xlsx', sheet_name='Sheet1')
# read every sheet into a dict of DataFrames:
sheets = pd.read_excel('book.xlsx', sheet_name=None)
df.to_excel('out.xlsx', index=False)
```

---

## 📈 Statistical Formats (SAS / Stata / HDF5 / MATLAB)

```python
df = pd.read_sas('data.sas7bdat')     # SAS
df = pd.read_stata('data.dta')        # Stata
df = pd.read_hdf('data.h5', 'key')    # HDF5 (large scientific data)

from scipy.io import loadmat           # MATLAB .mat files
mat = loadmat('data.mat')
```

---

## 🗄️ Databases (SQL)

Connect, run a query, and pull the result straight into a DataFrame.

```python
# MySQL
import pymysql
conn = pymysql.connect(host='...', user='...', password='...', db='...')
df = pd.read_sql('SELECT * FROM customers', conn)

# PostgreSQL
import psycopg2
conn = psycopg2.connect(host='...', dbname='...', user='...', password='...')
df = pd.read_sql('SELECT * FROM orders LIMIT 100', conn)
```

> Note: `pd.read_sql` takes any valid SQL string — filter and aggregate *in the database* to pull less data over the wire.

---

## ☁️ Cloud Sources (Redshift, S3, Dropbox)

```python
# Amazon Redshift — behaves like PostgreSQL
import psycopg2
conn = psycopg2.connect(host='cluster...redshift.amazonaws.com', dbname='...',
                        user='...', password='...', port=5439)
df = pd.read_sql('SELECT * FROM sales', conn)

# Amazon S3 — often loaded into a dict of DataFrames keyed by filename
import boto3
# ... load each CSV in the bucket into dfs['filename']

# Dropbox — connect with an access token, then read files into DataFrames
import dropbox
dbx = dropbox.Dropbox('ACCESS_TOKEN')
```

> Note: Keep credentials and access tokens **out of your code** — load them from environment variables or a secrets manager, never hard-code them.

---

## 🌐 HTML Tables

`read_html` scrapes every `<table>` on a page into a list of DataFrames:

```python
tables = pd.read_html('https://en.wikipedia.org/wiki/Some_Page')
df = tables[0]         # pick the table you want by index
```

---

## 🕸️ Web Scraping

When data isn't in a neat table, scrape the HTML with **requests + BeautifulSoup**:

```python
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://example.com')
soup = BeautifulSoup(resp.text, 'html.parser')
titles = [h2.get_text() for h2 in soup.find_all('h2')]
```

> Note: Respect each site's **robots.txt** and terms of service, and don't hammer servers with rapid requests.

---

## 🔌 APIs & JSON

Many services return **JSON** (JavaScript Object Notation) — nested key/value data that maps neatly to Python dicts.

```python
import requests
resp = requests.get('https://api.example.com/data', params={'q': 'python'})
data = resp.json()               # parse JSON into a dict/list
df = pd.json_normalize(data['results'])   # flatten nested JSON into a table
```

---

## 🔍 Extracting with Regex

Pull structured tokens (emails, phone numbers, hashtags) out of raw text:

```python
import re
emails   = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
hashtags = re.findall(r'#\w+', tweet)
mentions = re.findall(r'@\w+', tweet)
```

---

## 🧠 Common Commands

| Command                        | Loads from…                    |
|--------------------------------|--------------------------------|
| `pd.read_csv(path)`            | CSV / text file                |
| `pd.read_excel(path)`          | Excel workbook                 |
| `pd.read_sql(query, conn)`     | A SQL database                 |
| `pd.read_html(url)`            | HTML tables on a page          |
| `pd.read_json(path)`           | A JSON file                    |
| `requests.get(url).json()`     | A REST API                     |
| `pd.read_sas` / `read_stata`   | SAS / Stata files              |

---

## 📚 Glossary

| Term            | Definition                                                | When it matters                |
|-----------------|-----------------------------------------------------------|--------------------------------|
| Flat file       | Plain-text tabular file (CSV/TSV)                          | The most common data source    |
| Context manager | `with` block that auto-manages resources                  | Safe file handling             |
| Connection      | An open session to a database                             | SQL/cloud ingestion            |
| JSON            | Nested key/value data format                              | APIs                           |
| Web scraping    | Extracting data from a web page's HTML                    | No API/table available         |
| Regex           | Pattern language for matching text                        | Extracting tokens from text    |

---

🧠 **Pro Tips:**
* Filter/aggregate **in SQL** before loading — pull only the data you need.
* Never hard-code credentials; use environment variables.
* After loading, immediately run `df.info()` and `df.head()` to sanity-check the import.

🔗 Helpful Links:
* https://pandas.pydata.org/docs/user_guide/io.html
* https://requests.readthedocs.io/
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
