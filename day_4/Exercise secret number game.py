#make secret code
#guess 03 attempts and game over
#too low and too high

secret_number = 7
attempts = 0
max_attempts = 3

print("secret Number Game...!!!")


while attempts < max_attempts:
    guess_number = int(input("Please Enter Your Guess Number : "))
    if guess_number == secret_number:
        print("Your are the winner...Congratulations !!!")
        break

    elif guess_number < secret_number :
        attempts += 1
        print(f"your number too low and attempts left : {max_attempts- attempts}")

    elif guess_number > secret_number :
        attempts += 1
        print(f"your number too high and attempts left : {max_attempts- attempts}")

else:
        print("Game over ...!!! you have used all attempts " )













