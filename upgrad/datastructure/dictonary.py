games = {'Mike':100, 'Link':10, 'Sucre':35, 'Sara': 15}

#By default, python gives keys when not stated particularly
for game in games:
    print(f'1: {game}')

#To get values
for game in games:
    print(f'2: {games[game]}')

#You can mention particularly keys
for key in games.keys():
    print(f'3: {key}')

#You can mention particularly values
for val in games.values():
    print(f'4: {val}')

#Or both
for key, val in games.items():
    print(f'5: {key}, {val}')

#get method
for item in games:
    k = games.get('Sara') #if key exists, value will be printed
print(f'6: {k}')