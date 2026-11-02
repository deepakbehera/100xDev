import sys


def solve():
    # Read input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]

    # Step 1: Calculate total sum in O(N)
    total_sum = sum(a)

    # If the total sum is odd, it cannot be divided into two equal integer halves
    if total_sum % 2 != 0:
        print("NO")
        return

    target_sum = total_sum // 2
    left_sum = 0

    # Step 2: Iterate up to n - 1 (ensuring the right subarray is non-empty)
    for i in range(n - 1):
        left_sum += a[i]
        if left_sum == target_sum:
            print("YES")
            return

    # Step 3: If no valid split point is found
    print("NO")


if __name__ == "__main__":
    solve()