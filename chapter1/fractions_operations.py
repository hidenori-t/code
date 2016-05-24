'''
問題1-4(25)
分数電卓

Fraction operations 分数演算
'''

from fractions import Fraction
def add(a, b):
    print('Result of Addition: {0}'.format(a, b, a+b))

if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a, b)
