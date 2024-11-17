def are_you_playing_banjo(name):
    # name = input()
    # if name[0] == 'R' or name[0] == 'r':
    #     print(f'{name} plays banjo')
    # else:
    #     print(f'{name} does not play banjo')
    # return name

    if name[0] == 'R' or name[0] == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    return name

print(are_you_playing_banjo('Rajesh'))
print(are_you_playing_banjo('Chethan'))