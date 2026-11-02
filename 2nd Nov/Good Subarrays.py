import sys


def solve():
    # Read all input from standard input for fast I/O
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    t = int(input_data[2])

    a = [int(x) for x in input_data[3 : 3 + n]]

    # A subarray of size K has average >= T if its sum >= K * T
    target_sum = k * t

    # Compute the sum of the first window of size K
    current_sum = sum(a[:k])

    # Count good subarrays
    good_count = 0
    if current_sum >= target_sum:
        good_count += 1

    # Slide the window across the array
    for i in range(k, n):
        current_sum += a[i] - a[i - k]
        if current_sum >= target_sum:
            good_count += 1

    # Output the total count of good subarrays
    print(good_count)


if __name__ == "__main__":
    solve()