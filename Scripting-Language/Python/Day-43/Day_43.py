'polymorphism'

# Duck typing

class sbi:
  def create_acc(self):
    print("SBI account created")
    
  def deposit(self):
    print('SBI money deposited')
  
  def check_balance(self):
    print("SBI balance checked")
  

class union:
  def create_acc(self):
    print("UNION account created")
    
  def deposit(self):
    print('UNION money deposited')
  
  def check_balance(self):
    print("UNION balance checked")


def bank_details(obj):
  obj.create_acc()
  obj.deposit()
  obj.check_balance()

u_obj = union()
bank_details(u_obj)

sbi_obj = sbi()
bank_details(sbi_obj)



################

class america():
  def capital(self):
    self.a_c=input("Enter america capital : ")
    print(self.a_c)
  
  def lang(self):
    a_l=input('Enter america language : ')
    print(a_l)
  
class india():
  def capital(self):
    self.i_c=input("enter india capital : ")
    print(self.i_c)
  
  def lang(self):
    self.i_l=input('enter india language : ')
    print(self.i_l)

def country(obj):
  obj.capital()
  obj.lang()

india_obj = india()
country(india_obj)

america_obj = america()
country(america_obj)

'default arg polymorphism'

def add(a, b=0, c=0):
    return a + b + c

print(add(5))        # 5
print(add(5, 10))    # 15
print(add(5, 10, 20))  # 35

# ####
class add1:
  def cal(self,*a):
    print(a)

obj = add1()

obj.cal(10,20,30)
obj.cal(101,22)