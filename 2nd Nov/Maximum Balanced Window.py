import sys


def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    # Parse binary array elements
    a = [int(x) for x in input_data[2 : 2 + n]]

    # Step 1: Count ones in the first window of size K
    current_ones = sum(a[:k])

    # Flipping at most one 0 gives min(K, current_ones + 1) ones
    max_ones = min(k, current_ones + 1)

    # Step 2: Slide the window across the array
    for i in range(k, n):
        current_ones += a[i] - a[i - k]
        max_ones = max(max_ones, min(k, current_ones + 1))

    # Step 3: Output the result
    print(max_ones)


if __name__ == "__main__":
    solve()