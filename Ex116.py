def print_unicode_characters(start, end):
    for codepoint in range(start, end+1):
        print(chr(codepoint), end=' ')


# Example usage
start_codepoint = 128512
end_codepoint = 128591

print_unicode_characters(start_codepoint, end_codepoint)

