# insert a number between 1-9999 and print how many digits is it
number = int(input('Enter a number between 1 and 9999: '))
number_of_digits = 0
while 1 < number < 9999:
    if number // 10 != 0:
        number_of_digits += 1
    number == number // 10

print("The number of digits is: " + str(number_of_digits))













