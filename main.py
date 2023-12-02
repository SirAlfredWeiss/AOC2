with open('text.txt', 'r') as file:
   lines = file.read().splitlines()
games = {}
for line in lines:
    game_id, data = line.split(": ")
    parts = data.split("; ")
    game_id = int(game_id.split()[1])
    games[game_id] = part_list = []
    for part in parts:
        part_list.append({col:int(n) for n,col in map(str.split,part.split(", "))})
def validate_game(game):
    for draw in game:
        if draw.get('red',0) > 12 or draw.get('green',0) > 13 or draw.get('blue',0) > 14:
            return False
    return True
def max_cubes(game):
    out = {'red':0,'green':0,'blue':0}
    for dct in game:
        for s in ('red','green','blue'):
            out[s] = max(out[s],dct.get(s,0))
    return out['red']*out['green']*out['blue']
print("Part 1:",sum(gid for gid,game in games.items() if validate_game(game)))
print("Part 2:",sum(max_cubes(game) for gid,game in games.items()))