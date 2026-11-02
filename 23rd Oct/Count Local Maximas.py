import sys


def solve():
    # Fast I/O for competitive programming
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    Q = int(input_data[1])

    # 0-indexed array A
    A = [int(x) for x in input_data[2 : N + 2]]

    # Step 1: Build contribution array C
    # C[i] = 1 if A[i] is a local maximum among its immediate neighbors
    C = [0] * N
    for i in range(1, N - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            C[i] = 1

    # Step 2: Build Prefix Sum array P for C
    P = [0] * N
    P[0] = C[0]
    for i in range(1, N):
        P[i] = P[i - 1] + C[i]

    # Helper function for range sum query on array C
    def query_sum(l, r):
        if l > r:
            return 0
        if l == 0:
            return P[r]
        return P[r] - P[l - 1]

    # Step 3: Process queries in O(1)
    out = []
    idx = N + 2
    for _ in range(Q):
        L = int(input_data[idx])
        R = int(input_data[idx + 1])
        idx += 2

        # Convert 1-based bounds to 0-based
        l = L - 1
        r = R - 1

        # A valid local maximum for range [L, R] must be strictly inside (L, R)
        # 0-indexed inner range: [l + 1, r - 1]
        if r - l < 2:
            out.append("0")
        else:
            local_max_count = query_sum(l + 1, r - 1)
            out.append(str(local_max_count))

    # Output all answers
    print("\n".join(out))


if __name__ == "__main__":
    solve()