# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue=int(input("Please input revenue: "))
costs=int(input("Please input costs: "))

if revenue > costs:
    profit=revenue-costs
    print("Profit: ", profit)
else:
    loss=costs-revenue
    print("Loss: ",loss)

rent=profit/revenue
staffnum=int(input("Please staff number: "))
rentperonestaff=rent/staffnum
print("Rent per 1 staff: ", rentperonestaff)