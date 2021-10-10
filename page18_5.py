name = input('Enter a name: ')
income = int(input('Enter your income: '))
if income < 23000:
    income_after_taxes = income * 0.9
if 23000 < income < 46000 :
    income_after_taxes = income * 0.8
if 46000 < income < 120000:
    income_after_taxes = income * 0.7
if 120000 < income < 220000:
    income_after_taxes = income * 0.6
if income > 220000:
    income_after_taxes = income * 0.5

print('Your income after taxes is: ' + str(income_after_taxes))















