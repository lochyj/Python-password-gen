import random
import string

user = input('please enter the length of the password: ')

num = int(user)

ran = ''.join(random.choices(string.ascii_letters + string.digits, k = num))    
print('Your password is: ' + str(ran))
input()
