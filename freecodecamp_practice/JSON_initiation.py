import json

data = '''{
    "name" : "Emilio",
    "phone" : {
        "type": "intl",
        "number" : "+34 666 666 666"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

input = '''[
    {
        "id": "001",
        "x" : "2",
        "name" : "Emilio"
    },
    {
        "id" : "002",
        "x" : "7",
        "name" : "Paco"
    }
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])