puzzle_input = '2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14'

seen = []
banks = [int(x) for x in puzzle_input.split('\t')]

while str(banks) not in seen:
    seen.append(str(banks))

    m = max(banks)
    idx = banks.index(m)
    banks[idx] = 0
    if idx == len(banks) - 1:
        idx = 0
    else:
        idx += 1

    for x in range(m, 0, -1):
        banks[idx] += 1
        if idx == len(banks) - 1:
            idx = 0
        else:
            idx += 1

print(len(seen))