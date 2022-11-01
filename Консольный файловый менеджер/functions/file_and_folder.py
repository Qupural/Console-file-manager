import os
from functions import dekorator

@dekorator.decor
def new_older():
    name = input('введите название папки: ')
    os.mkdir(name)
    print('папка', name, 'создана! ')



def delete_tip(a):
    try:
        name = input(" введите название : ")
        if a == '1':
            os.rmdir(name)
            print( a, name , ' удалена!')
        else:
            os.remove(name)
            print(a, name , ' удален!')
    except FileNotFoundError:
        print('Такой папки или файла нет! ')
        print('Правильно введите название!')

@dekorator.decor
def delete_file_older():
    tip = input('удалить: 1 - папка, 2 - файл:  ')
    resulte = delete_tip('1') if tip == '1' else  delete_tip('2')
    return resulte


def copy_tip(a):
    try:
        name = input(f'введите название: ')
        name_2 = input(f'введите новое название : ')
        if a == '1':
            shutil.copyfile(name, name_2)
            print('Копия', name_2, 'создана')
        else:
            shutil.copytree(name, name_2)
            print('Копия', name_2, 'создана')
    except FileNotFoundError:
        print('Такой папки или файла нет! ')
        print('Правильно введите название!')

@dekorator.decor
def copy_older_file():
    try:
        tip = input('копируем : 1 - папка, 2 - файл :  ')
        resulte =  copy_tip('1') if tip == '2' else copy_tip('2')
        return resulte
    except TypeError:
        print('Введите номер выбора')

@dekorator.decor
def list_older_files(a):
    dirs = []
    files = []
    cvb = os.listdir()
    resulte = [files.append(i) if '.py' in i else dirs.append(i) for i in cvb]
    resultes =  print(dirs) if a =='папка' else print(files)
    return resultes