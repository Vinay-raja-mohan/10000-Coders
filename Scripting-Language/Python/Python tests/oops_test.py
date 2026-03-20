'1. What is a method in Python?'
# a function written inside a class is called as a method.

'2. Instance method'
# a method which is declared using instance variables in it , the variable may be named as anything but frequently used as self to reduce confusion, but the method gets only called upon creating a object and classing the method using the object.

'3. Class method'
# a method which is declared using class variables, these variables can be declared anywhere in the class using class name and also by using a classmethod decorator and a cls variable, for calling these method we can direcctly use class name , there is no need of creating a object for this.

'4. Static method'
#  a static method is a method which is declared using a decorator called @staticmethod, the main difference between a method and a static method is we can directly call a static method using the calss name there is no need to create a seperate object for this.

'5. Difference between instance and class method.'
# instance method : 1. Uses no decorator
                #   2. Uses object to store a class
                #   3. Should always decalre a variable inside the instance method

# class method :    1. Uses decorators
              #     2. uses no object to store a class
              #     3. Variable can be decalred anywhere, outside and inside a method

'6. What is method overriding?'
# when ever a parent and child class have the same method name or a constructor or even a attribute , the attribute which is written at the last gets overridden, means it overwrites all the decalration of variables and method to that of the last one , in constrtors it might give an error too.

'8. Create class with instance method.'

class insititue():
  def _84r(self):
    self.python_tutor = 'ajay sir'
    self.html_tutor = 'basha sir'
  
  def details(self):
    print(self.python_tutor)
    print(self.html_tutor)

obj = insititue()
obj._84r()
obj.details()

'9. Create class with class method using @classmethod.'
class new():
  name = 'vinay'

  @classmethod
  def old(cls):
    cls.kotha = 'new'
    cls.patha = 'old'
    print(cls.kotha)
    print(cls.patha)
    print(cls.name)

new.old()

'10. Create static method using @staticmethod'
class static:
  
  @staticmethod
  def s_method():
    print('hello')

static.s_method()

'11. What happens if you don’t use super()?'
# is it ok to not use super if there is no same methods or constructors in the parent and the child class, but if there is a same method or constructor in the parent and the child class, then we should use a super .

'12. Can we access parent constructor without super()?'
# no

'13. Can abstract class contain normal methods?'
