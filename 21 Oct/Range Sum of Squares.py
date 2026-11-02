import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    MOD = 10**9 + 7
    n = int(input_data[0])
    
    a = [int(x) for x in input_data[1 : n + 1]]
    
    # pref_prod stores cumulative product modulo (10^9 + 7) ignoring 0s
    pref_prod = [1] * (n + 1)
    # pref_zero stores count of zeros up to index i
    pref_zero = [0] * (n + 1)
    
    for i in range(1, n + 1):
        val = a[i - 1]
        if val == 0:
            pref_zero[i] = pref_zero[i - 1] + 1
            pref_prod[i] = pref_prod[i - 1]
        else:
            pref_zero[i] = pref_zero[i - 1]
            pref_prod[i] = (pref_prod[i - 1] * val) % MOD
            
    q = int(input_data[n + 1])
    idx = n + 2
    output = []
    
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        
        # Check if there are any zeros in range [l, r]
        zeros_in_range = pref_zero[r] - pref_zero[l - 1]
        
        if zeros_in_range > 0:
            output.append("0")
        else:
            # Range product = pref_prod[r] * inv(pref_prod[l - 1]) % MOD
            inv_l_minus_1 = pow(pref_prod[l - 1], MOD - 2, MOD)
            ans = (pref_prod[r] * inv_l_minus_1) % MOD
            output.append(str(ans))
            
    print('\n'.join(output))

if __name__ == '__main__':
    solve()