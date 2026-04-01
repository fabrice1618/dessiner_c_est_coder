triples = []

for a in range(1, 101):
    for b in range(a + 1, 101):
        c2 = a*a + b*b
        c = int(c2 ** 0.5)
        if c * c == c2:
            triples.append((a, b, c))

print(triples)

