'''Count Vowels
Take a string input and count how many vowels
(a, e, i, o, u) are in it.'''
text=input("Enter the String \n").lower()
vowels="aeiou"
count=0
for i in text:
    if i in vowels:
        count+=1
print("no of Vowels are",count)