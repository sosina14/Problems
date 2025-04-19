s = input()
k = int(input())

if k > len(s):
    print("impossible")
else:
    unique_letters = set(s)
    current_unique = len(unique_letters)
    changes_needed = max(0, k - current_unique)
    
    print(changes_needed)
