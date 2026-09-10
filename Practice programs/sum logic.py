a=input("Enter a 4 digit number\n")
list_1 = list(map(int, str(a)))
if len(list_1)!=4:
    print("Invalid Input!! Try Entering again a 4 didgit number")
    exit()
n=len(list_1)
for _ in list_1:
    if list_1[0]+list_1[1]==list_1[-1]+list_1[-2]:
        print(f"Sum of First two numbers and last two  in {a} numbers is equal")
        break
    else:
        print(f"Sum of First two numbers and last two  in {a} numbers is  not equal")
        break