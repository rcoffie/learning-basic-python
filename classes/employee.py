# class Employee:
#     ''' Class for employee data'''

#     def __init__(self, first, last, salary):
#         ''' Take attributes of employee first_name, last_name, and email'''
#         self.first = first
#         self.last = last 
#         self.salary = salary
#         self.email = first + '_' + last + '_' + '@company.com'


#     def detail(self):
#         ''' print employees details '''
#         return (f" hi {self.first.title()} {self.last.title()} we are going to pay you a salary of {self.salary}  ")


# emp_1 = Employee('martin', 'atongo', 2000)
# emp_2 = Employee('tomasi','andrew',4000)


# print(emp_1.detail())
# print(emp_1.email)
# print(emp_2.detail())
# print(emp_2.email)


# class Inheritance 


class Staff:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.email = first + '.' + last + '@email.com'
        self.pay = pay 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

class Developer(Staff):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    


staff_1 = Staff('Tumasi','John',8000)
staff_2 = Staff('Douglas','Boachie', 1000)

dev_1 = Developer('Kawaku','Ansah',9000, 'python')

print(dev_1.fullname())
print(dev_1.prog_lang)

print(staff_1.fullname())
