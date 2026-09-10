def Leap_Year():
    year=int(input("Enter the Year\n"))
    print(f"The Given Year is {year}")
    if(year%4==0 and year%100!=0):
        return f"{year} is A Leap Year but not Century Year\n" 
    elif year%400==0:
        return f"{year} is Century Year and Leap Year "
    else:
        return f"{year} is not a Leap Year\n"
print(Leap_Year())