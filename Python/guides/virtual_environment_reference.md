
# **Virtual Environment Guide for VS Code (.py + .ipynb)**

This guide shows how to **create**, **activate**, **use**, and **debug** a Python virtual environment in VS Code — for both **Python scripts** and **Jupyter notebooks**.

---

## 🚀 **Quick Commands (Reference Only)**
- Create venv: `python -m venv .venv`  
- Activate venv:  
  - macOS/Linux: `source .venv/bin/activate`  
  - PowerShell: `.venv\Scripts\Activate.ps1`  
- Freeze packages: `pip freeze > requirements.txt`  
- Install from file: `pip install -r requirements.txt`  

---

# **1. Create a Virtual Environment**
From the project root in VS Code:

```bash
python -m venv .venv
```

**Why `.venv`?**  
- Keeps environments isolated per project  
- Auto‑detected by VS Code  
- Easy to ignore in Git (`.venv/`)

---

# **2. Activate the Virtual Environment**
### macOS/Linux
```bash
source .venv/bin/activate
```

### Windows PowerShell
```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD
```cmd
.venv\Scripts\activate.bat
```

You’ll see `(.venv)` in your terminal prompt.  
Deactivate anytime with:

```bash
deactivate
```

---

# **3. Manage `requirements.txt`**
### Generate from the active venv
```bash
pip freeze > requirements.txt
```

### Install from the file
```bash
pip install -r requirements.txt
```

**Best practices**
- Update `requirements.txt` whenever you add/upgrade packages  
- Never commit `.venv/`  
- Pin versions for reproducibility

---

# **4. Tell VS Code to Use the Virtual Environment**
1. Open Command Palette (`Ctrl/Cmd + Shift + P`)  
2. Run **Python: Select Interpreter**  
3. Choose the interpreter inside `.venv`  

VS Code will now use this environment for:
- IntelliSense  
- Linting  
- Running `.py` files  
- Debugging  
- Jupyter notebooks (after kernel registration)

---

# **5. Running & Debugging `.py` Files**
### Run
- Click **Run Python File in Terminal**, or  
- Use the activated terminal:  
  ```bash
  python your_script.py
  ```

### Debug
- Set breakpoints  
- Press **F5**  
- VS Code uses the selected `.venv` interpreter automatically

---

# **6. Using the Virtual Environment in Jupyter Notebooks**
To use the same venv for `.ipynb` files, you must install and register a Jupyter kernel.

### 6.1 Install `ipykernel` inside the venv
```bash
pip install ipykernel
```

### 6.2 Install project packages
```bash
pip install <package-name>
```

### 6.3 Register the venv as a Jupyter kernel
```bash
python -m ipykernel install --user --name myvenv --display-name "Python (myvenv)"
```

### 6.4 Select the kernel in VS Code
- Open the notebook  
- Click **Select Kernel**  
- Choose **Python (myvenv)**  

### 6.5 Verify the notebook is using the venv
Run:

```python
import sys
sys.executable
```

You should see a path inside `.venv`.

---

# **7. Troubleshooting**
### ❌ Notebook imports fail
- Clear kernel cache:  
  **Command Palette → “Jupyter: Clear Jupyter Kernelspec Cache”**
- List kernels:
  ```bash
  jupyter kernelspec list
  ```
- Remove old ones:
  ```bash
  jupyter kernelspec remove <kernel-name>
  ```

### ❌ VS Code using wrong interpreter
- Re-run **Python: Select Interpreter**  
- Reload VS Code window

### ❌ Packages missing
Reinstall inside the venv:

```bash
pip install <package-name>
```

### ❌ New terminal not using venv
- Activate manually, or  
- Enable VS Code setting:  
  **Python: Terminal: Activate Environment**

---

# **8. Summary Workflow**
### For `.py` files
1. Create venv  
2. Activate venv  
3. Install packages  
4. Select interpreter  
5. Run/debug  

### For `.ipynb` files
1. Create + activate venv  
2. Install `ipykernel`  
3. Register kernel  
4. Select kernel  
5. Verify with `sys.executable`  

---