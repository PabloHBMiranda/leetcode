from collections import deque

while True:
    numberItems = int(input())
    if numberItems == 0:
        break

    while True:
        stack = deque(range(numberItems, 0, -1))
        inputData = input()

        if inputData == '0':
            print()
            break

        station = deque([])
        train = [int(s) for s in inputData.split()]

        pos = 0
        result = True
        while stack or station:
            if (len(station) == 0) or station[-1] < train[pos]:
                station.append(stack.pop())
            elif station[-1] == train[pos]:
                pos += 1
                station.pop()
            else:
                result = False
                break

        print('Yes') if result else print('No')