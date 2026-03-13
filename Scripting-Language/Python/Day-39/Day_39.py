# class bank:
#   balance = 25000

#   def __init__(self):
#     self.balance+= 25000

#   def new_method(self):
#     self.balance+=5000
#   @classmethod
#   def method(cls):
#     cls.balance += 10000

# obj = bank()
# obj.new_method()
# obj.method()
# print(obj.balance)
# print(bank.balance)


class bank:
  balance = 1000

  @classmethod
  def cls_method(cls):
    cls.balance += 500
  
  def method(self):
    self.balance += 20
    bank.balance += 10

print(bank.balance)
bank.cls_method()
print(bank.balance)


bank.cls_method()
print(bank.balance)

obj2 = bank()
obj2.method()
print(obj2.balance)
print(bank.balance)


bank.cls_method()
print(bank.balance)
print('-----')

obj3 = bank()
obj3.method()
print(obj3.balance)
print(bank.balance)



# deleting an class

class employee:
  emp_name= 'vinay'

  def __init__(self):
    self.emp_name= 'raj'
    del self.emp_name


obj = employee()
print(obj.emp_name)
print(employee.emp_name)









