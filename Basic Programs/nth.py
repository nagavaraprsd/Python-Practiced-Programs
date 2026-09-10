'''s=input("Enter the string \n").lower().replace(" ","")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome") alternative and advance one to check punchuvation marks also
    '''

s=input("Enter the string \n").lower()
clean_s="".join(char for char in s if char.isalnum())
if clean_s==clean_s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
