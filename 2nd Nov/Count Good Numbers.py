import sys


def solve():
    # Fast I/O reading
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    # Parse array A
    a = [int(x) for x in input_data[3 : 3 + n]]

    # Parse good numbers and convert to a Hash Set for O(1) membership check
    good_set = set(int(x) for x in input_data[3 + n : 3 + n + m])

    # Step 1: Count good numbers in the first window of size K
    current_good_count = sum(1 for x in a[:k] if x in good_set)

    result = [current_good_count]

    # Step 2: Slide the window across the array
    for i in range(k, n):
        # Remove outgoing element from the count if it's good
        if a[i - k] in good_set:
            current_good_count -= 1

        # Add incoming element to the count if it's good
        if a[i] in good_set:
            current_good_count += 1

        result.append(current_good_count)

    # Step 3: Print all window counts separated by space
    print(*(result))


if __name__ == "__main__":
    solve()