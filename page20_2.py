
grade = int(input('Enter your grade: '))
if grade < 55:
    verbal_evaluation = 'almost enough'
if 55 < income < 64 :
    verbal_evaluation = 'enough'
if 65 < income < 74:
    verbal_evaluation = 'almost good'
if 75 < income < 84:
    verbal_evaluation = 'good'
if 85 < income < 94:
    verbal_evaluation = 'very good'
if income > 95:
    verbal_evaluation = 'excellent!'

print('Your grade is: ' + str(verbal_evaluation))
