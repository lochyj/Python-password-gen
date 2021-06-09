import random  
import string  
user = input('please enter the length of the password: ')
num = int(user)
def specific_string(length):  
    sample_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#%^*-=[]"
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result)  
specific_string(num)  
input()