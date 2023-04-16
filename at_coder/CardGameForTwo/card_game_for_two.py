n = int(input())
an = list(map(int, input().split()))
an.sort(reverse=True)
is_alice_or_bob = True

alice = []
bob = []
for _ in range(n):
    if is_alice_or_bob:
        alice.append(an.pop(0))
    else:
        bob.append(an.pop(0))
    is_alice_or_bob = not is_alice_or_bob

print(sum(alice) - sum(bob))