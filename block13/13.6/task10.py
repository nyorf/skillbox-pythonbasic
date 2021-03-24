# K - коэффициент, S - сумма кредита, i - % ставка, n - срок

def payment(loan, term, interest):
    k = coefficient(term, interest)
    return loan * k - (loan * interest)


def coefficient(term, interest):
    nominator = interest * (1 + interest) ** term
    denominator = (1 + interest) ** term - 1
    return nominator / denominator


def calculations(loan, term, interest, finalyear):
    for year in range(1, finalyear + 1):
        interestPaid = loan * interest
        loanPaid = payment(loan, term, interest)
        print('Период:', year)
        print('Остаток долга на начало периода:', loan)
        print('Выплачено процентов:', interestPaid)
        print('Выплачено тела кредита:', loanPaid)
        loan -= loanPaid
        term -= 1
    return loan, term


loan = float(input('Введите сумму кредита: '))
term = int(input('На сколько лет выдан кредит? '))
interest = float(input('Сколько процентов годовых: ')) / 100

print('\n=========================\n')

loan, term = calculations(loan, term, interest, 3)

print('\n=========================\n')

additionalterm = int(input('На сколько лет продляется договор? '))
term += additionalterm
interest = float(input('Повышение ставки до: ')) / 100

loan, term = calculations(loan, term, interest, term)

print('\nОстаток долга:', loan)