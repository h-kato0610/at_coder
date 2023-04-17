N = int(input())

l = [None for n in range(N)]

for n in range(N):
    s = input()
    l[n] = s
l.reverse()

[print(i) for i in l]