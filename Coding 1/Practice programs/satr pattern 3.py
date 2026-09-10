def pattern():
    n=int(input("Enter no of *'s at base\n"))
    pt=0
    for i in range(0,n):
        pt=" "*(n-i-1)+"*"*(i+1)
        print(pt)
pattern()