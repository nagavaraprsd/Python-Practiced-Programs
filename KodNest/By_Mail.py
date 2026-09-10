users = [
    {"name": "Amit", "email": "amit@onefin.in"},
    {"name": "Zara", "email": "zara@gmail.com"},
    {"name": "Sam", "email": "sam@onefin.in"}
]

for user in users:
    email=user["email"]
    if email.endswith("@onefin.in"):
        print(user["name"])