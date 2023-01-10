# writing file
# filename = 'programming.txt'
# with open(filename, 'w') as text_file:
#     text_file.write('i love programming')



# appednig mode

filename = 'programming.txt'

with open(filename, 'a') as text_file:
    text_file.write('i love python. \n')
    text_file.write('django is the best web framework for python especially for large projects. \n')
    text_file.write('fastAPI is the best option for building apis for small python applications. \n')
    text_file.write('python ML with python web frameworks is the best  combo. \n')
