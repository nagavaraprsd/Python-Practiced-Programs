# s="Naga Vara Prasad"
# s=s.lower()
# a=list(s)
# v_count=0
# c_count=0
# vowels=['a','e','i','o','u']
# while ' ' in a:
#     a.remove(' ')
# for i in a:
#     if i in vowels:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)------> Over all Tc is O(n2)
s="Naga Vara Prasad"
v_count=0
c_count=0
for ch in s.lower():
    if ch.isalpha():
        if ch in 'aeiou':
            v_count+=1
        else:
            c_count+=1
print("Vowels=",v_count)
print("Consonants=",c_count)
#Overall TC is O(n)