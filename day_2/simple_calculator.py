#take the first number as an input
#take the second number as an input
#check the operator which user want to perform

#then check for the operator with if condition and perform the calculator

x = float(input("enter first number :"))
y = float(input("enter second number :"))
operator=input(str("enter operator :"))

if operator == '+':
    print("addition result:",x+y)
elif operator == '-':
    print("reduction result:",x-y)
elif operator == '*':
    print("multiply result :",x*y)
if y==0:
    print("Can't Divide by 0 ")
elif operator == '/':
    print("Divide result :", x / y)
