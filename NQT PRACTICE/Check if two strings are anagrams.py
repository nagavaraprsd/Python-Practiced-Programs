s1=input().lower()
s2=input().lower()
if sorted(s1)==sorted(s2):
    print("Both are anagrams")
else:
    print("Both are Not Anagrams")