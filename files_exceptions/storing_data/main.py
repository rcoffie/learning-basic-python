import json 

# f = open('test.json')

# data = json.load(f)


# for i in data:
#     print(i)

filename = 'test.json'

with open(filename) as f:
    data = json.load(f)

for i in data:
    print(i)