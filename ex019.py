import random

student1 = input('First student: ')
student2 = input('Second student: ')
student3 = input('Third student: ')
student4 = input('Fourth student: ')

students = [student1, student2, student3, student4]
print('The winner is {}'.format(random.choice(students)))