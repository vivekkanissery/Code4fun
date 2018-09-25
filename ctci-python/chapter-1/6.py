def solution(s):
    l = []
    p = ''
    count = 0
    for i in s:
        if p==i:
            count += 1
        else:
            if count:
                l.append(p)
                l.append(str(count))
            count = 1
        p = i
    if count:
        l.append(p)
        l.append(str(count))
    return ''.join(l)


if __name__=='__main__':
    tests = [
        ('aabbccc', 'a2b2c3'),
        ('abc', 'a1b1c1'),
        ('', '')
    ]
    for i, j in tests:
        assert solution(i) == j

