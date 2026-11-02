import sys


def solve():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    # Parse inputs
    N = int(data[0])
    Q = int(data[1])

    A = [int(x) for x in data[2 : N + 2]]

    # Pointer to track queries location in data
    idx = N + 2

    # Step 1: Build indicator array C
    # C[i] = 1 if A[i] == A[i+1], else 0
    C = [1 if A[i] == A[i + 1] else 0 for i in range(N - 1)]

    # Step 2: Build Prefix Sum array P for C
    P = [0] * (N - 1)
    if N > 1:
        P[0] = C[0]
        for i in range(1, N - 1):
            P[i] = P[i - 1] + C[i]

    out = []

    # Helper function for range query
    def query(l, r):
        if l > r:
            return 0
        if l == 0:
            return P[r]
        return P[r] - P[l - 1]

    # Step 3: Process queries
    for _ in range(Q):
        L = int(data[idx])
        R = int(data[idx + 1])
        idx += 2

        # 1-element subarray is always valid
        if L == R:
            out.append("YES")
            continue

        # Convert to 0-indexed range for C array
        l = L - 1
        r = R - 2

        # Number of adjacent equal pairs in range [L-1, R-2]
        same_count = query(l, r)

        # Total expected adjacent pairs is (R - L)
        if same_count == (R - L):
            out.append("YES")
        else:
            out.append("NO")

    # Print all results separated by newline
    print("\n".join(out))


if __name__ == "__main__":
    solve()