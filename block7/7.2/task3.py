winners = 0
for ticket in 345, 19, 87, 1020, 421:
    if 1 <= ticket // 100 < 10 and ticket % 5 == 0:
        print(ticket, '- счастливый')
        winners += 1
print('Всего победителей -', winners)