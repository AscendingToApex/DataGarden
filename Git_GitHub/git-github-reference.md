# 🧠 Git & GitHub Reference Guide

## 📚 Table of Contents
- [📁 1. Creating a Repository](#-1-creating-a-repository)
- [🔁 2. Standard Git Workflow](#-2-standard-git-workflow)
- [🔧 3. Common Git Commands](#-3-common-git-commands)
- [📚 4. Git Glossary](#-4-git-glossary)
- [🚨 5. Common Git Errors & Fixes](#-5-common-git-errors--fixes)
- [⚡ 6. Time-Saving Git Aliases](#-6-time-saving-git-aliases)
- [🧽 7. Sample .gitignore](#-7-sample-gitignore)
- [🧩 8. Visual Branch Workflow](#-8-visual-branch-workflow)

---

## 📁 1. Creating a Repository

### 🟦 On GitHub (Remote)

1. Go to [https://github.com](https://github.com)
2. Click **New Repository**
3. Fill in:
   - **Repository name**
   - (Optional) Description
   - Choose **Public** or **Private**
4. (Optional) Initialize with README, .gitignore, or license
5. Click **Create repository**

### 💻 On Local Machine

**Option A: Clone Existing GitHub Repo**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

**Option B: Start a New Repo Locally**
```bash
mkdir your-repo
cd your-repo
git init
```

To connect to GitHub:
```bash
git remote add origin https://github.com/your-username/your-repo.git
```

---

## 🔁 2. Standard Git Workflow

1. **Create or Modify Files**
2. **Check Status**
   ```bash
   git status
   ```
3. **Stage Changes**
   ```bash
   git add .
   ```
4. **Commit Changes**
   ```bash
   git commit -m "Your message"
   ```
5. **Push to GitHub**
   ```bash
   git push origin main
   ```
6. **Pull Updates from GitHub**
   ```bash
   git pull origin main
   ```

---

## 🔧 3. Common Git Commands

| Command | Description |
|--------|-------------|
| `git init` | Initialize a Git repo |
| `git clone <url>` | Copy a remote repo |
| `git status` | See modified/staged files |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save a snapshot |
| `git push origin main` | Upload changes to GitHub |
| `git pull origin main` | Get latest changes |
| `git branch` | Show local branches |
| `git checkout -b <name>` | Create and switch branch |
| `git checkout <name>` | Switch branches |
| `git merge <name>` | Merge into current branch |
| `git log` | Show commit history |
| `git remote -v` | Show remotes |
| `git reset` | Undo local changes |
| `git stash` | Temporarily save changes |

---

## 📚 4. Git Glossary

| Term | Description | When to Use |
|------|-------------|-------------|
| **Repository (repo)** | Git-tracked project folder | Always |
| **Commit** | Saved code snapshot | Every change |
| **Stage (add)** | Prepare file for commit | Before committing |
| **Push** | Send commits to GitHub | Sync with remote |
| **Pull** | Fetch + merge from GitHub | Stay updated |
| **Branch** | Independent code path | Feature or fix |
| **Merge** | Combine branches | Finalize feature |
| **Clone** | Copy repo from GitHub | Start new local copy |
| **Checkout** | Switch code state or branch | Task switching |
| **Stash** | Save WIP changes | Mid-task switch |
| **Origin** | Default remote name | Used in push/pull |
| **HEAD** | Current repo position | Used in reset/checkout |

---

## 🚨 5. Common Git Errors & Fixes

### 🔴 Error: *"fatal: not a git repository"*
**Fix:** Navigate into a Git repo or run `git init`

---

### 🔴 Error: *Merge conflict*
**Fix:**
1. Open file and resolve the `<<<<<<<` conflict markers
2. Run `git add .`
3. Run `git commit -m "Resolve conflict"`

---

### 🔴 Error: *Accidentally committed to the wrong branch*
**Fix:**
```bash
git checkout correct-branch
git cherry-pick <commit-hash>
git checkout wrong-branch
git reset --hard HEAD~1
```

---

### 🔴 Error: *Forgot to add a file to last commit*
**Fix:**
```bash
git add missed-file
git commit --amend
```

---

## ⚡ 6. Time-Saving Git Aliases

Add these to save typing:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm "commit -m"
git config --global alias.last "log -1 HEAD"
```

Now use:
```bash
git st
git co main
git cm "initial commit"
```

---

## 🧽 7. Sample .gitignore

```gitignore
# Node.js
node_modules/
.env

# Python
__pycache__/
*.pyc
.env

# macOS
.DS_Store

# VS Code
.vscode/
```

---

## 🧩 8. Visual Branch Workflow

```
main ──●──●──●──────────────▶ deployed
          \
feature-x ─●──●──●─┐
                    \
                     └─▶ Merge to main
```

---

🧠 **Pro Tips**
- Pull before pushing to avoid conflicts.
- Use feature branches for isolated work.
- Write clear commit messages.
- Keep your main branch clean and deployable.
