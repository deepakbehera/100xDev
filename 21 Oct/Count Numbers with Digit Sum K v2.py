import sys

def solve():
    # Generator yielding one token (number) at a time regardless of line breaks
    def token_generator():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = token_generator()
    
    try:
        n_str = next(tokens)
    except StopIteration:
        return
    
    n = int(n_str)
    
    # Construct prefix sum array directly on the fly
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + int(next(tokens))
        
    q = int(next(tokens))
    output = []
    
    # Process queries
    for _ in range(q):
        l = int(next(tokens))
        r = int(next(tokens))
        output.append(str(pref[r] - pref[l - 1]))
        
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()