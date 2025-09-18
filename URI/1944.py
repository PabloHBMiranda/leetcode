from collections import deque

attempts = int(input())

result = 0
game = deque('FACE')
for attempts in range(0, attempts, 1):
    if not game:
        game = deque('FACE')

    word = input().replace(' ', '')
    removed = ''

    for i in range(0, 4, 1):
        removed += (game.pop())

    if word != removed:
        game.extend(reversed(removed))
        game.extend(word)
    else:
        result += 1

print(result)
