from models import  session,Admin
from getpass import getpass
from AdminPage import *
from os import system
def signin():
    print('Enter Username')
    name = input()
    users = session.query(Admin)
    matchName = users.filter(Admin.username == name).first()
    if matchName:
        system('cls')
        print("User Name Exists")
        print("Enter A Valid User Name")
        signin()
    else:
        system('cls')
        print("Valid User Name")
        password = getpass('Password:')
        pass2 = getpass('Again Enter Password:')
        if password == pass2:
            admin = Admin(username=name, password=password)
            session.add(admin)
            session.commit()
        else:
            print('Enter Same Password')
            signin()
def login():
    print('Enter Your UserName')
    name=input()
    users = session.query(Admin)
    matchName = users.filter(Admin.username == name).first()
    if matchName:
        password = getpass('Password:')
        if matchName.password==password:
            system('cls')
            print('Welcome To Admin Panel')
            AdminPage()
        else:
            system('cls')
            print("Wrong Username Or Password......")
            login()
    else:
        system('cls')
        print('Enter A Valid User Name')
        login()


