from collections import deque

while True:
    inputData = int(input())
    if inputData == 0:
        break

    stack = deque(range(inputData, 0, -1))

    discard = True
    print('Discarded cards: ', end='')
    while True:
        if len(stack) <= 1:
            break

        if discard:
            print(stack.pop(), end='')
            if len(stack) > 1:
                print(', ', end='')
        else:
            stack.appendleft(stack.pop())

        discard = not discard

    print('\nRemaining card:', stack.pop())