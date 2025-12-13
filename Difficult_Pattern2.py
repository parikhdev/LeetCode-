def print_super_pattern(word):
    n = len(word)
    steps = list(range(n)) + list(range(n-2, -1, -1))
    for i in steps:
        left = word[:i+1]
        right = word[n-1-i:]
        total_len = 2 * n
        space_count = total_len - (len(left) + len(right))
        spaces = " " * space_count
        raw_line = left + spaces + right
        formatted_line = " ".join(raw_line)
        print(formatted_line)
print_super_pattern("SUPER")