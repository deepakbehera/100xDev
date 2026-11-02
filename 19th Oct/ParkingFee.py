import sys

def solve():
    # Read input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    h1, m1 = int(input_data[0]), int(input_data[1])
    h2, m2 = int(input_data[2]), int(input_data[3])
    
    # Calculate duration in minutes
    entry_minutes = h1 * 60 + m1
    exit_minutes = h2 * 60 + m2
    duration = exit_minutes - entry_minutes
    
    # First 2 hours (120 minutes) are free
    if duration <= 120:
        print(0)
    else:
        chargeable_minutes = duration - 120
        # Ceiling division for started hours
        started_hours = (chargeable_minutes + 59) // 60
        cost = started_hours * 20
        # Maximum fee is capped at 100 rupees
        print(min(100, cost))

if __name__ == "__main__":
    solve()