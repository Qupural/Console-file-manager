import platform
from functions import file_and_folder
from functions import quiz
from functions import bank
while True:
    print('1. создать папку')
    print('2. удалить(файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. посмотреть только папки')
    print('5. посмотреть только файлы')
    print('6. просмотр информации об операционной системе')
    print('7. играть в викторину')
    print('8. операции с банковским счетом')
    print('9. выход')
    nume = input('видете номер пункта: ')
    if nume == '1':
        file_and_folder.new_older()
    elif nume == '2':
        file_and_folder.delete_file_older()
    elif nume == '3':
        file_and_folder.copy_older_file()
    elif nume == '4':
        file_and_folder.list_older_files('папка')
    elif nume == '5':
        file_and_folder.list_older_files('файл')
    elif nume == '6':
        print(platform.uname())
    elif nume == '7':
        quiz.quiz()
    elif nume == '8':
        bank.bank()
    elif nume == '9':
        break
