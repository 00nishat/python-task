river={'padma':'run through rajshahi','meghna':'run through kishoregang', 'jomuna':'run through dhaka and rajshahi'}
for name in river.keys():
    print(name)
for name,massage in river.items():
    print(f'{name.upper()}= {massage}')
for msg in river.values():
    print(msg)