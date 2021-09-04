# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

#спросим время у пользователя в секундах
usertimesecs=int(input("Input time in seconds: "))

#вычислим оставшиеся часы
userhours= (usertimesecs // 3600)

#если часы больше 0, то вычислим остаток минут
if userhours > 0:
    userminutes = (usertimesecs - userhours*3600)//60
    countseconds = usertimesecs - userhours*3600 - userminutes*60

print(f"Current Time hh:mm:ss: {userhours}:{userminutes}:{countseconds}")

