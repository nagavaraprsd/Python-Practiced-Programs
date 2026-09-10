def Age(age):
    print(f"The Voter's age is {age}")
    if age<18:
        return "Teenagers can't Vote \nNot Eligible for Voting\n"
    else:
        return "Eligible for Voting,You can moave on\n"
print(Age(10))
print(Age(18))
print(Age(29))