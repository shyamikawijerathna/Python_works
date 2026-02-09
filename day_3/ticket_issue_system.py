

    # Ticket issue program
    # if height is less than 1.2m can not enter
    # age less than 18y low 20% off
    # ahe higher than 60y  50%
    # ticket price rs.1000
while True:
    print("""Ticket counter application
             Height over 1.2 m
             Below 18 years - 20 % discount
             Over 60 Years  - 50 % discount""")

    height = float(input("Enter your height(m) :"))

    ticket = 1000

    if height >= 1.2:
        print("Height is sufficient...!!!")
    else:
        print("You can't enter")
        exit()

    age = int(input("Enter your age ( years) : "))
    if age < 18:
        discount_20 = ticket * 0.2
        print(f"your ticket price is :{ticket - discount_20}")

    elif age > 60:
        discount_50 = ticket * 0.5
        print(f"your ticket price is : {ticket - discount_50}")
    else:
        print(f"Your ticket price is : {ticket}")


    exit_program = input("Do you want to continue ( Y/N ) : ")

    if exit_program == 'n':
        exit()
