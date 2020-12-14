from ProductPage import *
from os import system
def AdminPage():
    system('cls')
    while True:
        print("Enter Your Choice")
        print("\n\n1. Add New Product")
        print("\n\n2. Display All Products")
        print("\n\n3. Modify Product")
        print("\n\n4. Delete Product")
        print("\n\n5. Product Page")
        print("\n\n6. Add Department")
        print("\n\n7. Exit")
        option= int(input())
        if option==1:
            addNewProduct()
        if option==2:
            displayProducts()
        if option==3:
            modifyProduct()
        if option==4:
            deleteProduct()
        if option==5:
            ProductPage()
        if option==7:
            break
        if option==6:
            ADDepartment()

