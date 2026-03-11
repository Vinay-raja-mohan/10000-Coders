# # updating a instance variable

# class employee:
#   def __init__(self):
#     self.emp_id = 101
  
#   def method(self):
#     print(self.emp_id)


# obj = employee()
# print(obj.emp_id)
# obj.emp_id+=1
# obj.method()


# # updating in a sub class

# class employee:
#   def __init__(self):
#     self.emp_id = 101
#     print(self.emp_id)
  
#   def method(self):
#     self.emp_id += 1
#     print(self.emp_id)

# class student(employee):

#   def update(self):
#     self.emp_id += 1
#     print('update id = ',self.emp_id)


# # obj = employee()
# # obj.method()
# obj2=student()
# obj2.update()


# # deleting the instace variable

# class student:
#   def __init__(self):
#     self.roll = 100
#     print(self.roll)

#   def dele(self):
#     del self.roll
#     print(self.roll)

# obj = student()
# del obj.roll
# obj.dele()


# class brother:
#   def __init__(self):
#     self.age = 10
#     print(self.age)


# class sister(brother):
#   def n_age(self):
#     del self.age

# obj = sister()
# obj.n_age()
# print(obj.age)



# # class method

# class bank:

#   def __init__(self):
#     self.ifsc = 'ifsc1203'
#   @classmethod
#   def create_account(cls):
#     cls.balance = 5000  # class variable

# obj = bank()
# obj.create_account()

# print(obj.__dict__)  # prints only self or instance variables

# print(bank.__dict__)  # prints classs atributes


# class variable declaration 
# inside class outside method


class employee:

  name = 'vinay'
  roll = '101'

  def method(self):
    self.naming='raj'
  
  @classmethod
  
  def classy(cls):
    cls.f_name = 'taraka'
    print(cls.f_name)


obj = employee()
employee.new_name = 'mohan'

employee.classy()
print(employee.__dict__)

