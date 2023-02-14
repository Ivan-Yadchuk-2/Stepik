# Создаем функцию, которая шифрует или дешифрует введенное предложение
def do_cipher(direction, language, step):
    # Задаем 4 строки с прописными и строчными латинскими и русскими буквами
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    # Создаем условие по выбранному языку Анг или Рус
    if language == 'АНГ':
        # Устанавливаем величину алфавита
        eng = 26
        # Определяем шифрование (1) или дешифрование (2)
        if direction == '1':
            # Вводимая информация
            s1 = input('Введите текст для обработки:\n')
            res1 = ''
            for i in s1:
                # Условия для небуквенных символов
                if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    # Если символ не буква, то мы просто добавляем его в результирующую строку
                    res1 += i
                else:
                    # Задаем условие, если символ является буквой и является прописным/строчным, то с помощью формулы
                    # прибавляем к строке
                    if i.isalpha() and i.islower():
                        res1 += lower_eng_alphabet[(lower_eng_alphabet.find(i) + step) % eng]
                    elif i.isalpha() and i.isupper():
                        res1 += upper_eng_alphabet[(upper_eng_alphabet.find(i) + step) % eng]
            # Возвращаем зашифрованное слово
            return res1

        elif direction == '2':
            s2 = input('Введите текст для обработки:\n')
            res2 = ''
            for i in s2:
                if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    res2 += i
                else:
                    if i.isalpha() and i.islower():
                        res2 += lower_eng_alphabet[(lower_eng_alphabet.find(i) - step) % eng]
                    elif i.isalpha() and i.isupper():
                        res2 += upper_eng_alphabet[(upper_eng_alphabet.find(i) - step) % eng]
            return res2

    elif language == 'РУС':
        rus = 32
        if direction == '1':
            s3 = input('Введите текст для обработки:\n')
            res3 = ''
            for i in s3:
                if i not in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                    res3 += i
                else:
                    if i.isalpha() and i.islower():
                        res3 += lower_rus_alphabet[(lower_rus_alphabet.find(i) + step) % rus]
                    elif i.isalpha() and i.isupper():
                        res3 += upper_rus_alphabet[(upper_rus_alphabet.find(i) + step) % rus]
            return res3

        elif direction == '2':
            s4 = input('Введите текст для обработки:\n')
            res4 = ''
            for i in s4:
                if i not in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                    res4 += i
                else:
                    if i.isalpha() and i.islower():
                        res4 += lower_rus_alphabet[(lower_rus_alphabet.find(i) - step) % rus]
                    elif i.isalpha() and i.isupper():
                        res4 += upper_rus_alphabet[(upper_rus_alphabet.find(i) - step) % rus]
            return res4


# Приветствуем пользователя и просим ввести данные для шифрования/дешифрования
print('''
Привет, я помогу тебе расшифровать или зашифровать сообшение с помощью "Шифра Цезаря"!''')
direction = input('''Выберите направление!\n(1) - Шифрование\n(2) - Дешиврование: \n''').lower()
language = input('Выберите язык!\n"рус" - (Русский)\n"анг" - (Английский): \n').upper()
step = int(input('Выберете шаг сдвига!\nНапишите цифру:\n'))

# Выводим результат, вызываем функцию с параметрами введенными пользователем
print('''
А вот и результат:''', do_cipher(direction, language, step))
