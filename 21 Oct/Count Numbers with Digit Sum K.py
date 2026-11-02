import sys

def solve():
    # Fast I/O reading all space/newline separated tokens
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    n = int(input_data[idx])
    idx += 1
    
    # Extract the n array elements sequentially
    a = []
    for _ in range(n):
        a.append(int(input_data[idx]))
        idx += 1
    
    # Construct prefix sum array (1-based index support)
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]
        
    # Read Q
    q = int(input_data[idx])
    idx += 1
    
    output = []
    
    # Process queries
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        
        # Calculate sum for range [l, r]
        ans = pref[r] - pref[l - 1]
        output.append(str(ans))
        
    # Print result
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()