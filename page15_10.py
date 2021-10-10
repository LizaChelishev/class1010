# insert a number (float / integer) and print the closest even integer
number = float(input('Enter a number: '))
closest_integer = number // 1
if closest_integer % 2 == 0:
    closest_even_integer = closest_integer + 2
else:
    closest_even_integer = closest_integer + 1

closest_even_integer = int(closest_even_integer)
print('The closest even integer for the number you chose is: ' + str(closest_even_integer))




