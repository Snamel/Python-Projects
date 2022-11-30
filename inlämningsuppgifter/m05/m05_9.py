import pprint

pp = pprint.PrettyPrinter(indent=2)

test = [
    {'namn': 'Mohammed', 'result': '37'},
    {"namn": "Franz", "result": "93"},
    {"namn": "Henry", "result": "79"},
    {"namn": "Lova", "result": "54"},
    {"namn": "Cilla", "result": "61"},
    {"namn": "Henry", "result": "89"},
    {"namn": "Östen", "result": "62"},
    {"namn": "Vera", "result": "57"},
    {"namn": "Hedvig", "result": "4"},
    {"namn": "Xerxes", "result": "14"},
    {"namn": "Franz", "result": "64"},
    {"namn": "Otto", "result": "98"},
    {"namn": "Lova", "result": "15"},
    {"namn": "Rafael", "result": "48"},
    {"namn": "Walter", "result": "57"},
    {"namn": "Älva-My", "result": "70"},
    {"namn": "Ellen", "result": "71"},
    {"namn": "David", "result": "3"},
    {"namn": "Vera", "result": "80"},
    {"namn": "Leia", "result": "8"},
    {"namn": "Matteo", "result": "33"},
    {"namn": "August", "result": "68"},
    {"namn": "Henry", "result": "27"},
    {"namn": "Nicholas", "result": "72"},
    {"namn": "Selma", "result": "65"}
]

cols = "{:<10} | {:<10}"

print("\nSortera listan på poäng, lågt till högt")
test.sort(key=lambda i: int(i['result']))
for i in test:
    print(cols.format(i["namn"], i["result"]))

print("\nSortera listan på resultat, högt till lågt")
for i in test[::-1]:
    print(cols.format(i["namn"], i["result"]))

print("\nSortera listan på namn, a till ö")
for i in test[:-1]:
    print(cols.format(i["namn"], i["result"]))

print("\nSortera listan på först ålder, ung till äldre, och sedan på namn, a till ö")
pp.pprint(sorted(test, key=lambda i: (i['result'], i['namn'])))
