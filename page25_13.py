dig = int(input('Enter a one digit number: '))
x = int(input('Enter a number: '))
times_dig_in_x = 0
while x // dig != 0:
    x = x // dig
    times_dig_in_x += 1

print('Your number dig appears ' + str(times_dig_in_x) + ' times in your number X')







