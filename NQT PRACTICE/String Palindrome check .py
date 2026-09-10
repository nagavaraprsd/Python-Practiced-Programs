a=input()
s=a.lower()
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")