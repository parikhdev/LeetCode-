import os
import shutil
Source_Folder="D:\letstest"
File_Cat={
    "Documents":[".pdf","docx",".txt",".pptx"],
    "Images":[".jpg",".jpeg",".gif",".png"],
    "Videos":[".mp3",".mp4"]
}

def organize_folder(folder):
    for filename in os.listdir(folder):
        file_path=os.path.join(folder,filename)
        if os.path.isfile(file_path):
            ext=os.path.splitext(filename)[1].lower()
            moved=False
            for category,extensions in File_Cat.items():
                if ext in extensions:
                    fol_path=os.path.join(folder,category)
                    os.makedirs(fol_path,exist_ok=True)
                    shutil.move(file_path,os.path.join(fol_path,filename))
                    print(f"Moved--{filename}-->{category}")
                    moved=True
                    break
            if moved==False:
                fol_path = os.path.join(folder,"Others")
                os.makedirs(fol_path, exist_ok=True)
                shutil.move(file_path, os.path.join(fol_path, filename))
                print(f"Moved--{filename}-->Others")

organize_folder(Source_Folder)