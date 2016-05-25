'''
問題1-5(:27)

multi_table_exit_power.py

Multiplication table printer with exit power to the user
ユーザが抜け出せる乗算表
'''

def multi_table(a):

    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))


if __name__ == '__main__':

    while True:
        a = input('Enter a number: ')
        multi_table(float(a))

        answer = input('Do you want to exit? (y) for yes ') # 抜けたいか?
        if answer == 'y':
            break
