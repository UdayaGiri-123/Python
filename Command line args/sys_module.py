import sys
def addition(num1, num2):
	add = num1+num2
	print(add)

def substraction(num1,num2):
	sub = num1 - num2
	print(sub)

num1 = sys.argv[1]
operation = sys.argv[2]
num2 = sys.argv[3]

if(operation == "add"):
output = addition(num1,num2)
print(output)

elif(operation == "sub"):
output = substraction(num1,num2)
print(output)