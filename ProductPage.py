from models import Product,Department, session
from os import system
def ADDepartment():
    system('cls')
    print('Enter Name Of Department')
    name = input()
    departmentName=Department(name=name)
    session.add(departmentName)
    session.commit()

def  addNewProduct():
    departments = session.query(Department).all()
    print('\n Department List')
    print('\t Id \t\t Name')
    if departments:
        for department in departments:
            print('\n\t{}\t\t{}'.format(department.id, department.name))
        print("Enter The Product Details")
        print('\n Enter Departement Id')
        departmentId = int(input())
        print("\n Enter Name Of Product")
        name = input()
        print("\n Enter Price Of Product in Rupees")
        price = int(input())
        print("\n Enter Discount on Product only Value")
        discount = int(input())
        print("\n Enter Quantity Of Product")
        count = int(input())
        product=Product(name=name,price=price,discount=discount,count=count,department_id=departmentId)
        session.add(product)
        session.commit()
        print("Succes Fully Added")
    else:
        print("Please Enter Department")
        ADDepartment()


def displayProducts():
    system('cls')
    print("Product List")
    allProducts= session.query(Product).all()
    print('\n\tId\t\tName\t\tQunatity\t\tPrice\t\tDiscount\t\tDepartmentName')
    if allProducts:
        for product in allProducts:
            print('\n\t{}\t\t{}\t\t{}\t\t\t{}\t\t{}\t\t\t{}'.format(product.id,product.name,product.count,product.price,product.discount,product.department.name))
    else:
        print('Please Enter Products You Have No Product To Sale')
        addNewProduct()
def modifyProduct():
    system('cls')
    print("Modify Product")
    displayProducts()
    print("Enter id Of Product To Modify")
    ID = int(input())
    system('cls')
    singleProduct = session.query(Product).filter_by(id=ID)
    while True:
        print('Select To Update')
        print("\n1. Name")
        print("\n2. Quantity")
        print("\n3. Discount")
        print("\n4. Price")
        print("\n5. Department")
        print("\n6. Exit")
        option=int(input())
        if option==1:
            print("\n Enter Name")
            name=input()
            singleProduct.update({"name":name})
            session.commit()
            print('\n Update Sucessfully')
        if option==2:
            print("\n Enter Quantity")
            name=int(input())
            singleProduct.update({"count":name})
            session.commit()
            print('\n Update Sucessfully')
        if option==3:
            print("\n Enter Discount")
            name=int(input())
            singleProduct.update({"discount":name})
            session.commit()
            print('\n Update Sucessfully')
        if option==4:
            print("\n Enter Price")
            name=int(input())
            singleProduct.update({"price":name})
            session.commit()
            print('\n Update Sucessfully')
        if option==5:
            print("\n Enter Department")
            departments = session.query(Department).all()
            print('\n Department List')
            print('\t Id \t\t Name')
            if departments:
                for department in departments:
                    print('\n\t{}\t\t{}'.format(department.id, department.name))
                name = int(input())
                singleProduct.update({"department_id": name})
                session.commit()
                print('\n Update Sucessfully')
            else:
                print("Please Enter Department")
                ADDepartment()
        if option == 6:
            system('cls')
            break
def deleteProduct():
    system('cls')
    print("Delete Product")
    displayProducts()
    print("Enter The Id of Product You Wanna To Delete")
    ID =  int(input())
    singleProduct = session.query(Product).filter_by(id=ID)
    singleProduct.delete()
    session.commit()
    print("Sucess Fully Deleted")
def ProductPage():
    system('cls')
    displayProducts()
    print("Enter Id Of Product")
    ID=int(input())

    system('cls')
    singleProduct = session.query(Product).filter_by(id=ID).first()
    print("Product Page")
    print('\n\tId\t\tName\t\tQunatity\t\tPrice\t\tDiscount\t\tDepartmentName')
    print('\n\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}'.format(singleProduct.id,singleProduct.name,singleProduct.count,singleProduct.price,singleProduct.discount, singleProduct.department.name))