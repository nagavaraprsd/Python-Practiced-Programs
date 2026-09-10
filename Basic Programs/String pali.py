#String=list((map(str,input("Enter a String").split())))
String=list(input())
print(String)
s1=String[::-1]
print(s1)
if String==s1:
    print("Palindrome")
else:
    print("Not Palindrome")