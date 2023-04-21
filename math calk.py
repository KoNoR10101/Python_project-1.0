def facktorial(n):
    return

actions = { "+":lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '!': facktorial}

try:
    print('Введите число')
    nums = map(int, input().split())
    print('number:')
    operation = input()
    print(actions[operation](*nums))
except Exception as error:
    print(error)