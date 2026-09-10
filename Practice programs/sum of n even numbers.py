n=int(input("Enter the number\n"))
total=0
list1=[]
for i in range(1,n+1):
    if i%2==0:
        list1.append(i)
        total+=i
print(f"The list of Even numbers are \n{list1}")
print(f"Sum of Even numbers btw 0 and {n} are \n{total}")