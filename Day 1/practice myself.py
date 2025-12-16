#declare three string variables
#print the variables in a single line


family_1=("Father")
family_2=("Mother")
family_3=("Son")

print(family_1,family_2,family_3) # with normal spaces

print(f"{family_1},{family_2},{family_3}") #formating

print(family_1+','+family_2+','+family_3) #concatinate

print(family_1,family_2,family_3,sep='@')# with separator

#print your name
#print your name 5 times using single print statement
#print dogs,cats,birds separated by "?"
#print the sentences in two different lines using single print statement
#declare three string variables
#print them using string formating
#declare str,int,boolean,float variables and print the types of the variables

print("Shyamika")
print("shyamika\n"*5)

print("Dogs","Cats","Birds",sep='?')

print("The train will be\n arrived at 8.30 p.m")

name=("shyamika")
age=36
is_male=True
weight=68.56

print(type(name))
print(type(age))
print(type(is_male))
print(type(weight))

print(name+'*'+str(age)+'Years')



