# "inheritance"
# if one class extends another class
# it is a feature in the oops where a child class ingerits the prop and behaviour of the parent. 

# single inheritance :- a child class inherits from one parent class
# multiple inheritance:- a child class inherits from multiple parent class
# multilevel inheritance:- a child inherits from a parent, another child inhertis from that child.
# hiearchial inheritance:- multiple child classes inherit from the same parent class.
# hybrid inheritance:- loops d-a-b-c-d


'single inheritance'
class school:
  def __init__(self):
    self.schl_name = input("Enter schl name: ")
    self.schl_id = int(input("Enter schl id: "))
    self.schl_loc = input("Enter schl location: ")
  
  def details(self):
    print("name: ",self.schl_name)
    print("id: ",self.schl_id)
    print("loc: ",self.schl_loc)

class hm(school):
  def __init__(self):
    self.hm_name = input("Enter hm name: ")
    self.hm_no = int(input("Enter the mobile number: "))
    self.hm_salary = int(input("Enter the salary: "))

    super().__init__()

  def hm_details(self):
    print("name: ",self.hm_name)
    print("mobile no: ",self.hm_no)
    print("salary :",self.hm_salary)


obj = hm()
obj.details()
obj.hm_details()

"multiple inheritance"

class parent1:
  def __init__(self):
    self.p1_name = "sai"
    self.p1_age = 56

class parent2:
  def parent_method(self):
    self.p2_name= 'venkat'
    self.p2_age = 40

    

class child(parent1,parent2):
  def child_method(self):
    self.ch_name = 'tharak'
    self.ch_age = 20
  
  def details(self):
    print("parent 1 name: ",self.p1_name)
    print("parent 1 age: ",self.p1_age)
    print()
    print("parent 2 name: ",self.p2_name)
    print("parent 2 age: ",self.p2_age)
    print()
    print("child name: ",self.ch_name)
    print("child age: ",self.ch_age)

obj = child()
obj.parent_method()
obj.child_method()
obj.details()

"Multilevel inheritance"

class grandfather:
  def __init__(self):
    self.gf_name= 'thata'
    self.gf_age = 99

class father(grandfather):
  def __init__(self):
    self.f_name = "naana"
    self.f_age = 55
    super().__init__()

class son(father):
  def __init__(self):
    self.s_name = "koduku"
    self.s_age = 18
    super().__init__()

  def genes(self):
    print(f"Grand father name: {self.gf_name}, age : {self.gf_age}")
    print(f"Fathers name : {self.f_name}, age: {self.f_age}")
    print(f"Sons name: {self.s_name}, age: {self.s_age}")

obj = son()
obj.genes()


"hierarchical inheritance"
class office:
  def __init__(self):
    self.officer1 = 'first person'
    self.officer2 = 'second person'
    self.officer3 = 'third person'

class officer1(office):
  def __init__(self):
    super().__init__()
    self.officer1_age = 1
    print("first officer: ",self.officer1)
    print("first officer: ",self.officer1_age)
    

class officer2(office):
  def __init__(self):
    super().__init__()
    self.officer2_age = 2
    print("Second officer: ",self.officer2)
    print("Second officer: ",self.officer2_age)
    

class officer3(office):
  def __init__(self):
    super().__init__()
    self.officer3_age = 3
    print("Third officer: ",self.officer3)
    print("Third officer: ",self.officer3_age)

obj1 = officer1()
obj2 = officer2()
obj3 = officer3()


"Hybrid inheritance"
class a(b):
  def __init__(self):
    super().__init__()
    print("this is a method 'A'")

class b(c):
  def __init__(self):
    super().__init__()
    print("this is method 'B'")

class c(d):
  def __init__(self):
    super().__init__()
    print("this is method 'C'")

class d(a):
  def __init__(self):
    super().__init__()
    print("this is method 'D'")


    








# bank class , method declare create_acc, folder_name, mobile_no, aadar_name, ifsc=default ivali, account_number generate, type of account(ask user), if saving = deposit 1k, and then check if user deposited 1k or not, 0 account selected then 500 depo, use key and value ie dict.