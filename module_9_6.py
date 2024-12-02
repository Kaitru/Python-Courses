def all_variants(text):
    n = len(text)
    for mask in range(1, 2**n):
        subsequence = ''
        for _ in range(n):
            if mask & (1 << _):
                subsequence += text[_]
        yield subsequence

a = all_variants("abc")
for i in a:
    print(i)
