# "staticmethod"
# # no self no cls

# class bank:
#   @staticmethod
#   def create_acc():
#     print("static method")

# bank.create_acc()

# obj = bank()
# obj.create_acc()


# class cal:
#   @staticmethod

#   def add(a,b,c):
#     print(a+b+c)

# cal.add(1,2,3)


# "local variables"
# class emp:
#   def __init__(slef):
#     names = 'vinay'
#     fname = 'tharaka'
  
#   def name(self):
#     print(self.name)
  
#   @classmethod
#   def cls_method(cls):
#     emp_salary = 60000
#     print(emp_salary)

#   @staticmethod
#   def static_method():
#     emp_dept='sales'



# obj = emp()
# obj.name()

# emp.cls_method()


# "super"

# class parent:
#   def __init__(self):
#     print("this is parent constructor")

# class child(parent):
#   def __init__(self):
#     super().__init__()
#     print("this is child constructor")

# obj = child()
# # obj2 = parent()


# class bank:
#   def __init__(self,acc_no):
#     self.acc_no = acc_no
#     acc_no = 12

# class sbi(bank):
#   def __init__(self,bank_name,v):
#     self.bank_name = bank_name
#     print('bank name: ',self.bank_name)
#     super().__init__(v)
#     print('acc no: ',self.acc_no)


# obj = sbi('sbi',12)


class school:
  def __init__(self,schl_name,year):
    self.schl_name = schl_name
    self.year = year

class student(school):
  def __init__(self,std_name,std_roll,name,yr):
    self.std = std_name
    self.roll = std_roll
    super().__init__(name,yr)
    print(f" from super: {self.schl_name} from present class: {name}")
    print(self.year,yr)
  
  def method(self):
    print(self.std)
    print(self.schl_name)
    print(self.year)
    print(self.roll)

obj = student('vinay',87,'dav',2026)
obj.method()