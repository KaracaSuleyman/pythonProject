import os
from datetime import datetime


def edit_date():
    folder= input("Enter the folder to be edited path: ")
    files=[]         #dosyalar depolanacak
    dates=[]        #tarihler depolanacak
    def list_dir():
        for file in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, file)): #dosyamiz klasor mu onu kontrol ediyor
                continue

            if file.startswith("."):                        #dosyanin gizli dosyami oldugunu kontrol ettik
                continue

            else:
                files.append(file)

    list_dir()

     # tarihleri  alma
    for file in files:
        date_stamp= os.stat(os.path.join(folder, file)).st_mtime
        date=datetime.fromtimestamp(date_stamp).strftime("%d/%m/%Y")
        if date in dates:
            continue
        else:
            dates.append(date)

    for date in dates:
        if os.path.isdir(os.path.join(folder, date)):
            continue
        else:
            os.mkdir(os.path.join(folder, date))

    for file in files:

        date_stamp = os.stat(os.path.join(folder, file)).st_mtime
        date = datetime.fromtimestamp(date_stamp).strftime("%d/%m/%Y")

        os.rename(os.path.join(folder,file), os.path.join(folder,date,file))

if __name__ == "__main__":
    edit_date()

