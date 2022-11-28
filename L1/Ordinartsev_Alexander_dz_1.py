# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих
# переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип
# и содержимое переменных.
# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).
# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
import subprocess
import locale


# Lesson 1. Task 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и
# содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

# представление в строковом формате
str_1 = 'разработка'
str_2 = 'сокет'
str_3 = 'декоратор'

# проверка типа и содержания переменных
print(type(str_1))
print(type(str_2))
print(type(str_3))
print(str_1)
print(str_2)
print(str_3)

# преобразование строкового представления в Unicode
str_1_bytes = str_1.encode('utf-8')
str_2_bytes = str_2.encode('utf-8')
str_3_bytes = str_3.encode('utf-8')
print(type(str_1_bytes))
print(type(str_2_bytes))
print(type(str_3_bytes))
print(str_1_bytes)
print(str_2_bytes)
print(str_3_bytes)

# Lesson 1. Task 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

# запись в байтовом типе без преобразования
str_1 = b'class'
str_2 = b'function'
str_3 = b'method'

# определение типа переменных
print(type(str_1))
print(type(str_2))
print(type(str_3))

# определение содержимого переменных
print(str_1)
print(str_2)
print(str_3)

# определение длины переменных
print(len(str_1))
print(len(str_2))
print(len(str_3))

# Lesson 1. Task 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
str_1 = b'attribute'
# str_2 выводит ошибку. Невозможно записать в байтовом коде. str_2 закомментирована, чтобы не появлялась ошибка
#str_2 = b'класс'
# str_3 выводит ошибку. Невозможно записать в байтовом коде. str_3 закомментирована, чтобы не появлялась ошибка
#str_3 = b'функция'
str_4 = b'type'
print(str_1)
print(str_2)
print(str_3)
print(str_4)

# Lesson 1. Task 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_1 = 'разработка'
str_2 = 'администрирование'
str_3 = 'protocol'
str_4 = 'standard'

str_1_bytes = str.encode(str_1, 'utf-8')
str_1_str = bytes.decode(str_1_bytes, 'utf-8')
print(str_1_bytes)
print(type(str_1_bytes))
print(str_1_str)
print(type(str_1_str))
str_2_bytes = str.encode(str_2, 'utf-8')
str_2_str = bytes.decode(str_2_bytes, 'utf-8')
print(str_2_bytes)
print(type(str_2_bytes))
print(str_2_str)
print(type(str_2_str))
str_3_bytes = str.encode(str_3, 'utf-8')
str_3_str = bytes.decode(str_3_bytes, 'utf-8')
print(str_3_bytes)
print(type(str_3_bytes))
print(str_3_str)
print(type(str_3_str))
str_4_bytes = str.encode(str_4, 'utf-8')
str_4_str = bytes.decode(str_4_bytes, 'utf-8')
print(str_4_bytes)
print(type(str_4_bytes))
print(str_4_str)
print(type(str_4_str))

# Lesson 1. Task 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
# тип на кириллице.

# ping веб-ресурса yandex.ru и преобразование в строку на кириллице.
args = ['ping', 'yandex.ru']
yandex_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in yandex_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    line2 = line.decode('utf-8')
    print(line2)

# ping веб-ресурса youtube.com и преобразование в строку на кириллице.
args2 = ['ping', 'youtube.com']
youtube_ping = subprocess.Popen(args2, stdout=subprocess.PIPE)

for line2 in youtube_ping.stdout:
    line2 = line2.decode('cp866').encode('utf-8')
    line3 = line2.decode('utf-8')
    print(line3)

# Lesson 1. Task 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

str_1 = "сетевое программирование"
str_2 = "сокет"
str_3 = "декоратор"

# Создание файла test_file.txt, его заполнение
f_n = open("test_file.txt", 'w', encoding='utf-8')
f_n.write(str_1 + "\n")
f_n.write(str_2 + "\n")
f_n.write(str_3)
f_n.close()

# Проверка кодировки по умолчанию
f_n_coding = locale.getpreferredencoding()
print(f_n_coding)

# Открытие файла в формате Unicode и вывод его содержимого.
with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')