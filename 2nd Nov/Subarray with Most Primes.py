import sys


def solve():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2 : 2 + n]]

    # Step 1: Precompute primes up to MAX_VAL using Sieve of Eratosthenes
    MAX_VAL = 100000
    is_prime = [True] * (MAX_VAL + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(MAX_VAL**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX_VAL + 1, i):
                is_prime[j] = False

    # Step 2: Compute number of primes in the first window of size K
    current_primes = sum(1 for x in a[:k] if is_prime[x])

    max_primes = current_primes
    best_start_idx = 0

    # Step 3: Slide the window across the array
    for i in range(k, n):
        # Subtract outgoing element
        if is_prime[a[i - k]]:
            current_primes -= 1

        # Add incoming element
        if is_prime[a[i]]:
            current_primes += 1

        # Keep the first subarray that achieves maximum primes
        if current_primes > max_primes:
            max_primes = current_primes
            best_start_idx = i - k + 1

    # Step 4: Output the optimal subarray
    result = a[best_start_idx : best_start_idx + k]
    print(*(result))


if __name__ == "__main__":
    solve()