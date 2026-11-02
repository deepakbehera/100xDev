import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L, R = int(input_data[0]), int(input_data[1])
    
    count = 0
    for x in range(L, R + 1):
        if is_prime(x):
            # Reverse the digits of x
            rev_x = int(str(x)[::-1])
            if is_prime(rev_x):
                count += 1
                
    print(count)

if __name__ == "__main__":
    solve()