from os import listdir, path, mkdir
import shutil

TARGET_DIR = r"C:\Users\ejans\Downloads"

# Supported file extensions
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".zip"]

# Create required folders if they don't exist
def createRequiredDirectories(target_dir):
    required_dirs = ['Images', 'Videos', 'Audio', 'Documents', 'Others']
    for dir_name in required_dirs:
        dir_path = path.join(target_dir, dir_name)
        if not path.exists(dir_path):
            try:
                mkdir(dir_path)
                print(f"Folder {dir_name} Created")
            except Exception as e:
                print(f"Error creating folder {dir_name}: {e}")

# Check file extension and return the appropriate folder
def getFolderForFile(ext):
    ext = ext.lower()
    if ext in image_extensions:
        return 'Images'
    elif ext in video_extensions:
        return 'Videos'
    elif ext in audio_extensions:
        return 'Audio'
    elif ext in document_extensions:
        return 'Documents'
    else:
        return 'Others'
    
# Move files to respective directories based on file type
def moveFilesToDir(target_dir):
    file_list = checkFile(target_dir)["files"]
    if file_list:
        try:
            for file_name in file_list:
                ext_name = path.splitext(file_name)[-1].lower()  # Get the file extension and make it lowercase
                folder_name = getFolderForFile(ext_name)
                source = path.join(target_dir, file_name)
                target = path.join(target_dir, folder_name, file_name)
                shutil.move(source, target)
                print(f"File {file_name} moved to {folder_name}")
        except Exception as e:
            print("Error moving files: ", e)
        print("File organization successful")
    else:
        print("No files to organize")

# List files inside a directory
def listFiles(target_dir):
    try:
        files = listdir(target_dir)
        return files
    except FileNotFoundError:
        print(f"The directory {target_dir} does not exist.")
        return []
    except PermissionError:
        print(f"Permission denied to access the directory {target_dir}.")
        return []

# Checking items
def checkFile(target_dir):
    folders = []
    files = []
    files_list = listFiles(target_dir)
    
    # Sorting folders and files
    for i in files_list:
        item_path = path.join(target_dir, i)
        if path.isdir(item_path):
            folders.append(i)
        else:
            files.append(i)
        
    return {"folders": folders, "files": files}

def main(target_dir):
    if path.exists(target_dir):
        createRequiredDirectories(target_dir)
        moveFilesToDir(target_dir)
    else:
        print(f"The directory {target_dir} does not exist.")
    
if __name__  == "__main__":
    main(TARGET_DIR)