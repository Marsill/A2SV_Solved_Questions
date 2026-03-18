def prefix_sum(arr):
    ps = [[0]*(w+1) for _ in range(h+1)]
    for r in range(1, h+1):
        for c in range(1, w+1):
            ps[r][c] = arr[r-1][c-1] + ps[r-1][c] + ps[r][c-1] - ps[r-1][c-1]
    return ps

ph = prefix_sum(hor)
pv = prefix_sum(ver)

def query(ps, r1, c1, r2, c2):
    return ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    h_count = 0 if c1 == c2 else query(ph, r1, c1, r2, c2-1)
    v_count = 0 if r1 == r2 else query(pv, r1, c1, r2-1, c2)
    print(h_count + v_count)