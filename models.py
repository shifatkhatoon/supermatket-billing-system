from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_string = "postgres://postgres:dev@1234@localhost:5432/supermarket"

db = create_engine(db_string)
base = declarative_base()


class Department(base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String, nullable=False)
    products = relationship('Product', backref='department', lazy=True)


class Product(base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    discount = Column(Integer)  # percentage like 10% so the value will be 10
    count = Column(Integer)

    department_id = Column(Integer, ForeignKey('department.id'))


class Admin(base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True,index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Invoice(base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, index=True)
    invoice_date = Column(DateTime)
    tax = Column(Float)
    amount = Column(Float)
    customer_name = Column(String)
    customer_number = Column(String)


Session = sessionmaker(db)
session = Session()



# # Create
# doctor_strange = Film(title="Doctor Strange", director="Scott Derrickson", year="2016")
# session.add(doctor_strange)
# session.commit()
#
# # Read
# films = session.query(Film)
# for film in films:
#     print(film.title)
#
# # Update
# doctor_strange.title = "Some2016Film"
# session.commit()
#
# # Delete
# session.delete(doctor_strange)
# session.commit()
