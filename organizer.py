import os
import shutil

print("================================")
print("       FILE ORGANIZER")
print("================================")

folder = input("Enter the folder path: ")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
}

for filename in os.listdir(folder):

    file_path = os.path.join(folder, filename)

    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(filename)[1].lower()

    category = None

    for name, extensions in categories.items():
        if extension in extensions:
            category = name
            break

    if category is None:
        category = "Others"

    category_folder = os.path.join(folder, category)

    os.makedirs(category_folder, exist_ok=True)

    shutil.move(
        file_path,
        os.path.join(category_folder, filename)
    )

    print(f"Moved: {filename} -> {category}")

print()
print("Done! Your files have been organized.")