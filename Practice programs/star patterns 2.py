def pattern():
    n=int(input("no of stars at Top\n"))
    pt=0
    pt1=[]
    for i in range(0,n):
        pt="*"*(n-i)
        print(pt)
        pt1.append(pt)
pattern()