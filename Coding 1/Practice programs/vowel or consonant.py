def Alphabet(letter):
    print(f"The Entered character is {letter}")
    vowels=["a","e","i","o","u"]
    if letter.isdigit():
            print(f"Entered character is  Number")
            exit()
    print(type(letter))
    if letter.isalpha():
        if letter.lower() in vowels:
            return f"{letter} is a Vowel Sound"
        else:
            return f"{letter} is a Consonant Sound"
    else:
        return f"{letter} is not Alphabet"
print(Alphabet("A"))
print(Alphabet("b"))
print(Alphabet("e"))
print(Alphabet("9"))
