filename = 'pi_digits.txt'
with open(filename) as text_file:
    lines = text_file.readline()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))