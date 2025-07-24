def min_operations_to_make_lvable(n, s):
    # Case 1: Check if "lv" is already present
    if "lv" in s:
        return 0

    # Case 2: Check if "vl" exists (can reverse to make "lv")
    if "vl" in s:
        return 1

    # Case 3: Check for presence of "l" or "v" and calculate replacements
    has_l = 'l' in s
    has_v = 'v' in s

    if has_l and has_v:
        # Replace one character to form "lv"
        return 1
    elif has_l or has_v:
        # Insert one character to form "lv"
        return 1
    else:
        # Insert both "l" and "v"
        return 2

# Input reading with prompts
n = int(input("Enter the length of the string (n): "))
s = input("Enter the string (s): ").strip()

# Output the result
print(min_operations_to_make_lvable(n, s))