#10 PYTHON TIPS AND TRICKS FOR WRITING PYTHONIC CODE 

#1)TERNARY CONDITIONALS

condition = True 

if condition: 
	x = 1 
else: 
	x = 0 

print(x)

condition = True

x - 1 if condition else 0 

#2)UNDERSCORE PLACEHOLDERS

print(x)

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'{total:,}')

#3)CONTEXT MANAGERS 

f = open()