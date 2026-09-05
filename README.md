# 📂 File Organizer Script

## 📝 What is this?
This is a simple Python automation script designed to help clean up cluttered folders (like your **Downloads** or **Desktop**). 

Instead of manually sorting through hundreds of files, this script automatically scans a folder, creates organized subfolders based on file types, and moves each file into its matching category.

---

## 🎯 What it does
When you run the script and give it a folder path, it automatically organizes files into the following categories:

* **🖼️ Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
* **🎥 Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`
* **📄 Documents**: `.pdf`, `.docx`, `.doc`, `.txt`
* **🎵 Music**: `.mp3`, `.wav`, `.flac`
* **📦 Archives**: `.zip`, `.rar`, `.7z`
* **📁 Others**: Any unrecognized or miscellaneous files

---

## ✨ Features
* **Automatic Folder Creation**: Creates category folders automatically if they don't already exist.
* **Safe Handling**: Leaves existing folders untouched and only moves loose files.
* **Case-Insensitive**: Works with both lowercase and uppercase file extensions (e.g., `.PNG` and `.png`).
* **Real-time Output**: Shows you line-by-line in the console which file was moved and where it went.
  
