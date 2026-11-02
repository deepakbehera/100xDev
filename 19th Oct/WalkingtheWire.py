import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        s = data[i]
        n = len(s)
        
        # They can only meet on a single knot if the length is odd
        # AND the string is a palindrome.
        if n % 2 == 1 and s == s[::-1]:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()