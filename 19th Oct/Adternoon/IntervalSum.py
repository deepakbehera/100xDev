import sys


def solve():
    # Read all input from standard input at once for fast I/O
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    Q = int(data[0])

    results = []
    idx = 1
    for _ in range(Q):
        L = int(data[idx])
        R = int(data[idx + 1])
        idx += 2

        # Sum from 1 to R
        sum_R = R * (R + 1) // 2
        # Sum from 1 to L - 1
        sum_L_minus_1 = (L - 1) * L // 2

        # Sum from L to R inclusive
        ans = sum_R - sum_L_minus_1
        results.append(str(ans))

    # Print all results separated by a newline
    print("\n".join(results))


if __name__ == "__main__":
    solve()