import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    q = int(data[1])
    
    # Read initial binary array
    s = [int(val) for val in data[2:2 + n]]
    
    # Difference array of size (n + 2) to handle 1-based indexing
    diff = [0] * (n + 2)
    
    # Process q range queries
    idx = 2 + n
    for _ in range(q):
        l = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        
        diff[l] += 1
        diff[r + 1] -= 1
        
    result = []
    current_toggles = 0
    
    # Compute total toggles using prefix sums and determine final state
    for i in range(1, n + 1):
        current_toggles += diff[i]
        # Flip the original bit if it has been toggled an odd number of times
        final_bit = s[i - 1] ^ (current_toggles % 2)
        result.append(str(final_bit))
        
    print(" ".join(result))

if __name__ == '__main__':
    solve()