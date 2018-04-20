string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
print([len(x)-1 if x[-1]==',' or x[-1]=='.' else len(x) for x in string.strip().split()])
