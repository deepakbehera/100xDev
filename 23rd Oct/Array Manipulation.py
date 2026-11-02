import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    q = int(data[1])
    
    # Difference array of size (n + 2) to safely handle 1-based indexing and (b + 1) updates
    diff = [0] * (n + 2)
    
    idx = 2
    for _ in range(q):
        a = int(data[idx])
        b = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        
        diff[a] += k
        diff[b + 1] -= k
        
    max_val = 0
    current_sum = 0
    
    # Compute prefix sum to find the maximum element value
    for i in range(1, n + 1):
        current_sum += diff[i]
        if current_sum > max_val:
            max_val = current_sum
            
    print(max_val)

if __name__ == '__main__':
    solve()