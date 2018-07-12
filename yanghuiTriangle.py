def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [x + L[i+1] for i,x in enumerate(L[:-1]) ] + [1]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break