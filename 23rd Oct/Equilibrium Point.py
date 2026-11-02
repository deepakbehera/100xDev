import sys


def solve():
    # Fast input parsing
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]

    # O(N) sum calculation
    total_sum = sum(a)
    left_sum = 0

    # Find the first equilibrium point
    for i in range(n):
        # right_sum = total_sum - left_sum - a[i]
        right_sum = total_sum - left_sum - a[i]

        if left_sum == right_sum:
            print(i)
            return

        left_sum += a[i]

    # If no equilibrium point is found
    print(-1)


if __name__ == "__main__":
    solve()