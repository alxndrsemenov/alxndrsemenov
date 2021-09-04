# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

#запрашиваем число у пользователя
usernumbern=int(input("Input number n: "))

#удваиваем цифру складывая три числа в строку и превращаем ее в число
doublenumbern=int(str(usernumbern)+str(usernumbern))

#утраиваем цифру складывая три числа в строку и превращаем ее в число
tripplenumbern=int(str(usernumbern)+str(usernumbern)+str(usernumbern))

#cуммируем результат
sumofnumbersn=usernumbern+doublenumbern+tripplenumbern

print("Sum of entered numbers, one, double,tripple: ",sumofnumbersn)