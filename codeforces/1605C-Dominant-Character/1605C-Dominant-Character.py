t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if "aa" in s:
        print(2)
    elif "aba" in s or "aca" in s:
        print(3)
    elif "acba" in s or "abca" in s:
        print(4)
    elif "abbacca" in s or "accabba" in s:
        print(7)
    else:
        print(-1)