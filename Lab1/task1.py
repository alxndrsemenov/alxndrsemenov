#Lab1. Task1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
greetmsg = "Welcome to the SuperShop"
byemsg = "Good bye, have a nice day"

username=str(input("What is your name?: "))
usercity=str(input("What is your city?: "))

print(greetmsg, username + "from city:", usercity)

maxprice=int(input("Input max price: "))
minprice=int(input("Input min price: "))
itemprice=int(input("Item price: "))


if itemprice > maxprice:
    print("Price to high")
elif itemprice < minprice :
        print("Price too low")
else:
    print("Your item has been added to cart")