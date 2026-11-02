import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    target_block = '.' * k
    total_ways = 0
    
    # Process each row
    for i in range(3, 3 + n):
        row = input_data[i]
        # Check every contiguous subsegment of length k in the current row
        for j in range(m - k + 1):
            if row[j:j + k] == target_block:
                total_ways += 1
                
    print(total_ways)

if __name__ == "__main__":
    solve()