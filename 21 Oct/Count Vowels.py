import sys

def solve():
    # Fast I/O reading all inputs at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = input_data[1]
    q = int(input_data[2])
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # pref[i] stores the count of vowels in s[0 ... i-1]
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        is_vowel = 1 if s[i - 1] in vowels else 0
        pref[i] = pref[i - 1] + is_vowel
    
    idx = 3
    output = []
    
    # Process each query
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        
        # Calculate number of vowels in s[l ... r] (1-based)
        vowel_count = pref[r] - pref[l - 1]
        output.append(str(vowel_count))
    
    print('\n'.join(output))

if __name__ == '__main__':
    solve()