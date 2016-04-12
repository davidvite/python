import os
def rename_files() :
    #(1) get the files names in a folder
    
    file_list = os.listdir("/Users/davidvite/Downloads/what")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir("/Users/davidvite/Downloads/what")
    
    #(2) for each file, rename filename

    for file_name in file_list:
       print("Old-name -"+file_name)
       print("New-name -"+file_name.translate(None,"0123456789"))
       os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_files()
