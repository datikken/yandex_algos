a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

y = a%2 + b%2 + c%2

if(y == 0 or y == 3):
    print('Win')
else:
    print('Fail')