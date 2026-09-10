#Rotating by k positions from left
k=int(input())
arr=[1,2,3,4,5,6]
arr1=arr[k:]+arr[:k]
print(arr1)