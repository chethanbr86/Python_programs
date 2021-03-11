games = {'chet':100, 'indu':10, 'sha':35, 'bhagu': 15}

#By default, python gives keys when not stated particularly
for game in games:
    print(game)

#To get values
for game in games:
    print(games[game])

#You can mention particularly keys
for key in games.keys():
    print(key)

#You can mention particularly values
for val in games.values():
    print(val)

#Or both
for key, val in games.items():
    print(key, val)

#get method
for item in games:
    k = games.get('chet')
print(k)