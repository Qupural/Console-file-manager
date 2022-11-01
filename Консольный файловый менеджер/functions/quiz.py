from functions import new
import random
from functions import dekorator

@dekorator.decor
def quiz():
    celebrities = [ 'Сергей Шнуров', 'Егор Крид', 'Дима Билан', 'Баста (Василий Вакуленко)','Филипп Киркоров', 'Полина Гагарина', 'Григорий Лепс', 'Тимати (Тимур Юнусов)', 'Иван Ургант','Николай Басков']
    data = [ '13.04.1973', '25.06.1994', '24.12.1981', '20.04.1980', '30.04.1967', '27.03.1987', '16.07.1962', '15.08.1983', '16.04.1978', '15.10.1976']
    game = input('Начать игру? : ')
    if game == 'да ':
        cvb = 0
        po = 0
        no = 0
        answer = ' '
        while cvb!= 5:
            result = random.randrange(len(celebrities))
            value = celebrities[result]
            answer = input(f'Введите дату рождения {value}: ')
            answer_data = data[result]
            if answer == answer_data:
                celebrities.remove(value)
                data.remove(answer_data)
                cvb += 1
                po += 1
                print('good')
            else:
                print(f'Правильный ответ: {new.get_date(answer_data)}')
                cvb+=1
        no = 5 - po
        print('Кол-во правильных ответов:', po,'/' 'Кол-ко неправильных ответов:', no)
    elif game == 'нет':
        print('пока!')
    else:
        print('Я вас не понял ')

