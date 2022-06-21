''' Time to match your first pattern! The following example uses a match ...
case block to find the first name of a user by extracting it from a user data structure: 
'''

user = {
    "name":{
        "first": "Sam",
        "last": "Archibong"
    },
    "title": "Software Engineer"
}

# print(user)

# match user 
match user:
    case {"name" : {"first": first_name}}:
        pass
    
print(first_name)