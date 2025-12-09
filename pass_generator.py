#this is a basic python program to generate password
import random
import string
pass_len=0

while pass_len<=8:
    pass_len=int(input("Enter the length of password u want to generator: "))
    if pass_len<8:
        print("Lenght of password must be longer than 8 characters!!")
characters=string.ascii_letters + string.punctuation + string.digits
password_list=random.choices(characters,k=pass_len)
password="".join(password_list)
print(f"your generated password is{password}")



