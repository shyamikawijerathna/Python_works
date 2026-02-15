x=((((2**2)+(3**2))**(1/2)))

print(round(x,2))


#take two numbers as input and which one is the largest number

num_one=int(input("enter first number:"))
num_two=int(input("enter second number:"))

if num_one > num_two:
    print(f"number one is larger :{num_one}")
    if num_one % 2 == 0:
        print("number is even")
        if num_one % 4 == 0:
            print("Number can divide by 4")


    else:
        print("odd number")
elif num_two > num_one:
    print(f"number two is larger :{num_two}")
    if num_two % 2 == 0:

            print("number is even")

    else:
        print("odd number")

else:
    print("Numbers are equal")

#if its a even number check whether its divisible by 4



#if num1 is greater than num2 check whether the number is even or odd
















