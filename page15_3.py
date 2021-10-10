# v= pi*r^2*h
height = int(input('Insert the height of a pot: '))
radius = float(input('Insert the radius of the base of the pot: '))
pi = 3.14
if radius and height > 0:
    v = (radius ** 2) * pi * height
    print('The volume of the pot is: ' + str(v))
