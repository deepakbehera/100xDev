import sys


def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]

    prefix = [1] * n
    suffix = [1] * n

    # Step 1: Build prefix product array
    # prefix[i] contains the product of all elements to the left of index i
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * a[i - 1]

    # Step 2: Build suffix product array
    # suffix[i] contains the product of all elements to the right of index i
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * a[i + 1]

    # Step 3: Combine prefix and suffix products
    ans = [prefix[i] * suffix[i] for i in range(n)]

    # Print output space-separated
    print(*(ans))


if __name__ == "__main__":
    solve()