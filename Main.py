import os
import shutil
import time

cooldown = 5
username = "your name here"

print("Running...")

downloadfolder = rf"C:\Users\{username}\Downloads"
photosfolder = rf"C:\Users\{username}\OneDrive\Pictures"
videosfolder = rf"C:\Users\{username}\Videos"
musicfolder = rf"C:\Users\{username}\Music"

file_extension_map = {
            '.jpg': photosfolder,
            '.png': photosfolder,
            '.mp4': videosfolder,
            '.mp3': musicfolder
        }

known_folders = set(
    f for f in os.listdir(downloadfolder)
    if os.path.isfile(os.path.join(downloadfolder, f))
)

while True:
    current_folders = set(
        f for f in os.listdir(downloadfolder)
        if os.path.isfile(os.path.join(downloadfolder, f))
    )
    print("Successfully checked downloads folder")
    newfolders = current_folders - known_folders

    for folder in newfolders:
        print(f"New file detected: {folder}")
        filename, ext = os.path.splitext(folder)
        ext = ext.lower()


        moved = False

        for ext_key, target_folder in file_extension_map.items():
            if ext == ext_key:
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                source = os.path.join(downloadfolder, folder)
                destination = os.path.join(target_folder, folder)

                print(f'{filename} should go to {target_folder}')
                shutil.move(source, destination)
                moved = True
        if not moved:
            print(f'{filename}{ext} doesnt have a folder it should go in!')

        
    
    known_folders = current_folders

    time.sleep(cooldown)

# Personal os/shutil notes

# listdir(foldername) lists things inside that folder
# mkdir(foldername) creates a folder called foldername
# makedirs(foldername/subfolder)creates nested folders
# os.rmdir(foldername) removes an empty folder
# os.removedirs(foldername/subfolder) removes nested folders
# os.chdir(foldername) changes directory
# os.getcwd gets current directory
# os.remove(file) removes a file
# os.rename(oldname, newname) renames a file
# os.path.exists(foldername) check if a path exists
# os.path.isdir(foldername) returns true if its a folder
# os.path.isfile(filename) returns true it its a file
# os.path.join joins paths
# os.path.splittext(file.png) splits file name and extension if you were to print this it would output "file", ".png"
# os.path.getsize(foldername) gets the size of the folder in bytes
# os.path.abspath(foldername) gets the full pathname of a path
# os.name returns the name of the operating system
# shutil.move(currentpath, newpath) moves a file from currentpath to newpath
