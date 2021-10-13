number = int(input('Enter a number: '))
opposite = 0 
while number > 0:
    opposite = opposite * 10 + (number % 10)
    number = number // 10 
  
   
print(f'The opposite number is: {opposite}')




