import json

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

print(f'{type(json_file)=}\n{json_file = }')
print(f'{json_file["name"]=}')
print(f'{json_file["address"]["geo"]=}')
print(f'{json_file["email"]=}')

json_text = """
[
    {
        "userId": 1,
        "id": 9,
        "title": "nesciunt iure omnis dolorem tempora et accusantium",
        "body": "consectetur animi nesciunt iure dolore"
    },
    {
        "userId": 1,
        "id": 10,
        "title": "optio molestias id quia eum",
        "body": "quo et expedita modi cum officia vel magni"
    },
    {
        "userId": 2,
        "id": 11,
        "title": "et ea vero quia laudantium autem",
        "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
    },
    {
        "userId": 2,
        "id": 12,
        "title": "in quibusdam tempore odit est dolorem",
        "body": "praesentium quia et ea odit et ea voluptas et"
    }
]"""
print(f'{type(json_text)=}\n{json_text=}')
json_list = json.loads(json_text)
print(f'{type(json_list)=}\t{len(json_list)=}\n{json_list=}')
