# Задача 7. Стипендия
# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию и
# составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# Составьте программу расчета суммы денег, которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
educational_grant = int(input('Какая у вас стипендия? '))
expenses = int(input('А какие у вас расходы? '))
totalGrant = 0
totalExpenses = 0
for month in range(2, 12):
    totalExpenses += expenses
    totalGrant += educational_grant
    expenses = expenses + (expenses * 0.03)
remainingMoney = totalExpenses - totalGrant
print('У родителей нужно попросить', remainingMoney / 1, 'рублей.')