correct_pin = 7732
count = 0
isrunning = True
while isrunning:
   user_input = int(input('enter your pin '))
   count += 1
   if count < 3:
      if user_input == correct_pin:
         print('Access granted')
         isrunning = False
      else:
         print('Access Denied')
   else:
     print('card block you try', count,'times')
     isrunning = False
