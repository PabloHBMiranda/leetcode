from collections import deque

while True:
    numberItems = int(input())
    if numberItems == 0:
        break

    firsData = input()

    stack = deque([s for s in reversed(firsData.split())])

    finalData = input()
    train = [s for s in finalData.split()]

    station = deque([])
    pos = 0
    data = {'result': True, 'interactions': []}
    while pos < len(train) or stack:
        if (len(stack) > 0) and (len(station) == 0 or station[-1] != train[pos]):
            station.append(stack.pop())
            data['interactions'].append('I')
        elif station[-1] == train[pos]:
            pos += 1
            station.pop()
            data['interactions'].append('R')
        else :
            data['result'] = False
            break
    print(*data['interactions'], ' Impossible' if not data['result'] else '', sep="")