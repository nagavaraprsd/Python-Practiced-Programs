users = [
    {"name": "Amit", "age": 22},
    {"name": "Zara", "age": 17},
    {"name": "Sam", "age": 25}
]
for user in users:
    age=user["age"]
    if age>18:
        print(user["name"])