def pal(s):
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    odd_count = 0
    for count in counter.values():
        odd_count += count % 2
    return odd_count in [0, 1]

print(pal("motor"))
