word=input("Enter the words or letters seperated by space \n")

word_s=word.split()
word_count={}
for word in word_s:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
for word,count in word_count.items():
    print(f"{word}:{count}")