l1, r1, l2, r2 = map(int, input().split())

intersection = [max(l1,l2), min(r1,r2)] if l1 <= r2 and l2 <= r1 else [-1]

# In ra đoạn giao nhau
print(*intersection)