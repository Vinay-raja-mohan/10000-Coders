# *Part 1: Class Variable Tasks* 
# 1.	Create a class Student with a class variable school_name. Print the school name using an object.
class Student:
  schl_name = 'abc'

obj = Student()
print(obj.schl_name)

# 2.	Create a class Employee with class variable company = "TCS". Create 3 objects and print the company name using each object.
class Employee:
  company = 'TCS'
obj1 = Employee()
obj2 = Employee()
obj3 = Employee()
print(obj1.company," ",obj2.company," ",obj3.company)

# 3.	Create a class Car with class variable wheels = 4. Print the wheels value using class name and object name.
class Car:
  wheels = 4
obj = Car()
print(obj.wheels," ",Car.wheels)

# 4.	Create a class Laptop with class variable brand = "HP". Change the value of brand using class name and print it.
class laptop:
  brand='HP'
laptop.brand = 'MSI'
print(laptop.brand)

# 5.	Create a class Book with class variable category = "Education". Create 2 objects and display the category.
class Book:
  category = 'Education'
obj1 = Book()
obj2 = Book()
print(obj1.category,' ',obj2.category)

# 6.	Create a class College with class variable college_name. Update the college name and print it for all objects.
class College:
  college_name = ''
College.college_name = 'new college'
print(College.college_name)

# 7.	Create a class Mobile with class variable country = "India". Print the variable using class name.
class mobile:
  country = 'India'
print(mobile.country)

# 8.	Create a class Teacher with class variable subject = "Python". Change the subject using an object and observe the output.
class teacher:
  subject = 'Python'
obj = teacher
obj.subject = 'Java'
print(obj.subject)

# 9.	Create a class Bank with class variable bank_name = "SBI". Print the bank name using both class and object.
class bank:
  bank_name = 'SBI'
obj = bank()
print(obj.bank_name,' ',bank.bank_name)

# 10.	Create a class Animal with class variable type = "Mammal". Create multiple objects and print the type.
class animal:
  type = 'mamma;'
obj1 = animal()
obj2 = animal()
obj3 = animal()
print(obj1.type,' ',obj2.type,' ',obj3.type)

# ________________________________________
# *Part 2: Class Method Tasks*
# 11.	Create a class Student with class variable school_name. Create a class method to change the school name.
class student:
  schl_name = 'abc'
  @classmethod
  def cls_method(cls):
    cls.schl_name = 'cba'
obj = student()
obj.cls_method()
print(student.schl_name)

# 12.	Create a class Employee with class variable company. Write a class method to update the company name.
class employee:
  company= 'amazon'
  @classmethod
  def cls_method(cls):
    cls.company = 'google'
employee.cls_method()
print(employee.company)

# 13.	Create a class Car with class variable wheels. Write a class method to modify wheels.
class car:
    wheels = 4
    @classmethod
    def cls_method(cls):
        cls.wheels = 6
car.cls_method()
print(car.wheels)

# 14.	Create a class Book with class variable library_name. Use a class method to update the library name.
class book:
    library_name = "central library"
    @classmethod
    def cls_method(cls):
        cls.library_name = "city library"
book.cls_method()
print(book.library_name)

# 15.	Create a class Laptop with class variable brand. Write a class method to change the brand.
class laptop:
    brand = "dell"
    @classmethod
    def cls_method(cls):
        cls.brand = "hp"
laptop.cls_method()
print(laptop.brand)

# 16.	Create a class College with class variable college_name. Use class method to print the college name.
class college:
    college_name = "ACE Engineering College"
    @classmethod
    def cls_method(cls):
        print(cls.college_name)
college.cls_method()

# 17.	Create a class Mobile with class variable country. Create a class method to update the country name.
class mobile:
    country = "india"
    @classmethod
    def cls_method(cls):
        cls.country = "usa"
mobile.cls_method()
print(mobile.country)

# 18.	Create a class Bank with class variable bank_name. Create a class method to change bank name.
class bank:
    bank_name = "sbi"
    @classmethod
    def cls_method(cls):
        cls.bank_name = "hdfc"
bank.cls_method()
print(bank.bank_name)

# 19.	Create a class Hospital with class variable hospital_name. Use class method to update the hospital name.
class hospital:
    hospital_name = "city hospital"
    @classmethod
    def cls_method(cls):
        cls.hospital_name = "apollo hospital"
hospital.cls_method()
print(hospital.hospital_name)

# 20.	Create a class Company with class variable location. Write a class method to change the location and print it.
class company:
    location = "hyderabad"
    @classmethod
    def cls_method(cls):
        cls.location = "bangalore"
        print(cls.location)
company.cls_method()
