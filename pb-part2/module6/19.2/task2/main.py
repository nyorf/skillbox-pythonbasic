incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

total_income = sum(incomes.values())
lowest_income_value = min(incomes.values())
lowest_income_name = list(incomes.keys())[list(incomes.values()).index(lowest_income_value)]
incomes.pop(lowest_income_name)

print('Общий доход за год составил: {}'.format(total_income))
print('Самый маленький доход у {item}. Он составляет {income} рублей.'.format(
    item = lowest_income_name,
    income = lowest_income_value
))
print('Итоговый словарь: {}'.format(incomes))
