def solution(m):
    r = len(m)
    c = len(m[0])
    r_null = set()
    c_null = set()
    for i in range(r):
        for j in range(c):
            if m[i][j]==0:
                r_null.add(i)
                c_null.add(j)
    for i in range(r):
        for j in range(c):
            if (i in r_null) or (j in c_null):
                m[i][j] = 0
    return m


if __name__=='__main__':
    test = [
        [1, 2, 3, 0, 5],
        [0, 2, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [4, 1, 3, 4, 5],
        [1, 1, 1, 1, 1]
    ]
    sol = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 2, 3, 0, 5],
        [0, 1, 3, 0, 5],
        [0, 1, 1, 0, 1]
    ]
    try:
        assert solution(test) == sol
    except AssertionError:
        print("expected %s, got %s"%(sol, solution(test)))
