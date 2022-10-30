import os
import shutil
def new_older():
    name = input('введите название папки: ')
    os.mkdir(name)
    print('папка', name, 'создана! ')



def delete_tip(a):
    name = input(" введите название : ")
    if a == 'папка':
        os.rmdir(name)
        print( a, name , ' удалена!')
    else:
        os.remove(name)
        print(a, name , ' удален!')


def delete_file_older():
    tip = input('удалить: 1 - папка, 2 - файл:  ')
    if tip == '1':
        delete_tip('папка')
    else:
        delete_tip('файл')

def copy_tip(a):
    name = input(f'введите название: ')
    name_2 = input(f'введите новое название : ')
    if a == 'файл':
        shutil.copyfile(name, name_2)
        print('Копия', name_2, 'создана')
    else:
        shutil.copytree(name, name_2)
        print('Копия', name_2, 'создана')

def copy_older_file():
    tip = input('копируем : 1 - папка, 2 - файл :  ')
    if tip == '2':
         copy_tip('файл')
    else:
        copy_tip(123)
def list_older_files(a):
    dirs = []
    files = []
    files
    cvb = os.listdir()
    for i in cvb:
        if '.py' in i:
            files.append(i)
        else:
            dirs.append(i)
    if a =='папка':
        print(dirs)
    else:
        print(files)
