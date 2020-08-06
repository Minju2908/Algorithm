def convert(n, base):
    T = "01234"
    q, r = divmod(n, base)
    if n%3 == 0:
        q -=1
        r = 3
    if q == 0:
        if r == 3:
            return T[4]
        return T[r]
    else:
        if r == 3:
            return convert(q, base) + T[4]
        return convert(q, base) + T[r]

print(convert(21, 3))

