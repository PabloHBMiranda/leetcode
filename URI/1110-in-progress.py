from collections import deque

stack = deque()
while True:
    inputData = int(input())
    if inputData == 0:
        break

    print('Discarded cards: ', end='')
    if inputData > 1:
        for pos, value in enumerate(range(1, inputData + 1), start=1):
            if value % 2 == 0:
                stack.appendleft(value)
            else:
                print(value, end='')
                if inputData != 3 and inputData != 2:
                    print(', ', end='')

                if value == inputData and inputData % 2 != 0:
                    stack.appendleft(stack.pop())

        discard = True
        while True:
            if stack.maxlen <= 1:
                break

            if discard:
                print(stack.pop(), end='')
                if stack.maxlen > 1:
                    print(', ', end='')
            else:
                stack.appendleft(stack.pop())

            discard = not discard

        print('\nRemaining card:', stack.pop())
    else:
        print('\nRemaining card:', 1)
