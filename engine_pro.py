execution = False
print('''welcome, this car is an automatic car enter ON 
to start your car, Off is stop, type -help for more guide''')
car_owner = 'Bankat'.lower()
user_name = input("enter your username ").lower()
if user_name == car_owner:
   print(f"welcome Mr {user_name.upper()} the is yours!!!")
   print("type -help for more guide")
elif user_name == ('classB').lower():
   print(f'welcome {user_name.upper()} this car is for people!!!')
else:
   print(f'Hello Mr {user_name.upper()} i guess you are in classD, this car is not for you')
   quit()
isrunning = True
engine_on = False
while isrunning:
   command = input("enter command, (Q to exit) ").lower()
   if command == 'q':
      break
   if command == "on" and engine_on == False:
      print("starting lamborghini, the car is ON")
      engine_on = True
   elif command == "on" and engine_on:
     print("lamboghni is on already")
   elif command == "off" and engine_on == True:
      print('stopping lambor, the car is off')
      engine_on = False    
   elif command == "off" and engine_on == False:
     print("lamborghini has stop already")
   elif command == "-help":
     print(''' enter D to drive.
 enter ON to start your car
 enter OFF to stop
 enter R to reverse. 
 enter P to park.
 enter AC for air conditioner''')
     engine_on = True
   elif command == "r" and engine_on:
     print("lamborghini is reversing")
     
   elif command == "r" and engine_on == False:
     print('lambor is off cannot reverse')
     
   elif command == "d" and engine_on:
     print('Drive mood lambor is driving')
   elif command == "d" and engine_on == False:
     print('lambor is off cannot drive')
     
   elif command == "p" and engine_on:
     print("park mood, lamborghini is parking")
   elif command == "p" and engine_on == False:
     print("park mood already")
     
   elif command == "ac" and engine_on:
    print('Air conditioner mood enjoy yourself')
   elif command == 'ac' and engine_on == False:
    print("cannot engage Ac please on lamborghini first")
   else:
     print("invalid command")
