import sys


def solve():
    # Fast I/O for large inputs
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    Q = int(input_data[1])

    # Reading array A (0-indexed)
    A = [int(x) for x in input_data[2 : N + 2]]

    # Step 1: Build indicator array C
    # C[i] = 1 if A[i] == A[i+1], else 0
    C = [1 if A[i] == A[i + 1] else 0 for i in range(N - 1)]

    # Step 2: Build Prefix Sum array P for C
    P = [0] * (N - 1)
    if N > 1:
        P[0] = C[0]
        for i in range(1, N - 1):
            P[i] = P[i - 1] + C[i]

    # Helper function for range query on prefix sum array
    def query_sum(l, r):
        if l > r:
            return 0
        if l == 0:
            return P[r]
        return P[r] - P[l - 1]

    # Step 3: Answer queries in O(1)
    out = []
    idx = N + 2
    for _ in range(Q):
        L = int(input_data[idx])
        R = int(input_data[idx + 1])
        idx += 2

        # 1-element range has no adjacent pairs
        if L == R:
            out.append("0")
            continue

        # Convert to 0-indexed range for C array
        l = L - 1
        r = R - 2

        ans = query_sum(l, r)
        out.append(str(ans))

    # Output all answers
    print("\n".join(out))


if __name__ == "__main__":
    solve()