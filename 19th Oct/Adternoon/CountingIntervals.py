import sys


def solve():
    # Read all input at once for fast I/O performance
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    Q = int(input_data[0])
    results = []

    idx = 1
    for _ in range(Q):
        T = int(input_data[idx])
        L = int(input_data[idx + 1])
        R = int(input_data[idx + 2])
        idx += 3

        # Base constraint check
        if L > R:
            results.append("0")
            continue

        # Calculate count based on type
        if T == 1:
            count = R - L - 1
        elif T == 2 or T == 3:
            count = R - L
        elif T == 4:
            count = R - L + 1

        # The count cannot be negative
        results.append(str(max(0, count)))

    # Output all answers separated by newline
    print("\n".join(results))


if __name__ == "__main__":
    solve()