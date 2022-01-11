import random
import string

print('Welcome to Random Password Generator')
char = string.ascii_letters + string.digits

def pass_gen():
  while True:
    authVal = int(input('Specify length of password (8-26) : ')) 
    while authVal >= 8 and authVal < 27:
      print("Success!")
      break
    else:
      print('That is an invalid input, provide value between 8-26')
      continue
    break
  password = ''.join(random.sample(char, authVal))
  print("Your password is:", password)


pass_gen()