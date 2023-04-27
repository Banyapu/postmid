def mystery(s):
    s = s.lower()
    n = 0
    for c in range(ord("a"), ord("z") + 1):
        if chr(c) in s:
            n += 1
    return n


print(mystery("The quick brown fox jumps over the lazy dog"))
