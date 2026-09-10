def check():
    math=int(input("Enter the marks in the Mathematics\n"))
    phy=int(input("Enter the marks in the Physics\n"))
    che=int(input("Enter the marks in the Chemistry\n"))
    if 100>=math>=40 and 100>=phy>=40 and 100>=che>=40:
        return "Student Passed Examination"
    elif math>100 or phy>100 or che>100:
        return "Invalid Marks!! Please Re-Enter the Marks"
    else:
        return "Student Failed Examination"
print(check())
    