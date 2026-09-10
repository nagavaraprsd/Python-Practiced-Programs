#Write a Python program to find the second highest number in a list
a = list(map(int, input("Enter numbers: ").split()))

first = max(a)
a.remove(first)
second = max(a)
print("Second highest number is:", second)