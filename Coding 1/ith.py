'''FizzBuzz
Write a program that prints numbers from 1 to 30. For multiples of 3, print “Fizz” instead of the number,
for multiples of 5 print “Buzz,”
and for multiples of both 3 and 5, print “FizzBuzz.”'''
'''Fuzz = []
Buzz = []
FuzzBuzz = []

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        FuzzBuzz.append(i)
    elif i % 3 == 0:
        Fuzz.append(i)
    elif i % 5 == 0:
        Buzz.append(i)

print("Fuzz (multiples of 3):", Fuzz)
print("Buzz (multiples of 5):", Buzz)
print("FuzzBuzz (multiples of 3 and 5):", FuzzBuzz)'''
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
