import sys


def solve():
    # Read all input from standard input for fast I/O
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    n = int(data[0])
    k = int(data[1])

    # Parse the array elements
    a = [int(x) for x in data[2 : 2 + n]]

    # Step 1: Compute sum of the first window of size K
    current_sum = sum(a[:k])
    max_sum = current_sum

    # Step 2: Slide the window across the array
    for i in range(k, n):
        current_sum += a[i] - a[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    # Step 3: Print the maximum sum found
    print(max_sum)


if __name__ == "__main__":
    solve()