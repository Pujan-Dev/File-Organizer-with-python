# File Organizer

A simple Python script to organize files in your directory into categorized folders like `IMAGES`, `VIDEOS`, `DOCUMENTS`, `PROGRAMMING`, `AUDIO`, `ARCHIVES`, and `OTHER`.

## ✅ Features

- Automatically sorts files by type
- Handles unknown files into an `OTHER` folder
- Cleans up empty folders (if not in category list)
- Supports many common file formats

## 📁 Categories Supported

| Category    | File Extensions                    |
| ----------- | ---------------------------------- |
| IMAGES      | `.jpg`, `.png`, `.svg`, ...        |
| VIDEOS      | `.mp4`, `.avi`, `.mkv`, ...        |
| DOCUMENTS   | `.pdf`, `.docx`, `.xlsx`, ...      |
| ARCHIVES    | `.zip`, `.tar`, `.rar`, ...        |
| AUDIO       | `.mp3`, `.wav`, `.ogg`, ...        |
| PROGRAMMING | `.py`, `.cpp`, `.html`, `.js`, ... |
| OTHER       | Any unsupported or unknown file    |

## 🚀 Usage

1. **Clone or download the repository.**
2. Place the script in the folder you want to organize.
3. Run the script:

```bash
python organize.py
```

4. Files will be moved into folders like `IMAGES/`, `VIDEOS/`, etc.

## 🧠 How it Works

- The script scans the current directory.
- It checks the file extensions and maps them to categories.
- Each file is moved into its corresponding folder.
- Unrecognized file types go into the `OTHER` folder.
- Empty folders (not in the category list) are removed.

## 📌 Requirements

No external libraries needed — just Python 3.

## 📃 License

This project is open-source and free to use.
