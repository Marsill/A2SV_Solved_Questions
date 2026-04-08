t = int(input()) 
for _ in range(t): 
    n, m = map(int, input(). split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    a[0] =min(a[0] , b[0] - a[0])

    
    for i in range(1, len(a)):
        l = 0
        r = m - 1
        while l <= r:
            mid = (l+r)//2
            if b[mid] - a[i] < a[i-1]:             
                l = mid + 1
            else:
                r = mid - 1
        if a[i] >= a[i-1] and l < len(b):
            a[i] = min(a[i], b[l] - a[i])
        elif a[i] >= a[i-1]:
            continue
        elif l < len(b):
            a[i] = b[l] - a[i]
        else:
            print("NO")
            break
    else:
        print("YES")