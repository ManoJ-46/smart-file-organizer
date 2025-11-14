import os
import shutil
from pathlib import Path

def organize(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("folder not found!")
        return

    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    }

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            for category, extensions in categories.items():
                if ext in extensions:
                    dest_folder = folder / category
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(dest_folder / file.name))
                    print(f"Moved {file.name} -> {category}/")
                    break

if __name__ == '__main__':
    path = input("Enter folder path to organize: ").strip('"')
    organize(path)
    print("\nAll files neatly organized!")
