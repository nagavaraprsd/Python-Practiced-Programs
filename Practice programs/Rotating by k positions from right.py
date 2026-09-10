#Rotating k positions from right
k=int(input("Enter no of positions to shift"))
arr=[1,2,3,4,5,6]
arr1=arr[-k:]+arr[:-k]
print(arr1)