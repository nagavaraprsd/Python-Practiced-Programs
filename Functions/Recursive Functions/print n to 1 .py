#Write a recursive function to print numbers from N to 1.
def num(n):
    if n==0:
        return []
    return[n]+num(n-1)
print(num(10))