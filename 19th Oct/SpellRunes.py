import sys

def get_rune(k):
    # k is 0-indexed count of generated runes
    if k % 2 == 0:
        # Uppercase letter (A-Z)
        return chr(ord('A') + (k // 2) % 26)
    else:
        # Digit (0-9)
        return chr(ord('0') + (k // 2) % 10)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = 0  # Global rune index counter
    
    result = []
    for i in range(1, n + 1):
        # Generate i runes for the left end
        left = []
        for _ in range(i):
            left.append(get_rune(k))
            k += 1
            
        # Generate i runes for the right end
        right = []
        for _ in range(i):
            right.append(get_rune(k))
            k += 1
            
        # Middle space count: Total width (2*n) - left count (i) - right count (i)
        spaces = " " * (2 * n - 2 * i)
        
        row = "".join(left) + spaces + "".join(right)
        result.append(row)
        
    print("\n".join(result))

if __name__ == "__main__":
    solve()