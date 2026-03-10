# # instance variable

# class student:
#   def __init__(self):
#     self.std_id = int(input('Enter Student id: '))
#     self.std_name = input("Enter Student Name: ")

#   def vinay(vinay):
#     print(vinay.std_id)

# obj = student()
# obj.vinay()

# print(obj.std_name)

# obj2 = student()
# obj2.vinay()

# print(obj2.std_name)



# # inside constructor

# class bank:
#   def __init__(self):
#     self.holder_name = 'hari'
#     self.mobile = 9287654321
#     self.acc_num = 12342123456789
#     self.IFSC = 'IFSC01234'

#   def stud(self):
#     self.name='vinay'

# obj = bank()
# obj.stud()
# obj.middle_name='raj'
# print(obj.__dict__)


# printing

# inside constructor
class employee:
  def __init__(self):
    self.emp_id = 101
    self.emp_name = 'hari'

    print(self.emp_id)
    print(self.emp_name)
  
  def vinay(vinay):
    print(vinay.emp_id)
    print(vinay.emp_name)

  
obj = employee()
obj.vinay()
