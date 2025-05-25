import os
from pathlib import Path

# Define file categories and associated extensions
CATEGORIES = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn",
                  ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PROGRAMMING": [".py", ".c", ".cpp", ".h", ".java", ".js", ".ts", ".jsx", ".tsx", ".html", ".css", ".scss", ".php", ".go", ".rs", ".sh", ".bat", ".json", ".xml", ".yaml", ".yml", ".ipynb"],
    "OTHER": []  # Will collect everything that doesn't match
}

# Create reverse map for extensions
EXTENSION_MAP = {
    ext: category for category, extensions in CATEGORIES.items() for ext in extensions
}

def organize_files(directory="."):
    base_path = Path(directory)

    for entry in base_path.iterdir():
        if entry.is_file():
            ext = entry.suffix.lower()
            category = EXTENSION_MAP.get(ext, "OTHER")
            target_dir = base_path / category
            target_dir.mkdir(exist_ok=True)
            new_path = target_dir / entry.name
            entry.rename(new_path)
            print(f"Moved: {entry.name} -> {category}/")

    # Try to remove empty folders not in categories
    for entry in base_path.iterdir():
        if entry.is_dir() and entry.name not in CATEGORIES:
            try:
                os.rmdir(entry)
                print(f"Removed empty folder: {entry.name}")
            except OSError:
                pass

    print("Done organizing.")

if __name__ == "__main__":
    organize_files()

