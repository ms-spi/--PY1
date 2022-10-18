money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

cash = money_capital + salary # все деньги после 1-го месяца
while cash >= spend:
    month += 1
    cash -= spend
    cash += salary
    spend *= (1 + increase)

print(month)
