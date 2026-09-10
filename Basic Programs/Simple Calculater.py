sum=0
difference=0
product=0
divide=0
choice=int(input("""
                    1.Addition 
                    2.Substraction
                    3.Multiplication
                    4.division
                    5.To Exit
Enter your Choice number\n """))
choices=[1,2,3,4,5]
if choice not in choices:
    print("Invalid Input or Re Enter the correct Choice")
    exit()
if choice==1:
    print(f"You chose Addition")
elif choice==2:
    print(f"You chose Substraction" )
elif choice==3:
    print(f"You chose Multiplication")
elif choice==4:
    print(f"You chose Division")
elif choice==5:
    exit()
a=input("Enter the First Number\n")
if a.lstrip('-').isdigit()==False:
    print("Invalid Input")
    exit()
b=input("Enter the Second Number\n")
if b.lstrip('-').isdigit()==False:
    print("Invalid Input")
    exit()
a=int(a)
b=int(b)
if choice==1:
    sum=a+b
    print(f"Addition is {sum}")
elif choice==2:
    if a<b:
        difference=b-a
    else:
        difference=a-b
    print(f"difference is {difference}")
elif choice==3:
    product=a*b
    print(f"Multiplication is {product}")
elif choice==4:
    if b==0:
        exit()
    divide=a/b
    print(f"Division is {divide}")