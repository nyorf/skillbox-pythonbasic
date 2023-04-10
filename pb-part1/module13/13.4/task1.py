def addCheck(budget, new_tax):
    if budget + new_tax > budget:
        return True
    else:
        return False

budget = float(input('Введите бюджет страны: '))
new_tax = float(input('Новые поступления (налог): '))

if addCheck(budget, new_tax):
    print('Результат: Бюджет увеличится')
else:
    print('Результат: Бюджет не изменится')