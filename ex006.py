number = int(input('Type a number'))

print('Number {} '.format(number))
print('Double of {} is: {}'.format(number, (number * 2)))
print('Triple of {} is: {}'.format(number, (number * 3)))
print('Square root of {} is: {: .2f}'.format(number, (pow(number, (1/2)))))