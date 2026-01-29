#Equality operator
a = 10
b = 20

print('check a equals to b',a==b)  # Equality operator
print('check if a does not equal to b', a!= b)  #inequality operator

print('check if a greator than b',a>b) #Greater than operator
print('check if a less than b',a<b) #less than operator
print('check if a is greater than or equal to b :',a>=b) #greater than or equal
print('check if a is less than or equal to b :',a<=b) # less than or equal


#exercise
#Take two numbers as input and check with all the operators

x=20
y=30
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

str_one=("kamal")
str_two=("amal")

print('check str_one equals to str_two :',str_one==str_two)  # Equality operator
print('check if str_one does not equal to str_two :', str_one!=str_two)  #inequality operator
print('check if str_one greator than str_two',str_one>str_two) #Greater than operator
print('check if str_one less than str_two',str_one<str_two) #less than operator
print('check if str_one is greater than or equal to str_two :',str_one>=str_two) #greater than or equal
print('check if str_one is less than or equal to str_two :',str_one<=str_two) # less than or equal



#write a program to check if a number is divisible by 5,if its divisible print

number=int(input(f"please enter number :"))
print("The number is divisiable by 0 ?:",number % 5 ==0)
