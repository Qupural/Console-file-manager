import os
dirs = []
files = []
files
cvb = os.listdir()
for i in cvb:
    if '.py' in i:
        files.append(i)
    else:
        dirs.append(i)
print(files)
print(dirs)