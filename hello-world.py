# This is a simple hello world program

import pyinputplus as pyip

print('Hello, World!')
print('What is your name?')
name = pyip.inputStr()
print(f'Your name is {len(name) + 1} chracter long')
age = pyip.inputInt('What is your age?')
print(f'You will be {age + 1} next year')

