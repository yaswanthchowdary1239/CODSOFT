import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="{}?@!$%^&*()_+*"
all=lower+upper+numbers+symbols
print("Wecome to password generator:")
length=int(input("Enter the length of the password :" ))
password="".join(random.sample(all,length))
print(password)