#Write a recursive function to find the factorial of a number
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(6))