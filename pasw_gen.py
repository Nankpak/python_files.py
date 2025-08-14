import random
power_house = 'abcdefghi1234567891jk0HIJKLMNOPQRSTUVWXYZ@#$^&*()!?:;'
try:
  user_len = int(input('enter the length of your password '))
  password = ""
  for i in range(user_len):
     password = random.choice(power_house)
     print(password, end="")
except ValueError:
  print('length must be number not character')
