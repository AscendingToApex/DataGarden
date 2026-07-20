# 💻 Notebooks & IDEs Reference Guide

Where you *write and run* your code matters. This beginner-friendly guide compares the main environments for Python data work — **Jupyter Notebook**, **Google Colab**, and the **Python / IPython terminal** — and covers the notebook basics (cells, modes, shortcuts, magic commands) that trip up newcomers.

> A **notebook** interleaves code, output, and narrative text — ideal for exploration and sharing. The **terminal/script** approach is better for automation and production.

## 📚 Table of Contents

* [🗺️ Choosing an Environment](#-choosing-an-environment)
* [📓 Jupyter Notebook](#-jupyter-notebook)
* [⌨️ Notebook Modes & Shortcuts](#-notebook-modes--shortcuts)
* [✨ Magic Commands](#-magic-commands)
* [☁️ Google Colab](#-google-colab)
* [🖥️ Python & IPython in the Terminal](#-python--ipython-in-the-terminal)
* [📄 Running a .py Script](#-running-a-py-script)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🗺️ Choosing an Environment

| Environment | Runs where | Best for |
|-------------|------------|----------|
| **Jupyter Notebook** | Locally in a browser | Exploration, teaching, mixing code + notes |
| **Google Colab** | In the cloud (browser) | Zero-install, sharing, free GPUs |
| **IPython** | Terminal | Quick interactive experiments |
| **Python + script** | Terminal | Automation, reusable/production code |

---

## 📓 Jupyter Notebook

A notebook is a document made of **cells**:

- **Markdown cells** — display formatted text (notes, headings, math).
- **Code cells** — run code and show the output right below.

```python
# a code cell
import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3]})
df.head()
```

---

## ⌨️ Notebook Modes & Shortcuts

Jupyter has two **modes**:

- **Command mode** — press **`Esc`** (cell border turns **blue**). Change the notebook's *structure* (add/delete/move cells).
- **Edit mode** — press **`Enter`** (cell border turns **green**). Change a cell's *contents*.

Handy shortcuts (in command mode):

| Shortcut | Action |
|----------|--------|
| `Shift + Enter` | Run cell, select the next |
| `Ctrl + Enter`  | Run cell, stay put |
| `A` / `B`       | Insert cell above / below |
| `D D`           | Delete the cell |
| `M` / `Y`       | Convert to Markdown / Code |
| `Z`             | Undo cell deletion |

> Pro Tip: Restart the kernel and **Run All** before sharing a notebook — it confirms your results reproduce top-to-bottom, not just in the order you happened to run cells.

---

## ✨ Magic Commands

IPython/Jupyter "magics" are shortcuts prefixed with `%` (line) or `%%` (whole cell):

```python
%matplotlib inline     # show plots in the notebook
%timeit my_function()  # time how long code takes
%%time                 # time an entire cell
%run script.py         # run an external .py file
%who                   # list defined variables
!pip install pandas    # run a shell command with !
```

---

## ☁️ Google Colab

[colab.research.google.com](https://colab.research.google.com/) — Jupyter notebooks that run in the cloud.

- **Free** and requires **no installation** (runs in the browser; needs internet).
- Save copies to **Google Drive** and **GitHub**.
- **Share and co-edit** like a Google Doc.
- Click **Mount Drive** in the left panel to connect your Google Drive.

> Note: In Colab you re-import your packages each new session, so keep all `import` statements in one cell at the top.

---

## 🖥️ Python & IPython in the Terminal

**IPython** (an enhanced interactive Python, built on top of Python):

```bash
ipython          # start it
# ...write Python directly, with syntax coloring & tab-completion
quit             # exit
```
- Auto-completes and color-codes ("syntax coloring") as you type.
- Can execute **shell commands** directly.
- Awkward for editing multi-line code after the fact.

**Plain Python** shell:

```bash
python           # start the basic interpreter
```
- Similar, but you must press **Tab** for completion (IPython does more automatically).

---

## 📄 Running a .py Script

For reusable code, save it in a **`.py`** file and run it from the terminal:

```bash
cd path/to/project
python filename.py
```

> Pro Tip: Prototype in a notebook, then move stable, reusable logic into `.py` files you can import and automate.

---

## 🧠 Common Commands

| Command | What it does |
|---------|--------------|
| `jupyter notebook` | Launch Jupyter locally |
| `Esc` / `Enter` | Command / edit mode |
| `Shift + Enter` | Run a cell |
| `%timeit` / `%%time` | Benchmark code |
| `%run file.py` | Run a script in the notebook |
| `!command` | Run a shell command |
| `ipython` / `python` | Start interactive shells |
| `python file.py` | Run a script from the terminal |

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| Cell | A block of code or markdown in a notebook | Notebook structure |
| Kernel | The process that runs your notebook's code | Restart to clear state |
| Command/Edit mode | Structure vs. content editing | Notebook navigation |
| Magic command | `%`/`%%` IPython shortcut | Timing, plotting, shell access |
| IPython | Enhanced interactive Python shell | Quick terminal experiments |

---

🧠 **Pro Tips:**
* **Restart & Run All** before trusting or sharing a notebook's results.
* Use **Colab** when you want zero setup or a free GPU; use local Jupyter for offline work.
* Graduate reusable code from notebooks into **`.py` files** for automation.

🔗 Helpful Links:
* https://jupyter.org/
* https://colab.research.google.com/
* https://ipython.readthedocs.io/
