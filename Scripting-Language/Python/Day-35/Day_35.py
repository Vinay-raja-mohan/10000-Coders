import random
import pyttsx3
import time

pas=''

a = int(input("Enter the no. of alpha: "))
for x in range(a):
  d = random.choice('abcdefghijklmnopqrstuvwxyz')
  pas+=d

num = int(input("enter the number of digits: "))
for y in range(num):
  n = random.choice('0123456789')
  pas += n

spl = int(input("Enter the no. of spl char: "))
for z in range(spl):
  m = random.choice('!@#$%^&*()][:;><.,')
  pas += m

print(pas)

pas=[]
a = int(input("Enter the no. of alpha: "))
pas +=random.choices('asdfghjkl',k=a)

num = int(input("enter the number of digits: "))
pas += random.choices('1234567890',k=num)

spl = int(input("Enter the no. of spl char: "))
pas += random.choices('!@#$%^&*)(',k=spl)


new_pass =''
for i in pas:
  new_pass += i
print(new_pass)

print(random.sample('python',k=5))

en = pyttsx3.init()
en.setProperty('rate',50)

voices = en.getProperty('voices')
en.setProperty('voice',voices[0].id)
en.say('aaaaaaaaaa')
en.runAndWait()


l = ['vinay','raj','mohan']
for x in l:
  en.say(x)
  time.sleep(3)
  en.runAndWait()