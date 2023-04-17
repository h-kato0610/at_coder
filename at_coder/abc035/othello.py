N, Q = map(int, input().split())

B = 1
W = 0

n = [W for i in range(N)]

for q in range(Q):
    l, r = map(int, input().split())

    if l == r:
        n[l - 1] = W if n[l - 1] == B else B
    else:
        for i in range(l - 1, r, 1):
            n[i] = W if n[i] == B else B

print(''.join(map(str, n)))
