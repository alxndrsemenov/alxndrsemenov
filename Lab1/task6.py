# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.

firstdayrun=int(input("Input first day kilometres run: "))
reachdayrun=int(input("Input kilometres need to reach: "))

currentdayrun=firstdayrun
day=1

while currentdayrun < reachdayrun :
      currentdayrun = currentdayrun*1.1
      day=day+1
print("Day reached :",day)
