import math
import sys


def count_factors(n: int) -> int:
    """Counts the total number of positive factors of n using trial division up to sqrt(n)."""
    if n < 1:
        return 0

    factors_count = 0
    limit = math.isqrt(n)

    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                factors_count += 1  # i and n // i are the same factor
            else:
                factors_count += 2  # i and n // i are two distinct factors

    return factors_count


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])

    # A prime number has strictly 2 distinct factors (1 and N)
    if count_factors(N) == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()