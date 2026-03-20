"Abstraction"
# it hide the internal impelementation details and showing only essential features to the user , EX = ATM, Gearbox, Remote

# concrete class : it is a regular class

from abc import ABC,abstractmethod
class Bank(ABC):
  @abstractmethod
  def create_account(self):
    pass

  @abstractmethod
  def withdraw(self):
    pass

  @abstractmethod
  def check_balance(self):
    pass
###################################################
class union(Bank):
  def create_account(self):
    self.union_Holder = 'sai-Union'
    print(self.union_Holder)
  
  def withdraw(self):
    print('union 2000')

  def check_balance(self):
    print('union balance 25000')
###################################################
class sbi(Bank):
  def create_account(self):
    self.sbi_Holder = 'sai-Sbi'
    print(self.sbi_Holder)
  
  def withdraw(self):
    print('Sbi 2000')

  def check_balance(self):
    print('Sbi balance 20000')
  
obj = union()
obj.create_account()
obj.withdraw()
obj.check_balance()

obj_sbi = sbi()
obj_sbi.create_account()
obj_sbi.withdraw()
obj_sbi.check_balance()


import random

class BANK(ABC):

  @abstractmethod
  def create_account(self):
    pass


class SBI(BANK):

  Holder_Details = []

  def create_account(self):
    new_Holder = {}
    new_Holder['holder_name']=input('Enter Holder Name: ')
    new_Holder['Aadhar_num']=int(input('Enter Holder Aadhar Number: '))
    new_Holder['Mobile_num']=int(input("Enter Mobile Number: "))
    new_Holder['IFSC']= 'SBI01234'
    new_Holder['Account_num'] = random.randint(00000000000,999999999999999)

    n = input('Select Your Account(Savings/Zero): ').lower()

    while True:
      if n=='savings':
        s = int(input('The minimum deposit is 1000: '))
        if s >= 1000:
          new_Holder['balance'] = s
          break
        
        else:
          print('Please deposit 1000 Rupees/:')

      elif n=='zero':
        s = int(input('The minimum deposit is 500: '))
        if s >= 500:
          new_Holder['balance'] = s
          break
        
        else:
          print('Please deposit 500 Rupees/:')
    
    SBI.Holder_Details.append(new_Holder)

    print(SBI.Holder_Details)
  
obj = SBI()

while True:
  print('''
          1) create account
          2) exit
''')
  
  v = int(input("select options"))

  if v == 1:
    obj.create_account()
  
        



