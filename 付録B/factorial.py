# 『Pythonからはじめる数学入門』:p235-236
# B.1　if __name__ == '__main__':
# Find the factorial of a number

def fact(n):
    p = 1
    for i in range(1, n+1):
        p = p*i
    return p
print(__name__)
if __name__ == '__main__':
    n = int(input('Enter an integer to find the factorial of: '))
    f = fact(n)
    print('factorial of {0}: {1}'.format(n, f))
