import sys


def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    s = input_data[2]

    # Set of all upper and lower case vowels for O(1) lookup
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    # Compute number of vowels in the first window of size K
    current_vowel_count = sum(1 for char in s[:k] if char in vowels)

    result = [current_vowel_count]

    # Slide the window across the string
    for i in range(k, n):
        # Remove effect of the character sliding out
        if s[i - k] in vowels:
            current_vowel_count -= 1

        # Add effect of the character sliding in
        if s[i] in vowels:
            current_vowel_count += 1

        result.append(current_vowel_count)

    # Print the answer separated by spaces
    print(*(result))


if __name__ == "__main__":
    solve()