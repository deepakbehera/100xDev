import sys

def solve():
    # Fast I/O to read all inputs at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 0-indexed list of input values
    a = [int(x) for x in input_data[1 : n + 1]]
    
    # pref[i] stores sum of elements at EVEN 1-based indices up to index i
    pref = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            # i is 1-based, corresponding to a[i-1] in 0-indexed list
            pref[i] = pref[i - 1] + a[i - 1]
        else:
            pref[i] = pref[i - 1]
            
    q = int(input_data[n + 1])
    
    idx = n + 2
    output = []
    
    # Process queries
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        
        # Range sum for even indices in [l, r]
        # Since 1 <= l <= r <= n, pref[l - 1] is always valid (pref[0] = 0)
        ans = pref[r] - pref[l - 1]
        output.append(str(ans))
        
    print('\n'.join(output))

if __name__ == '__main__':
    solve()