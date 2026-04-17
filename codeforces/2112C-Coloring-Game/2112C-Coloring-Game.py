t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = arr[-1]
    ans = 0

    for k in range(2, n):
        T = max(arr[k], max_val - arr[k])

        i = 0
        j = k - 1
        while i < j:
            if arr[i] + arr[j] > T:
                ans += (j - i)
                j -= 1
            else:
                i += 1

    print(ans)