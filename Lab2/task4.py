#  Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#  Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

#запрашиваем ввод строки
string=str(input("Введите строку: "))

#создаем список из строки используя в качестве разделителя - пробел
mylist=string.split(" ")

i=0
#проходим в цикле элементы списка и выводим их с новой строки, если элемент больше 10 символов печатаем первые 10
for i in range(len(mylist)):
    if (len(mylist[i])) <=10:print(f"Cтрока {i+1}: {mylist[i]}\n")
    if (len(mylist[i])) > 10:
        cutstr = mylist[i][0:10]
        print(f"Cтрока {i+1}: {cutstr}\n")
