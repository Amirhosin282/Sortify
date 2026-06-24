# Sortify 📂

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Sortify is a lightweight Python utility that automatically organizes files inside a folder based on their file types.

It scans a directory and sorts documents, images, audio files, videos, and unknown files into dedicated folders, helping you keep messy directories clean and organized.

> Simple, fast, and built for everyday use.

---

## 🚀 Features

* Automatically organizes files by extension
* Creates destination folders when needed
* Supports documents, images, audio, and video files
* Handles uppercase and lowercase file extensions
* Cross-platform support
* Lightweight and dependency-free

---

## 📦 Folder Categories

| Folder    | Supported Extensions                                |
| --------- | --------------------------------------------------- |
| Documents | pdf, doc, docx, txt, odt, rtf, ppt, pptx, xls, xlsx |
| Audio     | mp3, wav, flac, ogg, m4a                            |
| Videos    | mp4, mkv, avi, mov, wmv, webm, flv                  |
| Pictures  | jpg, jpeg, png, gif, bmp, webp, svg, tiff           |
| Other     | Any unsupported file type                           |

---

## 📁 Example

Before:

```text
Downloads/
├── Report.pdf
├── Song.mp3
├── Photo.JPG
├── Movie.mkv
└── Unknown.xyz
```

After:

```text
Downloads/
├── Documents/
│   └── Report.pdf
├── Audio/
│   └── Song.mp3
├── Pictures/
│   └── Photo.JPG
├── Videos/
│   └── Movie.mkv
└── Other/
    └── Unknown.xyz
```

---

## 🛠 Usage

Clone the repository:

```bash
git clone https://github.com/amirhosin282/sortify.git
```

Run the program:

```bash
python main.py
```

Enter the path of the folder you want to organize and let Sortify do the work.

---

## ⚠️ Notes

* Existing folders will be reused if they already exist.
* Files are moved, not copied.
* Make sure you have permission to modify the target directory.
* Unsupported file types will be moved to the `Other` folder.

---

🎉 Made with Python by Amirhosin282

![Footer](https://capsule-render.vercel.app/api?type=waving\&color=gradient\&height=80\&section=footer)
