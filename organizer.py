#  file/folder organizer 

import os
import shutil

source_folder=r"path of the folder "  # path of the folder 
#  file typee
file_type= {"images":[".jpg",".jpeg",".png",".fig"], "pdfs" : [".pdf"],"documents":[".txt",".docs",".xlsx",".pptx"],"videos":[".mp4",".mov",">mkv"]}

for folder in file_type :
    folder_path=os.path.join(source_folder,folder)  
    if not os.path.exists(folder_path) :
        os.mkdir(folder_path)

for file in os.listdir(source_folder) :
    file_path= os.path.join(source_folder,file)
    if os.path.isfile(file_path):
        for folder, extensions in file_type.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path,os.path.join(source_folder,folder))
                print(f"moved:{file}----> {folder}")
                break

