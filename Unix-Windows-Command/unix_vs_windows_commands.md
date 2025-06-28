# 🖥️ Unix vs Windows Command Reference

This guide provides a comprehensive mapping of common Windows Command Prompt commands to their Unix/Linux shell equivalents, ideal for developers, system admins, and users switching environments.

---

## 📁 File & Directory Commands

| Windows       | Linux/Unix         | Description                             |
|---------------|--------------------|-----------------------------------------|
| `dir`         | `ls -l`            | List directory contents                 |
| `cd`          | `cd`               | Change current directory                |
| `cd ..`       | `cd ..`            | Go up one directory                     |
| `md`          | `mkdir`            | Create new directory                    |
| `rmdir`       | `rm -rf` / `rmdir` | Delete directory                        |
| `ren` / `rename` | `mv`           | Rename a file or folder                 |
| `copy` / `xcopy` | `cp`            | Copy files or directories               |
| `move`        | `mv`               | Move files or directories               |
| `del`         | `rm`               | Delete a file                           |
| `start`       | `open`             | Open a file with default program (Mac)  |
| `cls`         | `clear`            | Clear terminal screen                   |
| `echo`        | `echo`             | Print text to the screen                |
| `type`        | `cat`              | Print file contents                     |
| `attrib`      | `chmod` / `chown`  | Change file permissions/ownership       |
| -             | `file`             | View file type                          |
| -             | `stat`             | View file metadata                      |
| -             | `basename` / `dirname` | Extract filename or path            |

---

## 🔄 Process Management

| Windows       | Linux/Unix   | Description                         |
|---------------|--------------|-------------------------------------|
| `tasklist`    | `ps aux`     | List running processes              |
| `taskkill`    | `kill` / `killall` | Kill a process                 |
| -             | `top` / `htop` | Monitor processes live             |

---

## 📡 Networking Tools

| Windows       | Linux/Unix     | Description                             |
|---------------|----------------|-----------------------------------------|
| `ping`        | `ping`         | Check network connection                |
| `tracert`     | `traceroute`   | Trace network path                      |
| `ipconfig`    | `ifconfig` / `ip a` | View network configuration         |
| `netstat`     | `netstat` / `ss` | Show network connections              |
| `nslookup`    | `nslookup`     | DNS lookup                              |
| -             | `curl` / `wget`| Download from a URL                     |

---

## 🛠 System Utilities

| Windows       | Linux/Unix     | Description                              |
|---------------|----------------|------------------------------------------|
| `time`        | `date`         | Display system time/date                 |
| `chdir`       | `pwd`          | Show current directory                   |
| `systeminfo`  | `uname -a`     | System and kernel info                   |
| `format`      | `mkfs.ext4` or `gparted` | Format storage                    |
| `chkdsk`      | `fsck`         | Check disk integrity                     |
| -             | `df -h`        | Disk space usage                         |
| -             | `du -sh`       | Directory space usage                    |

---

## 📦 Archiving & Compression

| Windows       | Linux/Unix         | Description                       |
|---------------|--------------------|-----------------------------------|
| -             | `tar`              | Archive files                     |
| -             | `gzip` / `gunzip`  | Compress and decompress           |
| -             | `zip` / `unzip`    | Create and extract zip files      |

---

## 📅 Scheduled Tasks

| Windows       | Linux/Unix        | Description                            |
|---------------|-------------------|----------------------------------------|
| `at`          | `cron` / `crontab`| Schedule repeated jobs                 |
| `schtasks`    | `crontab -e`      | Edit scheduled jobs                    |
| -             | `watch`           | Run a command repeatedly               |

---

## 🧠 Environment Management

| Windows            | Linux/Unix               | Description                           |
|--------------------|--------------------------|---------------------------------------|
| `set var=value`    | `export var=value`       | Set environment variables             |
| `echo %VAR%`       | `echo $VAR`              | Print variable value                  |
| -                  | `printenv`               | List all environment variables        |
| -                  | `which <command>`        | Show path of an executable            |
| -                  | `alias` / `unalias`      | Create or remove command shortcuts    |
| -                  | `source ~/.bashrc`       | Reload terminal configuration         |

---

## 📘 Help & Documentation

| Windows       | Linux/Unix   | Description                              |
|---------------|--------------|------------------------------------------|
| `command /?`  | `man command`| Display command manual                   |
| `help`        | `help`       | Display help on built-ins                |
| -             | `--help`     | Show command-specific help               |

---

### ✅ Tips
- Use `tab` to auto-complete commands and paths
- Use `history` to see previous commands
- Combine commands with `&&` or `|` for advanced usage

---

📁 Recommended folder name in your repo: `unix-windows-command-reference`

📄 Save this file as: `unix_vs_windows_commands.md`

---

🔗 Helpful Links:
- [Explainshell](https://explainshell.com/) – Breakdown of shell commands
- [SS64 Command Reference](https://ss64.com/)
- [Linux Command Library](https://tldr.sh/)
