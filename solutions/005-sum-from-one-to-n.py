# Read input (if any), compute, and print the result
N = int(
    input()
)

total = 0

for i in range(1, N+1):
    total += i

print(total)