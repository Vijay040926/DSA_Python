def longest_word_length(s):
    max_length = 0;
    current_length = 0

    for i in range(len(s)):
        if s[i] != ' ':
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0

    if current_length > max_length:
        max_length = current_length

    return max_length


res = longest_word_length("The quick brown fox jumps over the lazy dog")
print(res)