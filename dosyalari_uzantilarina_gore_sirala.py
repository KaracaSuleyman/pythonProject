import os

def edit():
    folder= input("Enter the folder to be edited path: ")
    files=[]         #dosyalar depolanacak
    extensions=[]    #uzantilar depolanacak
    def list_dir():
        for file in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, file)): #dosyamiz klasor mu onu kontrol ediyor
                continue

            if file.startswith("."):                        #dosyanin gizli dosyami oldugunu kontrol ettik
                continue

            else:
                files.append(file)

    list_dir()

    for file in files:                                       #uzantilari alma
        extension= file.split(".")[-1]
        if extension in extensions:
            continue
        else:
            extensions.append(extension)

    for extension in extensions:                            # klasorler olusturuluyor
        if os.path.isdir(os.path.join(folder, extension)):
            continue
        else:
            os.mkdir(os.path.join(folder, extension))

    for file in files:
        extension= file.split('.')[-1]
        os.rename(os.path.join(folder, file), os.path.join(folder,extension, file))

if __name__ == "__main__":
    edit()

