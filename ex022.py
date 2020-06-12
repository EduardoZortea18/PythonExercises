name = str(input('Type your full name: ')).strip()
'''.strip elimina os whitespaces antes e depois'''

print('Your name in upper case: {}'.format(name.upper()))
print('Your name in lower case: {}'.format(name.lower()))
print('Your name has: {} letters'.format(len(name)-(name.count(' '))))
splitName = name.split()
print('Your first name is {} and it has {} letters'.format(splitName[0], len(splitName[0])))