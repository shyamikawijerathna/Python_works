username = input("Enter your username :")
password = input(" Enter your password")

if username == "group 5 " and password == 123456:
    print("Login successfull...!!!")

    rows = int(input("Enter the number of rows :"))
    columns = int(input("Enter the number of columns :"))
    symbols = input("Enter the symbol :")

    for x in range(rows):
        for y in range(columns):
            print(symbols,end="")
            print()

else :
    print("access denied")
    exit()
