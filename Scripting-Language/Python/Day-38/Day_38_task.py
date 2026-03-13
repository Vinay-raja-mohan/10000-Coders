# 1 Student
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
s=Student("Vinay",20,90)
print(s.name,s.age,s.marks)

# 2 Employee
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print(self.id,self.name,self.salary)
e=Employee(101,"Raj",50000)
e.display()

# 3 Car
class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
c=Car("Toyota","Fortuner",4000000)
print(c.brand,c.model,c.price)

# 4 Laptop
class Laptop:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
    def update_price(self,p):
        self.price=p
l=Laptop("Dell","16GB",70000)
l.update_price(65000)
print(l.price)

# 5 Book
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
b=Book("Python","Guido",500)
del b.price

# 6 College
class College:
    college_name="ACE Engineering College"
c1=College()
print(c1.college_name)
print(College.college_name)

# 7 BankAccount
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
b=BankAccount("Vinay",1000)
b.deposit(500)
print(b.balance)

# 8 Mobile
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def update_price(self,p):
        self.price=p
m=Mobile("Samsung",30000)
m.update_price(28000)
print(m.price)

# 9 Teacher
class Teacher:
    school_name="ABC School"
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name,Teacher.school_name)
t=Teacher("Ravi")
t.display()

# 10 Product
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def delete_price(self):
        del self.price
p=Product("Laptop",60000)
p.delete_price()

# 11 Employee company
class Employee2:
    company="TCS"
e1=Employee2()
e2=Employee2()
print(e1.company,e2.company)

# 12 Student classmethod
class Student2:
    school_name="ABC School"
    @classmethod
    def update_school(cls,name):
        cls.school_name=name
Student2.update_school("XYZ School")
print(Student2.school_name)

# 13 Bike
class Bike:
    category="Two Wheeler"
b1=Bike()
b2=Bike()
print(b1.category,b2.category)

# 14 Hospital
class Hospital:
    hospital_name="City Hospital"
    @classmethod
    def change_name(cls,name):
        cls.hospital_name=name
Hospital.change_name("Apollo")
print(Hospital.hospital_name)

# 15 Movie
class Movie:
    def __init__(self,name,hero,rating):
        self.name=name
        self.hero=hero
        self.rating=rating
    def display(self):
        print(self.name,self.hero,self.rating)
m1=Movie("RRR","RamCharan",9)
m1.display()

# 16 Course
class Course:
    platform="Online"
    @classmethod
    def update_platform(cls,p):
        cls.platform=p
Course.update_platform("Offline")
print(Course.platform)

# 17 Customer
class Customer:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def update_city(self,c):
        self.city=c
c=Customer("Vinay","Hyderabad")
c.update_city("Delhi")
print(c.city)

# 18 Company
class Company:
    location="Hyderabad"
del Company.location

# 19 Library
class Library:
    def __init__(self,book,author):
        self.book=book
        self.author=author
l=Library("Python","Guido")
del l.author

# 20 Vehicle
class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show(self):
        print(self.name,self.price)
    def update_price(self,p):
        self.price=p
    def delete_price(self):
        del self.price
v=Vehicle("Car",500000)
v.show()
v.update_price(450000)
v.delete_price()