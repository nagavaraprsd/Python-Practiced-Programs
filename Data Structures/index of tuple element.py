# Find the index of an element in a tuple.
tup=(1,2,3,4)
x=int(input("Enter the element to find index:\n"))
if x in tup:
    print("index of element is",tup.index(x))
else:
    print("Element Not Found")