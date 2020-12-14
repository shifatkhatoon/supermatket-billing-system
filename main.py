from os import system
from models import Product, Department, Invoice, session,Admin
from getpass import getpass
from adminMenu import *
#
# create_dept = Department(name="Cosmetic")
# session.add(create_dept)
# session.commit()
#
# vaseline = Product(
#     name="Vaseline",
#     price=100,
#     discount=0,
#     count=20,
#     department_id=create_dept.id
# )
#
# session.add(vaseline)
# session.commit()
products = session.query(Product)

def generate_invoice(data):
    total = 0
    print("\n\n********************************INVOICE************************\n")

    print("\tItem\t\tQuantity\tPrice \tAmount \t\tAmount after discount\n")
    for id in data:
        pr = products.filter_by(id=id).first()
        amt = data[id] * pr.price
        damt = amt - amt * (pr.discount / 100)
        print("\t{}\t\t{}\t{} \t{} \t\t{}".format(pr.name, data[id], pr.price, amt, damt))
        total+=damt
    print("\n\n\t\t\t\t\t\t\t\t\t\t Total:= Rs. ",total)

def show_products():
    print("\n\n\t\tSelect Items\n\n")

    print("========================================================================\n")
    print("P.NO.\t\tNAME\t\t\t\tPRICE\t\tDiscount\n")
    print("========================================================================\n")

    for product in products:
        print("{}\t\t{}\t\t\t{}\t\t{}%".format(product.id, product.name, str(product.price), product.discount))

def customer_menu():
    show_products()
    print("\n======================================================")
    print("\n\t\t\t\t\t\t Place Order")
    print("\n======================================================")
    more = 'y'
    data = {}
    while more == 'y':
        p_no = int(input("\n\n Enter the P.NO. of the Item:\t"))
        if not products.filter_by(id=p_no).first():
            print("Enter valid product id")
            continue
        count = int(input("\n\n How many units? :\t"))
        data[p_no] = count
        more = str(input("Do You Want To Order Another Product ? (y/n)")).strip()
        more = more
        pass
    print(data)
    print("\n======================================================")
    input("Thank you for shopping press enter to generate Invoice: ")
    system('clear')
    generate_invoice(data)




def show_intro():
    print("\n\n\n\t\t\t\t\t Welcome to Supermarket Billing \n\t\t\t\t\t Press Enter key to enter!!")

    print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tMade by: Shifat ")

    input()


if __name__ == "__main__":
    show_intro()
    while True:
        system('cls')
        print("\n\n\n\tSelect your kind")
        print("\n\n\t1. Customer")
        print("\n\n\t2. Admin")
        print("\n\n\t3. Exit")
        print("\n\n\tPlease select an option(1-3)")
        option = int(input())
        if option == 1:
            system('cls')
            customer_menu()
        if option == 2:
            admin_menu()
        else:
            break
