# class : it is the blue print of the object. contains ATTRIBUTES(variables) and METHODS(functions).
# object: it is the physical quantity of the class.

class employee:
  emp_id = 101
  emp_name = 'vinay'
  emp_salary = 25000

  def details(self):
    print(self.emp_id)
    print(self.emp_name)
    print(self.emp_salary)

vin = employee()

vin.details()

print('-----------------------------')

class employee:
  emp_id = 101
  emp_name = 'vinay'
  emp_salary = 25000

  def __init__(self):
    print(self.emp_id)
    print(self.emp_name)
    print(self.emp_salary)

employee()

print('-----------------------------')

# Constructer:  def __int__(self):

class students:
  def __init__(self):
    print("Constructor")

obj = students()

print('-----------------------------')

class Dog:
    def __init__(self, name):
        self.name = name 
        greeting = "Woof!" 

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy")
dog2 = Dog("Lucy")

dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Lucy says Woof!


print('-----------------------------')


class new:
   def __init__(vinay,emp_name,emp_salary):
      vinay.emp_name = emp_name
      vinay.emp_salary = emp_salary
      print(emp_salary)
      print(vinay.emp_salary)

   def emp(self):
      print(self.emp_name)
      print(self.emp_salary)

obj = new('vinay',1234)

obj.emp()
