with open('dummy.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())