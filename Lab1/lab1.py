#task1
greetmsg = "Welcome to the SuperShop"
byemsg = "Good bye, have a good day"
price1 = 0
price2 = 0

print(greetmsg)
price1=input("Input max price")
if 5 <= price1 <15:
    print("We have following items for this price")
else:
    print("There is no items for this price")
