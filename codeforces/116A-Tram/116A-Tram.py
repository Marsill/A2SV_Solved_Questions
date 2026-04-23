n = int(input())

current = 0
capacity = 0

for _ in range(n):
    a, b = map(int, input().split())
    
    current -= a   # passengers exit
    current += b   # passengers enter
    
    capacity = max(capacity, current)

print(capacity)