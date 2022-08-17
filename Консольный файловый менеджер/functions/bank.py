def bank():
    money = 0
    sum = ''
    item = ''
    while True:
        print('1. Мой баланс')
        print('2. пополнение счета')
        print('3. покупка')
        print('4. история покупок')
        print('5. выход')

        choice = input('Выберите пункт меню: ' )
        if choice == '1':
            print (money)
        elif choice == '2':
            money = int(input('Введите сумму пополнения: '))
            print(f'Ваш балланс: {money}')
        elif choice == '3':
            sum_1 = int(input("Введите сумму покупки: "))
            sum += str(sum_1)+' '
            if sum_1 > money:
                print('Error, not money')
            else:
                item_1 = input("Введите название товара: ")
                item += item_1+ ' '
                money -= sum_1
                print(f'Ваш балланс: {money}')
        elif choice == '4':
            print (f'Название: {item} \n Cумма:  {sum} ')
            print(f'Ваш балланс: {money}')
        elif choice == '5':
            break
        else:
            print('Неверный пункт меню')
