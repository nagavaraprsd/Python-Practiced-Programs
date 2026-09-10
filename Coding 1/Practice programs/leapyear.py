def Leap_Year(year):
    print(f"The Given Year is {year}")
    if(year%4==0 and year%100!=0 or year%400==0):
        return f"{year} is A Leap Year\n" 
    else:
        return f"{year} is not a Leap Year\n"
print(Leap_Year(2004))
print(Leap_Year(1986))
print(Leap_Year(2002))
print(Leap_Year(2000))
