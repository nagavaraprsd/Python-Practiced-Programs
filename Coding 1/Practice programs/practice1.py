def check(num):
    if num==0:
        return "Number is Zero"
    elif num<0:
        return "Number is Negative"
    else:
        return "Number is Positive"
print(check(6))
print(check(0))
print(check(-5))