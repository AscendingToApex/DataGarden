# 🌱 Contributing to DataGarden

Thanks for helping the garden grow! DataGarden is a collection of **beginner-friendly reference guides** for data analysts and aspiring data scientists. Consistency is what makes it usable — please follow the conventions below.

## 🗂️ Repository Structure

Every topic is a top-level folder organized the same way:

```
Topic_Name/
├── README.md          # landing page: lists guides, reading order, cheat sheets, related topics
├── guides/            # the reference guides (*_ref.md)
├── cheat-sheets/      # quick-reference PDFs
└── templates/         # reusable starter files
```

## 🏷️ Naming Conventions

- **Topic folders:** `Snake_Case`, capitalized (e.g., `Machine_Learning`, `Data_Wrangling`). Proper names may stay short (`SQL`, `R`).
- **Guides:** lowercase `snake_case` ending in `_ref.md` (e.g., `pandas_ref.md`, `hypothesis_testing_ref.md`).
- **Cheat sheets:** keep the descriptive source filename.

## 📄 Guide Format

Each guide should follow this shape (see any existing guide as a model):

1. **`# 🔖 Title Reference Guide`** — H1 with a leading emoji.
2. **Metadata line** directly under the title:
   ```
   > 🟢 **Level:** Beginner  ·  **Prerequisites:** link to a prior guide, or "none"
   ```
   Levels: **🟢 Beginner · 🟡 Intermediate · 🔴 Advanced**.
3. **Intro paragraph** — one short paragraph on what the guide covers, plus an opening `>` orientation note.
4. **`## 📚 Table of Contents`** — bulleted links to every section (emoji-anchor style: `[🚀 Getting Started](#-getting-started)`).
5. **Sections** separated by `---`, each with worked examples in fenced code blocks and `> Note:` / `> Pro Tip:` callouts.
6. **`## 🧠 Common Commands`** and/or **`## 📚 Glossary`** tables where useful.
7. **Footer:** a `🧠 **Pro Tips:**` recap and a `🔗 Helpful Links:` list of authoritative external docs.

### Style
- Write for a beginner: define jargon, show runnable examples, prefer clarity over completeness.
- Use tables for comparisons and command references.
- Keep every table-of-contents anchor in sync with its heading (test links before submitting).
- No personal data, credentials, API keys, or real internal endpoints — use placeholders (`host='...'`).

## ➕ Adding a Guide

1. Create `Topic/guides/your_topic_ref.md` following the format above.
2. Add it to that topic's `README.md` (guides table + reading order).
3. If it's a new topic, create the folder structure, a topic `README.md`, and add the topic to the root [README.md](README.md) index.

## 🔀 Workflow

- Branch off `Production`, make your changes, and open a pull request into `Production`.
- Use a descriptive branch name (e.g., `add-excel-guide`, `fix-anchor-links`).
- Keep PRs focused on one topic or one kind of change where possible.

Happy gardening! 🌱
