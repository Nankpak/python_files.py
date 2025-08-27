def passwd_strength():
    number = 1,2,3,4,5,6,7,8,9,0
    if len(password) <= 6:
       print('weak password')
    elif len(password) >6 and len(password) <= 10:
       print('medium password')
    else:
          print('strong password')
password = input('enter your password ')
passwd_strength()
