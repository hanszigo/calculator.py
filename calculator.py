def mul(x,y):
	return x *y

def raise_to_power(x,y):
	return x **y

def div(x,y):
	return x/y

def base_div(x,y):
	return x // y

def modulos(x,y):
	return x % y
	
def add(x,y):
	return x + y

def sub(x,y):
	return x - y
	

x = ("calculator")
print(x.upper())

y = "enter a number and calculate it with another number"
print(y.upper())


num1 = int(input())
op = input()
num2 = int(input())



if op == "*":
		print(mul(num1,num2))
		if num1 == 0 or num2 == 0:
			raise Exception("zerro erro multiplaction")
	

if op == "**":
	print(raise_to_power(num1,num2))
	if num1 == 0 or num2 == 0:
			raise Exception("zerro erro multiplacation")
			
if op == "/":
	print(div(num1,num2))
	if num1 == 0 or num2 == 0:
			raise Exception("zerro erro division")
	

if op == "//":
	print(base_div(num1,num2))
	if num1 == 0 or num2 == 0:
			raise Exception("zerro erro division")

if op == "%":
	print(modulos(num1,num2))
	if num1 == 0 or num2 == 0:
			raise Exception("zerro erro division")

if op == "+":
	print(add(num1,num2))
	if num1 == 0 or num2 == 0:
		raise Exception("zerro erro addition")

if op == "-" :
	print(sub(num1,num2))
	if num1 == 0 or num2 == 0:
			raise Exception("zerro erro subtraction")
		
		

