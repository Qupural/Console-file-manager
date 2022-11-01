import os
from functions import dekorator

@dekorator.decor
def derictor():
    rew = []
    if os.path.exists("listdir.txt"):
        with open('listdir.txt', 'r') as f:
            rew = rew.append(f)
    dir = []
    file = []
    cvb = os.listdir()
    for i in cvb:
        if '.py'  in i:
            file.append(i)
        elif '.txt' in i:
            file.append(i)
        elif '.data' in i:
            file.append(i)
        else:
            dir.append(i)
    with open('listdir.txt', 'w') as f:
        f.write(f'Files: {file}\n  Dirs: {dir}')