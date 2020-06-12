number = int(input('Type the number that u want to see the multiplication table: '))
c = 0;

while c < 10:
    c = c + 1;
    print('-' * 10)
    print('{} x {} = {} |'.format(number, c, (number * c)))
