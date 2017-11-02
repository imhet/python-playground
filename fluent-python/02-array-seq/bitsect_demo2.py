import bisect

data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]  # precomputed list of keys

for i in [0, 1, 5, 8]:
    print(data[bisect.bisect_left(keys, i)])
