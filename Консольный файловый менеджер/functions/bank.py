import pickle
import os
def bank():
    money  = 0
    historys = []
    HISTORY = 'history.data'
    BALACE = 'balace.data'
    if os.path.exists(BALACE):
        with open(BALACE, 'rb') as f:
            money = pickle.load(f)

    if os.path.exists(HISTORY):
        with open(HISTORY, 'rb') as f:
            historys = pickle.load(f)

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
            moneyup = int(input('Введите сумму пополнения: '))
            money = money + moneyup
            print(f'Ваш балланс: {money}')
        elif choice == '3':
            sum = int(input("Введите сумму покупки: "))
            if sum > money:
                print('Error, not money')
            else:
                item = input("Введите название товара: ")
                money -= sum
                history = (item, sum)
                historys.append(history)
                print(f'Ваш балланс: {money}')
        elif choice == '4':
            for history in historys:
                print ((history))
            print(f'Ваш балланс: {money}')
        elif choice == '5':
            with open(BALACE, 'wb') as f:
                pickle.dump(money, f)
            with open(HISTORY, 'wb') as f:
                pickle.dump(historys, f)

            break
        else:
            print('Неверный пункт меню')