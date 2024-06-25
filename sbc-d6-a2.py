r = int(input("Enter the number of rows for the pattern: "))
c = int(input("Enter the number of rows for the pattern: "))

row = 1
column = 1

while row <= r:
    if row == 1 or row == r:
        print('*' * r)
    else: 
        print('*' + ' ' * (c - 2) + '*')
    row += 1


'''
r = int(input("Enter the number of rows for the pattern: "))
c = int(input("Enter the number of columns for the pattern: "))

row = 1

while row <= r:
    if row == 1 or row == r:
        print('*' * c)
    else:
        print('*' + ' ' * (c - 2) + '*')
    row += 1
'''