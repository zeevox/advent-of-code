li = [1, 0, 15, 2, 10, 13]
freq = {x: [i + 1, i + 1] for i, x in enumerate(li)}

counter = len(li) + 1
while counter <= 2020:
    p = freq[li[counter - 2]]
    v = 0 if p[0] == p[1] else p[1] - p[0]
    li.append(v)
    freq[v] = [freq.get(v, [counter])[-1], counter]
    counter += 1

print(li[-1])
