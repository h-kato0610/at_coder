a = int(input())
b_c = list(map(int, input().split()))
s = input()

n = sum(b_c, a)

print('{} {}'.format(n, s))