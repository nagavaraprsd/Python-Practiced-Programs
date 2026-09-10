# f=open("demo.txt","w")
# f.write("Hello World")
# f.close()
# f=open("demo.txt","r")
# print(f.read())
# f=open("demo.txt","w")
# f.write("Hello World")
# f.close()
# f=open("demo.txt","a")
# f.write("\nThis is vara Prasad")
# f.close()
# with open("demo.txt","r") as f:
#     print(f.read())
# file = open(r"D:\Luffy_Zoro_Sanjii\File Handling\demo1.txt", "x")
# file.close()#---> Creating aa file in a specific folder using a path and giving a new name of file at the end like '\demo1.txt'

# To print no of words in file 
# with open("demo.txt","r") as file:
#     data=file.read()
# words=data.split()
# print("No of words = ",len(words))
# file.close()

# To print no of lines in file 
# with open("demo.txt","r") as file:
#     data=file.read()
# lines=data.splitlines()  #---> instead of line 26 and 27 we can use like 'lines=file.readlines()'
# print("No of lines = ",len(lines))
# file.close()

# To print only uppercase charscters
# with open("demo.txt","r") as file:
#     data=file.read()
# for word in data:
#     if word.isupper():
#         print(word,end="")
# file.close()

