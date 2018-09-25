def solution(inp1, inp2):
    m = {}
    for i in inp1:
        m[i] = m.get(i, 0) + 1
    for i in inp2:
        if i not in m:
            return False
        else:
            m[i] = m.get(i) - 1
            if m[i] == 0:
                del m[i]
    if m.keys():
        return False
    else:
        return True


if __name__=='__main__':
    tests = [
        (('abcd', 'acdc'), False),
        (('abc', 'bac'), True),
        (('a', 'ab'), False),
        (('a1231', 'asdas1324'), False),
        (('', '1'), False),
        (('', ''), True)
    ]
    for i, j in tests:
        assert solution(*i) == j

