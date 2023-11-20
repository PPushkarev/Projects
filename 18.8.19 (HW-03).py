# Задание 18.8.19 (HW-03)

num_tickets = int(input("Введите количество билетов:"))
ages = []
for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя {i+1}: "))
    ages.append(age)
print("Введенные возраста посетителей:", ages)

price0 = 0
price1 = 990
price2 = 1390

total_cost = 0

for age in ages:
    if age <= 18:
        fprice = price0
    elif 18 < age <= 25:
        fprice = price1
    else:
        fprice = price2
    total_cost += fprice
    print(f"Ваша стоимость для посетителя {age}: {fprice} руб.")
if num_tickets >= 3:
    total_cost *= 0.9
    print("Скидка -10 %")
print(f"Общая стоимость для всех посетителей: {total_cost} руб.")