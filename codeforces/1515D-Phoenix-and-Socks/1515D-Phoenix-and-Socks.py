from collections import Counter

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))

    left = c[:l]
    right = c[l:]

    cl = Counter(left)
    cr = Counter(right)

    for color in list(cl.keys()):
        m = min(cl[color], cr[color])
        cl[color] -= m
        cr[color] -= m

    if l > r:
        cl, cr = cr, cl
        l, r = r, l

    cost = 0
    diff = (r - l) // 2

    for color in cr:
        pairs = cr[color] // 2
        take = min(pairs, diff)
        cr[color] -= take * 2
        diff -= take
        cost += take

    cost += diff

    remaining = sum(cl.values()) + sum(cr.values())
    cost += remaining // 2

    print(cost)