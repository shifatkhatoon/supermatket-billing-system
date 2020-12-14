from login import *
from os import system
def admin_menu():
    system('cls')
    print('Welcome To Admin Pannel')
    while True:
        print("Enter Your Choice")
        print("\n\n\t1. Register New User")
        print("\n\n\t2. Login Existing User")
        print("\n\n\t3. Exit")
        option = int(input())
        if option == 1:
            system('cls')
            signin()
        if option == 2:
            system('cls')
            login()
        else:
            break
