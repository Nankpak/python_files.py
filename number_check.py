def number():
    if number_check %2 == 0:
       print(f'{number_check} is an even number')
    else:
       print(f'{number_check} is an odd number')
try:
   number_check = int(input('enter your number '))
   number()
except ValueError:
   print('input must be integer not character')
