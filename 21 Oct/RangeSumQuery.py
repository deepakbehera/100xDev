import sys

def solve():
    # Fast I/O reading all input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # Extract the n array elements
    a = [int(x) for x in input_data[1 : n + 1]]
    
    # Construct the prefix sum array
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]
    
    # Read number of queries
    q = int(input_data[n + 1])
    
    idx = n + 2
    output = []
    
    # Process each query in O(1)
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        
        # Calculate sum for range [l, r]
        output.append(str(pref[r] - pref[l - 1]))
    
    # Print all answers separated by newline
    print('\n'.join(output))

if __name__ == '__main__':
    solve()