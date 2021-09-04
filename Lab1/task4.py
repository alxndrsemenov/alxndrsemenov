# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

#запрашиваем число у пользователя
usernumbern=int(input("Input number n: "))
lengthnumber=int((len(str(usernumbern))))
stringnum=str(usernumbern)


count=0
highest=0

#запускаем счетчик с 0 пока он меньше длины числа увеличиваем его на 1
while count < lengthnumber:
      #если текущий элемент списка больше нашего максимума, то присваиваем максимум текущему элементу списка
      if highest < int(stringnum[count]):
          highest = int(stringnum[count])
      count = count + 1
print("Highest number is: ",highest)