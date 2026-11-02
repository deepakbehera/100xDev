import sys

def solve():
    # Read input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    sum_n = (n*(n+1))//2
    print(sum_n)

if __name__ == "__main__":
    solve()