import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]
    
    max_len = 1
    best_start = 1
    
    curr_len = 1
    curr_start = 1
    
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            curr_len += 1
        else:
            curr_len = 1
            curr_start = i + 1  # 1-indexed day number
            
        # Update maximum length and starting day
        if curr_len > max_len:
            max_len = curr_len
            best_start = curr_start
            
    print(max_len, best_start)

if __name__ == "__main__":
    solve()