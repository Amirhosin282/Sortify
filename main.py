from cli.config import view, line
import os
import platform
import shutil

# get cli baner and show it by pyfiglet and rainbowtext
view()

work_path = input("Enter the address of the folder you want to perform the operation on: \033[0m").strip()
if not os.path.isdir(work_path):
    print("\033[31m Folder not found")
    exit()

# get files from working folder by os.listdir
files = [
    f for f in os.listdir(work_path)
    if os.path.isfile(os.path.join(work_path, f))
]

# check folders and create if not exist
if not os.path.exists(os.path.join(work_path, "Documents")):
    os.mkdir(os.path.join(work_path, "Documents"))
    print("\033[32m Documents folder created")

if not os.path.exists(os.path.join(work_path, "Audio")):
    os.mkdir(os.path.join(work_path, "Audio"))
    print("\033[32m Audio folder created")

if not os.path.exists(os.path.join(work_path, "Videos")):
    os.mkdir(os.path.join(work_path, "Videos"))
    print("\033[32m Videos folder created")

if not os.path.exists(os.path.join(work_path, "Pictures")):
    os.mkdir(os.path.join(work_path, "Pictures"))
    print("\033[32m Pictures folder created")

if not os.path.exists(os.path.join(work_path, "Other")):
    os.mkdir(os.path.join(work_path, "Other"))
    print(f"\033[32m Other folder created\n\033[33m{line}")

# find file type and move to folder
for i in files:
    file_name = i.lower()
    if file_name.endswith((".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".ppt", ".pptx", ".xls", ".xlsx")): # find Doc files
        shutil.move(os.path.join(work_path, i), os.path.join(work_path, "Documents"))
    
    elif file_name.endswith((".mp3", ".wav", ".flac", ".ogg", ".m4a")): # find Audio files
        shutil.move(os.path.join(work_path, i), os.path.join(work_path, "Audio"))
    
    elif file_name.endswith((".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm", ".flv")): # find video files
        shutil.move(os.path.join(work_path, i), os.path.join(work_path, "Videos"))
    
    elif file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff")): # find pic files
        shutil.move(os.path.join(work_path, i), os.path.join(work_path, "Pictures"))
    else:
        shutil.move(os.path.join(work_path, i), os.path.join(work_path, "Other"))

# print result
print("\033[32m all doc files moved to Documents folder")
print("\033[32m all Auditory files moved to Audio folder")
print("\033[32m all pic files moved to Pictures folder")
print("\033[32m all Video files moved to Videos folder")