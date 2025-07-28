# 📄 File Hash Checker

A simple and beginner-friendly command-line tool to calculate and verify cryptographic hashes of files using common algorithms like `SHA-256` and `MD5`. Useful for file integrity verification, malware analysis, or just learning how file hashing works.

File Hash Checker is a CLI (command line interface) tool designed for ease of use. This tool is part of the **CyberTools** collection made by [ollieistic](https://github.com/ollieistic). I might make a GUI version of all tools in this collection in the future.

## ✨ Features

- Calculate file hash using multiple algorithms at once
- Copy any hash result to clipboard
- Compare results with another hash


## 📁 Supported Algorithms

These are the algorithms that are currently supported:

- `md5`
- `sha1`
- `sha224`
- `sha256`
- `sha384`
- `sha512`
- `sha3_256`
- `blake2b`
- `blake2s`

These cover the most commonly used hashing needs while keeping the tool lightweight.

## 🔐 Why Hash a File?

Hashing is a one-way cryptographic function that takes a file and produces a fixed-length string (the hash). It's often used to:

- Check if a download is corrupted or tampered with
- Validate file integrity in cybersecurity
- Detect malware or altered code
- Verify backups or software packages

## 📋️ Requirements

- **A Python 3.6.x installation**
- **Library "Pyperclip" installed**

---
### Windows Guide

1. Download Python at https://python.org/download
2. Make sure to add **PYTHON.EXE** to path and that you are installing as administrator
3. Install the **Pyperclip** library
```
pip install pyperclip
```

### Linux Guide (Arch)

If you are on a different Linux distribution other than Arch, please scroll to the bottom.

1. **Install Python3 and Pip**
```
sudo pacman -S python3
sudo pacman -S python-pip
```
2. **Clone the repository**
```
git clone https://github.com/ollieistic/cybertools
```
Note: You need to install `Git` to run this command. Install it via `sudo pacman -S git`.

3. **Create a virtual environment and activate it**

Run these commands to create a virtual environment and activate it - this is the best way to keep your system clean.
```
cd cybertools
python3 -m venv xyz
source xyz/bin/activate
```
Replace `xyz` with whatever you want to call your virtual environment, usually you just call it `venv`.

If you see `(venv)` at the beginning of each line in your terminal, that means you successfully activated your virtual environment. To deactivate it, run `deactivate`.

4. **Install the Pyperclip library**

Run this command to install Pyperclip in your virtual environment.
```
pip install pyperclip
```
**Note: Since the library will be installed in your virtual environment, you must run the tool when inside the virtual environment, otherwise the the tool will not work as the library isn't installed system-wide.**

If you prefer to have you Python libraries installed system-wide, which isn't recommended for security reasons, do it via this command:
```
sudo pacman -S install python-pyperclip
```

### Other Distros

The guide for Arch Linux works for most distros that use different package managers such as Ubuntu or Fedora. You only need to replace `pacman -S` with `apt install` or `dnf install` depending on your distribution.

Some packages may be named differently, if this is the case, please look it up.

I am sorry for not making a guide on other distros. This is because my first Linux distro was Arch and still is. I have not used any other distros before and I am not planning on doing so anytime in the future.
