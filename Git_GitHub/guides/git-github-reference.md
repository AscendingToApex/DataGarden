# 🧠 Git & GitHub Reference Guide

## 📚 Table of Contents

* [🛠 Initial Setup on Windows](#-initial-setup-on-windows)
* [🔧 Git & GitHub Configuration](#-git--github-configuration)
* [📁 Creating Repositories](#-creating-repositories)
* [🔁 Standard Git Workflow](#-standard-git-workflow)
* [🚀 Working with Remotes](#-working-with-remotes)
* [🛑 Ignoring Files with .gitignore](#-ignoring-files-with-gitignore)
* [🧪 Branching, Merging, and Collaboration](#-branching-merging-and-collaboration)
* [🧯 Troubleshooting & Undoing Mistakes](#-troubleshooting--undoing-mistakes)
* [🔍 Exploring History & Comparing Changes](#-exploring-history--comparing-changes)
* [📓 Git Log Filtering & Insights](#-git-log-filtering--insights)
* [🧠 Common Git Commands](#-common-git-commands)
* [📚 Glossary](#-glossary)

---

## 🛠 Initial Setup on Windows

1. Open **Git Bash**
2. Run `git --version` to verify installation
3. Configure prompt:

   * Use `cd` to move to home directory
   * Run `start .` to open File Explorer
   * Move `bash_profile` and `terminal-config` to home directory
   * Use Git Bash to rename:

     ```bash
     mv terminal-config .terminal-config
     mv bash_profile .bash_profile
     ```
   * Restart Git Bash for changes to take effect
   * Optional: Right-click Git Bash → Options → Background to customize appearance

---

## 🔧 Git & GitHub Configuration

### For Personal Computers

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### For Shared Computers (repo-specific)

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

### On GitHub.com

* Profile → Settings → Emails
* Set a primary email and check "Keep my email addresses private"

### Change Default Editor

```bash
git config --global core.editor "code --wait" # VS Code example
```

More editors: [GitHub docs](https://help.github.com/en/github/using-git/associating-text-editors-with-git)

---

## 📁 Creating Repositories

### Local

```bash
mkdir project-name
cd project-name
git init
```

* Use `ls -a` or `dir /a` to verify hidden `.git` folder
* Create initial file: `touch README.md`

### GitHub

1. Go to [github.com](https://github.com)
2. Create new repository
3. Do **not** initialize with README if one exists locally

### Link Local to Remote

```bash
git remote add origin https://github.com/yourname/repo.git
git push -u origin main
```

---

## 🔁 Standard Git Workflow

```bash
git status           # Check changes
git add .            # Stage all changes
git commit -m "Message"  # Save snapshot
git push origin main # Push to GitHub
git pull origin main # Sync changes
```

---

## 🚀 Working with Remotes

### Push Existing Repo

```bash
git remote add origin <url>
git push -u origin main
```

### Pull Existing Repo

```bash
git remote add origin <url>
git fetch
git pull origin main
```

### Clone Repo

```bash
git clone <url> [new-folder-name]
```

### Change Remote

```bash
git remote set-url origin <new-url>
```

### Rename Original Remote for Forking

```bash
git remote rename origin upstream
git remote add origin <your-fork-url>
```

---

## 🛑 Ignoring Files with .gitignore

* GitHub allows adding templates during repo creation
* Customize manually:

```bash
# Ignore all .log files
*.log

# Ignore node_modules
node_modules/
```

* GitHub’s templates: [github.com/github/gitignore](https://github.com/github/gitignore)

---

## 🧪 Branching, Merging, and Collaboration

### Create & Switch Branch

```bash
git checkout -b feature-branch
```

### Push Branch

```bash
git push origin feature-branch
```

### Merge Branches

```bash
git checkout main
git merge feature-branch
git push
```

### Delete Branch

```bash
git branch -d feature-branch
```

### Visualize Branches

```bash
git log --graph --oneline --all
```

### Forking Workflow

* Fork on GitHub
* Clone locally
* Add upstream remote:

```bash
git remote add upstream <original-repo-url>
```

---

## 🧯 Troubleshooting & Undoing Mistakes

### Undo Last Commit Message

```bash
git commit --amend
```

### Unstage File

```bash
git reset HEAD <file>
```

### Discard Local Changes

```bash
git checkout <file>
```

### Reset to Previous Commit

```bash
git log
# Copy hash

git checkout <hash> <file>
```

---

## 🔍 Exploring History & Comparing Changes

```bash
git log --oneline

# Filter commits
git log --author="Name"
git log --since=1.week

# Compare changes
git diff <file>
git diff --staged

git show HEAD~1
```

### Check Remote Status

```bash
git fetch
git status
```

---

## 📓 Git Log Filtering & Insights

```bash
git shortlog

# Commits by author since 30 days
git log --author="Alice" --since=30.days

# Search commit messages
git log --grep="bug fix"
```

---

## 🧠 Common Git Commands

| Command        | Description       |
| -------------- | ----------------- |
| `git init`     | Start local repo  |
| `git clone`    | Copy from GitHub  |
| `git add`      | Stage changes     |
| `git commit`   | Save snapshot     |
| `git status`   | Check file state  |
| `git diff`     | Show differences  |
| `git push`     | Send to GitHub    |
| `git pull`     | Get updates       |
| `git branch`   | List branches     |
| `git checkout` | Switch branch     |
| `git merge`    | Combine branches  |
| `git log`      | History           |
| `git reset`    | Undo staging      |
| `git stash`    | Save temp changes |

---

## 📚 Glossary

| Term     | What It Means             | When to Use            |
| -------- | ------------------------- | ---------------------- |
| Repo     | A project folder with Git | Always                 |
| Commit   | A saved snapshot          | After staging changes  |
| Staging  | Preparing for commit      | Before `git commit`    |
| Push     | Upload to GitHub          | Sync local with remote |
| Pull     | Download & merge          | Update local repo      |
| Branch   | Parallel line of code     | Features, fixes        |
| Merge    | Combine changes           | Feature complete       |
| Clone    | Copy from GitHub          | Start a project        |
| Fork     | Copy with history         | Contribute to others   |
| HEAD     | Current commit pointer    | Git navigation         |
| Upstream | Original remote repo      | Forking workflows      |

---

🧠 **Pro Tips:**

* Commit often, use clear messages
* Use branches for all new features
* Always pull before pushing
* Use `.gitignore` early
* Name branches descriptively: `feature/`, `bugfix/`, `hotfix/`

📎 Save this file as `README.md` in your repo for quick daily access!

---

🔗 Helpful Links:

* [Git Cheat Sheet PDF](https://education.github.com/git-cheat-sheet-education.pdf)
* [GitHub Docs](https://docs.github.com/en)
