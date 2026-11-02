import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    q = int(data[1])
    
    # 1-indexed difference array of size (n + 2)
    diff = [0] * (n + 2)
    
    # Read initial array values and construct initial difference array
    x = [int(val) for val in data[2:2 + n]]
    for i in range(1, n + 1):
        val = x[i - 1]
        diff[i] += val
        diff[i + 1] -= val
        
    # Process range updates
    idx = 2 + n
    for _ in range(q):
        a = int(data[idx])
        b = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        
        diff[a] += k
        diff[b + 1] -= k
        
    max_val = 0
    current_val = 0
    
    # Compute prefix sums to find the maximum element value
    for i in range(1, n + 1):
        current_val += diff[i]
        if current_val > max_val:
            max_val = current_val
            
    print(max_val)

if __name__ == '__main__':
    solve()