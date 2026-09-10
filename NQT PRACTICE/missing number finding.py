arr=list(range(1,51))
arr.remove(20)
n=int(input())
if n*(n+1)//2==sum(arr):
    print("No Missing Number")
else:
    print("Missing Number is",int(n*(n+1)/2-sum(arr)))