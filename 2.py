import requests
import json

_tiles = []

tiles = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
etiles = []


while len(_tiles) != 16:
    j = requests.get('https://olimp.miet.ru/ppo_it/api').content
    tile =  json.loads(j)['message']['data']

    if tile not in _tiles:
        _tiles.append(tile)

for _t in _tiles:
    flagUp = 1
    flagDown = 1

    for j in range(64):
        if _t[0][j] != 255:
            flagUp = 0
            break

    for j in range(64):
        if _t[j][0] != 255:
            flagDown = 0
            break

    if flagUp and flagDown:
        tiles[0][0] = _t
        _tiles.remove(_t)
        break

for i in range(1, 4):
    index = 0
    mini = 1000000000

    for _t in _tiles:
        _mini = 0

        for j in range(64):
            _mini += abs(tiles[i-1][0][63][j] - _t[0][j])

        if _mini < mini:
            mini = _mini
            index = _tiles.index(_t)

    tiles[i][0] = _tiles[index]
    _tiles.remove(_tiles[index])
        
for k in range(4):
    for i in range(1, 4):
        index = 0
        mini = 1000000000

        for _t in _tiles:
            _mini = 0

            for j in range(64):
                _mini += abs(tiles[k][i-1][j][63] - _t[j][0])

            if _mini < mini:
                mini = _mini
                index = _tiles.index(_t)

        tiles[k][i] = _tiles[index]
        _tiles.remove(_tiles[index])

for k in tiles:
    for i in range(64):
        raw = k[0][i]

        for j in range(1, 4):
            for a in k[j][i]:
                raw.append(a)

        etiles.append(raw)


s = ''

for i in etiles:
    for j in i:
        s += str(j) + ' '

f = open('1.txt', 'w')
f.write(s)