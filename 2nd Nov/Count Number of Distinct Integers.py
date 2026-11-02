from collections import Counter
import sys


def solve():
    # Read all input from standard input for fast I/O
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    # Parse array elements
    a = [int(x) for x in input_data[2 : 2 + n]]

    # Step 1: Initialize frequency map for the first window of size K
    freq_map = Counter(a[:k])

    result = [len(freq_map)]

    # Step 2: Slide the window across the array
    for i in range(k, n):
        outgoing = a[i - k]
        incoming = a[i]

        # Process outgoing element
        freq_map[outgoing] -= 1
        if freq_map[outgoing] == 0:
            del freq_map[outgoing]

        # Process incoming element
        freq_map[incoming] += 1

        # Store number of distinct elements in current window
        result.append(len(freq_map))

    # Step 3: Output all results separated by space
    print(*(result))


if __name__ == "__main__":
    solve()