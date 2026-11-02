import sys


def solve():
    # Fast input reading
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]

    # Prefix sum arrays storing even and odd sums up to index i - 1
    pref_even = [0] * (n + 1)
    pref_odd = [0] * (n + 1)

    for i in range(n):
        pref_even[i + 1] = pref_even[i] + (a[i] if i % 2 == 0 else 0)
        pref_odd[i + 1] = pref_odd[i] + (a[i] if i % 2 != 0 else 0)

    total_even = pref_even[n]
    total_odd = pref_odd[n]

    special_indices_count = 0

    # Check every index i
    for i in range(n):
        even_before = pref_even[i]
        odd_before = pref_odd[i]

        # Suffix sums after removing a[i]
        if i % 2 == 0:
            even_after = total_even - even_before - a[i]
            odd_after = total_odd - odd_before
        else:
            even_after = total_even - even_before
            odd_after = total_odd - odd_before - a[i]

        # After removing a[i], even-indexed items after i swap to odd indices and vice versa
        new_even_sum = even_before + odd_after
        new_odd_sum = odd_before + even_after

        if new_even_sum == new_odd_sum:
            special_indices_count += 1

    print(special_indices_count)


if __name__ == "__main__":
    solve()