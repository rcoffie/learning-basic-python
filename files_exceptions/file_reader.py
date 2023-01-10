''' this opens the text file digits.txt and save it in memory as file_objects'''
with open('pi_digits.txt') as file_object: 
    '''' here we save the contents in file_objects as contents '''
    contents = file_object.read()
''' this print the content we saved in file_objects'''
print(contents.rstrip())



