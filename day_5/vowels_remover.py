

enter_word = input("please enter the word :").upper()

word_without_vowels = ""

for char in enter_word :

        if char == "A":
            continue
        elif char =="E":
            continue
        elif char =="I":
            continue
        elif char =="O":
            continue
        elif char =="U":
            continue
        else:
            word_without_vowels += char

print("Your final word is : ",word_without_vowels)
