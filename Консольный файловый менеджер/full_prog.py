import platform
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
        from functions import file_and_folder
        file_and_folder.new_older()
    elif nume == '2':
        from functions import file_and_folder
        file_and_folder.delete_file_older()
    elif nume == '3':
        from functions import file_and_folder
        file_and_folder.copy_older_file()
    elif nume == '4':
        from functions import file_and_folder
        file_and_folder.list_older_files('папка')
    elif nume == '5':
        from functions import file_and_folder
        file_and_folder.list_older_files('файл')
    elif nume == '6':
        print(platform.uname())
    elif nume == '7':
        from functions import quiz
    elif nume == '8':
        from functions import bank
    elif nume == '9':
        break
