import requests
import shutil

dirfile = input("Enter path to the directory with file(no \"www.\" !):")
file = input("Enter the name of the file:")

fullpath = dirfile + file

filereq = requests.get(fullpath, stream=True)
print(filereq)

with open(file, "wb") as receive:
    shutil.copyfileobj(filereq.raw, receive)
del filereq

with open(file, "r", encoding='windows-1251', errors='ignore') as f:
    text = f.read()
    print(text)

