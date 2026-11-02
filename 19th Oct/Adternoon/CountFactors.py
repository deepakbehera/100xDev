import math
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])

    count = 0
    limit = int(math.isqrt(N))

    for d in range(1, limit + 1):
        if N % d == 0:
            if d * d == N:
                count += 1
            else:
                count += 2

    print(count)


if __name__ == "__main__":
    solve()