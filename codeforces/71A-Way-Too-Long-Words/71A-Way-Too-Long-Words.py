t = int(input())
for _ in range(t):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        length = len(s) - 2
        print(f"{s[0]}{length}{s[-1]}")