import sys

def solve():
    # Read the input integer
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    steps = 0
    
    # Repeat until n becomes a single digit
    while n >= 10:
        prod = 1
        for digit in str(n):
            prod *= int(digit)
        n = prod
        steps += 1
        
    print(steps)

if __name__ == "__main__":
    solve()