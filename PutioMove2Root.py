#   Libraries

import putiopy

############################# User Specific ###########################

# Root Folder
root = 999999999 # INSERT YOUR ROOT FOLDER

# Token
PutioToken = ' ' # INSERT YOUR TOKEN

############################# User Specific ###########################

# List Files, Move Video files to Root Folder  and Delete Sub-folders

def PutioMove2Root():
        files1 = client.File.list(root) 
        for file1 in files1:

            if file1.file_type == "FOLDER":
                files2 = client.File.list(file1.id)
                for file2 in files2:
                    if file2.file_type == "VIDEO":
                        print file2.id
                        client.File.move(file2,root)
                        client.File.delete(file1)

client = putiopy.Client(PutioToken) # Instanciate Client Object

PutioMove2Root()



