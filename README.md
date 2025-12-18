# 🚀 Auto Upversion

Let’s get started! This script is designed to automatically save incremental versions of `.hip` files in Houdini, preventing overwrites and keeping a clean, consistent versioning system.

---

## 📦 What does this script do?

The script analyzes the current file path and:

* Detects whether the file name already contains a version tag (`_v###`).
* If no version exists, it automatically creates the initial `_v000`.
* If a version exists, it safely increments it without overwriting files.
* Normalizes version padding to a minimum of 3 digits.
* Saves the `.hip` file using the next available version.

---

## ✨ Features

* ✅ Intelligent auto-increment versioning
* ✅ Full overwrite protection
* ✅ Automatic padding normalization
* ✅ Works with any file naming convention
* ✅ Ideal for buttons, shelf tools or callbacks

---

## 💡 Recommended usage

This script is perfect for:

* Quick save buttons
* Shelf tools
* Versioning pipelines
* Workflows where file safety is critical

Simply pass the current `.hip` file path, and the system will take care of the rest.
