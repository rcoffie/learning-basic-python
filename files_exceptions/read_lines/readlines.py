filename = 'filename.txt'
with open(filename) as text_file:
    for file in text_file.readlines():
        print(file.rstrip())