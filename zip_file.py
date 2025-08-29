# Say you’re working on a project whose files you keep in a folder named C:\Users\Al\AlsPythonBook. You’re worried about losing your work, so you’d like to create ZIP file “snapshots” of the entire folder. You’d also like to keep different versions of these snapshots, so you want the ZIP file’s filename to increment each time a new version is made; for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip, AlsPythonBook_3.zip, and so on. You could do this by hand, but that would be rather annoying, and you might accidentally misnumber the ZIP files’ names. It would be much simpler to run a program that does this boring task for you.
import pathlib
import zipfile
import os

def backup_to_zip():
    #The function will determine what filename to use for the ZIP file it will create.
    print(pathlib.Path().cwd().parts[-1])
    file_name_1 = pathlib.Path().cwd().parts[-1]
    n = 0
    while True:
        p = pathlib.Path(f"spam_{n}.zip")
        if(p.exists()):
            print("it exists")
        else:
            print("nope about to make zip:" + str(p))
            zipfile.ZipFile(f"spam_{n}.zip", "w")
            break
        n += 1
        
    #Then, it will create the file, walk the folder folder
    #add each of the subfolders and files to the ZIP file.

backup_to_zip()