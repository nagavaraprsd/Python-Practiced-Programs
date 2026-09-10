# Write a recursive function to find the sum of digits of a number.
def num1(num):
    num2=0
    if num==0:
        return 0
    num2=num%10
    num=num//10
    return num2+num1(num)
print(num1(509))