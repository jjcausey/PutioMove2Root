#   Libraries

import putio 


# Root Folder
root = 999999999 # INSERT YOUR ROOT FOLDER ID

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
                        #client.File.MP4(file2)
                        client.File.delete(file1)



PutioToken = 'XXXXXXXXXXXXXXXXXXXX' # INSERT YOUR TOKEN
             
client = putio.Client(PutioToken) # Instanciate Client Object

PutioMove2Root()



