import os
import shutil

from_dir="C:/Users/Ryan/Desktop/progamação 2/pythons/PRO_1-1_C102_AtividadeDoAluno1-main"
to_dir="C:/Users/Ryan/Desktop/progamação 2/pythons/aula 102"
list_of_files=os.listdir(from_dir)

print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    
    print(name)
    print(extension)

    if extension=="":
        continue
    if extension in [".gif",".png",".jpeg",".jpg",".jfif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"Imagens da aula 102"
        path3=to_dir+"/"+"Imagens da aula 102"+"/"+file_name
        print(path1)
        print(path3)

        if os.path.exists(path2):
            print("Movendo "+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Movendo "+file_name+"...")
            shutil.move(path1,path3)