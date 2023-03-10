# Подключаем модуль random
import random

# Создаем глобальный список, содержащий слова для игры
word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место',
             'вопрос', 'лицо', 'глаз', 'страна', 'друг', 'сторона', 'дом', 'случай', 'ребенок', 'голова',
             'система', 'вид', 'конец', 'отношение', 'город', 'часть', 'женщина', 'проблема', 'земля',
             'решение', 'власть', 'машина', 'закон', 'час', 'образ', 'отец', 'история', 'нога', 'вода',
             'война', 'возможность', 'компания', 'результат', 'дверь', 'народ', 'область', 'число',
             'голос', 'развитие', 'группа', 'жена', 'процесс', 'условие', 'книга', 'ночь', 'суд', 'деньга',
             'уровень', 'начало', 'государство', 'стол', 'средство', 'связь', 'имя', 'президент', 'форма',
             'путь', 'организация', 'качество', 'действие', 'статья', 'общество', 'ситуация', 'деятельность',
             'школа', 'душа', 'дорога', 'язык', 'взгляд', 'момент', 'минута', 'месяц', 'порядок', 'цель',
             'программа', 'муж', 'помощь', 'мысль', 'вечер', 'орган', 'правительство', 'рынок', 'предприятие',
             'партия', 'роль', 'смысл', 'мама', 'мера', 'улица', 'состояние', 'задача', 'информация', 'театр',
             'внимание', 'производство', 'квартира', 'труд', 'тело', 'письмо', 'центр', 'утро', 'мать', 'комната',
             'семья', 'сын', 'смерть', 'положение', 'интерес', 'федерация', 'век', 'идея', 'управление', 'автор',
             'окно', 'ответ', 'совет', 'разговор', 'мужчина', 'ряд', 'счет', 'мнение', 'цена', 'точка', 'план',
             'проект', 'глава', 'материал', 'основа', 'причина', 'движение', 'культура', 'сердце', 'рубль', 'наука',
             'документ', 'неделя', 'вещь', 'чувство', 'правило', 'служба', 'газета', 'срок', 'институт', 'ход',
             'стена', 'директор', 'плечо', 'опыт', 'встреча', 'принцип', 'событие', 'структура', 'количество',
             'товарищ',
             'создание', 'значение', 'объект', 'гражданин', 'очередь', 'период', 'образование', 'состав', 'пример',
             'лес', 'исследование', 'девушка', 'данные', 'палец', 'судьба', 'тип', 'метод', 'политика', 'армия', 'брат',
             'представитель', 'борьба', 'использование', 'шаг', 'игра', 'участие', 'территория', 'край', 'размер',
             'номер',
             'район', 'население', 'банк', 'начальник', 'класс', 'зал', 'изменение', 'большинство', 'характер', 'кровь',
             'направление', 'позиция', 'герой', 'течение', 'девочка', 'искусство', 'гость', 'воздух', 'мальчик',
             'фильм',
             'договор', 'регион', 'выбор', 'свобода', 'врач', 'экономика', 'небо', 'факт', 'церковь', 'завод', 'фирма',
             'бизнес', 'союз', 'деньги', 'специалист', 'род', 'команда', 'руководитель', 'спина', 'дух', 'музыка',
             'способ', 'хозяин', 'поле', 'доллар', 'память', 'природа', 'дерево', 'оценка', 'объем', 'картина',
             'процент', 'требование', 'писатель', 'сцена', 'анализ', 'основание', 'повод', 'вариант', 'берег',
             'модель', 'степень', 'самолет', 'телефон', 'граница', 'песня', 'половина', 'министр', 'угол', 'зрение',
             'предмет', 'литература', 'операция', 'двор', 'спектакль', 'руководство', 'солнце', 'автомобиль',
             'родитель',
             'участник', 'журнал', 'база', 'пространство', 'защита', 'название', 'стих', 'море', 'удар', 'знание',
             'солдат', 'миллион', 'строительство', 'технология', 'председатель', 'сон', 'сознание', 'бумага', 'реформа',
             'оружие', 'линия', 'текст', 'выход', 'ребята', 'магазин', 'соответствие', 'участок', 'услуга', 'поэт',
             'предложение', 'желание', 'пара', 'успех', 'среда', 'возраст', 'комплекс', 'бюджет', 'представление',
             'площадь', 'генерал', 'господин', 'дочь', 'понятие', 'кабинет', 'безопасность', 'фонд', 'сфера', 'папа',
             'сотрудник', 'продукция', 'будущее', 'продукт', 'содержание', 'художник', 'республика', 'сумма',
             'контроль',
             'парень', 'ветер', 'хозяйство', 'помочь', 'курс', 'губа', 'река', 'грудь', 'огонь', 'нос', 'волос', 'ухо',
             'отсутствие', 'радость', 'сад', 'подготовка', 'необходимость', 'доктор', 'лето', 'камень', 'здание',
             'капитан', 'собака', 'итог', 'рис', 'техника', 'элемент', 'источник', 'деревня', 'депутат', 'проведение',
             'рот', 'масса', 'комиссия', 'цвет', 'рассказ', 'функция', 'определение', 'мужик', 'обеспечение',
             'обстоятельство', 'работник', 'разработка', 'лист', 'звезда', 'гора', 'применение', 'победа', 'товар',
             'воля', 'зона', 'предел', 'целое', 'личность', 'офицер', 'влияние', 'поддержка', 'ответственность'
             ]


# Создаем функцию, которая возвращает случайное слово из списка word_list в верхнем регистре
def get_word():
    x = random.randint(0, 22)
    word = word_list[x].upper()
    return word


# Защита от дурака
def is_valid(inf):
    if inf.isalpha():
        return True
    else:
        return False


# Замена прочерков угаданными буквами
def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end='')
        else:
            print('_', end='')
    print()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
--------
|      |
|      O
|     \\|/
|      |
|     / \\
-''',
        # голова, торс, обе руки, одна нога
        '''
--------
|      |
|      O
|     \\|/
|      |
|     / 
-''',
        # голова, торс, обе руки
        '''
--------
|      |
|      O
|     \\|/
|      |
|      
-''',
        # голова, торс и одна рука
        '''
--------
|      |
|      O
|     \\|
|      |
|     
-''',
        # голова и торс
        '''
--------
|      |
|      O
|      |
|      |
|     
-''',
        # голова
        '''
--------
|      |
|      O
|    
|      
|     
-''',
        # начальное состояние
        '''
--------
|      |
|      
|    
|      
|     
-'''
    ]
    return stages[tries]


# Основная функция для игры
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву слова
    guessed = False # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    # Приветствие пользователя и вывод дисплея на экран
    print('\nДавайте играть в угадайку слов!', display_hangman(tries))
    print('Загаданное слово:', word_completion)
    # Основной цикл функции
    while True:
        # Запрашиваем у пользователя букву и переводим в верхний регистр
        inf = input('Введите букву или слово на русском языке:\n').upper()
        # Используем защиту от дурака на каждый символ
        if is_valid(inf):
            # Условие, что буква уже была использована
            if inf in guessed_words or inf in guessed_letters:
                print('Уже было!')
                continue
            # Условие, что пользователь ввел слово
            if len(inf) > 1:
                # Угадал
                if inf == word:
                    print(f'Поздравляем, вы угадали слово {word}! Вы победили!')
                    break
                # Не угадал
                else:
                    # Добавляем слова в уже встречавшиеся
                    guessed_words.append(inf)
                    # Отнимаем попытку
                    tries -= 1
                    print(f'Не верно, осталось попыток {tries}!')
                    # Выводим измененный дисплей, так как попытки уменьшились
                    print(display_hangman(tries))
                    # Выводим измененное слово с помощью функции print_word
                    print_word(word, guessed_letters)
                    # Если попыток осталось 0, то заканчиваем игру и выводим загаданное слово
                    if tries == 0:
                        print(f'Вы не смогли угадать слово: {word}!')
                        break
                    continue
            # Условие, что пользователь ввел букву и угадал
            if inf in word:
                # добавляем букву в список использованных букв
                guessed_letters.append(inf)
                # Рассматриваем каждую букву в слове
                for c in word:
                    # Если буква не в списке уже использованных букв
                    if c not in guessed_letters:
                        # то выводим:
                        print('Вы угадали букву!')
                        # Выводим измененное слово с помощью функции print_word
                        print_word(word, guessed_letters)
                        break
                    # Если все буквы угаданы, выводим слово
                    if guessed:
                        print_word(word, guessed_letters)
                        print(f'Поздравляем, вы угадали слово {word}! Вы победили!')
                        break
            # Не угадали букву
            else:
                # добавляем букву в список использованных букв
                guessed_letters.append(inf)
                # Отнимаем попытку
                tries -= 1
                print(f'Не верно, осталось попыток {tries}!')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
            # Если попыток не осталось, выводим:
            if tries == 0:
                print(f'Вы не смогли угадать слово: {word}!')
                break
        # Если не прошел защиту на дурака
        else:
            print('Ошибочный ввод. Попробуйте заново!')


# Создаем переменную для основного цикла
new_game = 'да'
# Основной цикл программы, если переменная new_game == 'да', то используем основную функцию play()
while new_game == 'да':
    play(get_word())
    # Узнаем о желании повторной игры:
    new_game = input('\nЕсли хотите сыграть еще раз, напишите "Да": ').lower()
else:
    # Если такого желания нет:
    print('\nВсего хорошего! Заглядывай еще :)')