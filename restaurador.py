import os

backups_dir='backups'

carpetas=os.listdir(backups_dir)

for i,c in enumerate(carpetas):
    fecha=c.split("data")[1].split(".db")[0]
    print(i,"fecha del backup: ",fecha)