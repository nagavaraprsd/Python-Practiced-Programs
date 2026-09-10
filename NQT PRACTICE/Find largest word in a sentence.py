s="Naga Vara Prasad"
a=s.split()
# max_len=0
# for word in a:
#     if len(word)>max_len:
#         max_len=len(word)
# print(max_len)#if length is asked
max_word=a[0]
for word in a:
    if len(word)>len(max_word):
        max_word=word
print(max_word)