from os import listdir, path, mkdir
import shutil

TARGET_DIR = r"C:\Users\ejans\Downloads"

# TARGET_DIR = r"C:\Users\ejans\Downloads"

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
        try:
            listFiles(path.join(target_dir, i))
            folders.append(i)
        except:
            files.append(i)
        
    return {"folders": folders, "files": files}

# Checking extension name
def checkExt(target_dir):
    ext_list = []
    files_list = checkFile(target_dir)["files"]
    
    for i in files_list:
        ext_list.append(i.split('.')[-1])
        
    filtered_ext = list(dict.fromkeys(ext_list))
    return filtered_ext
    
# Creating Directories
def createDirectories(target_dir):
    for i in checkExt(target_dir):
        try:
            mkdir(path.join(target_dir, i))
            print(f"Folder {i} Created")
        except FileExistsError:
            print(f"Folder {i} Already Exists")
        except Exception as e:
            print(f"Error creating folder {i}: {e}")
            
# Moving files to respective directories
def moveFilesToDir(target_dir):
    file_list = checkFile(target_dir)["files"]
    if file_list:
        try:
            for i in file_list:
                ext_name = i.split('.')[-1]
                source = path.join(target_dir, i)
                target = path.join(target_dir, ext_name)
                shutil.move(source, target)
                print(f"File {i} moved to {ext_name}")
        except Exception as e:
            print("Error moving files: ", e)
        print("File organization successful")
    else:
        print("No files to organize")

def main(target_dir):
    createDirectories(target_dir)
    moveFilesToDir(target_dir)
    
if __name__  == "__main__":
    main(TARGET_DIR)