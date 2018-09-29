def solution(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    m = [[0 for i in range(l1+1)] for j in range(l2+1)]
    for i in range(l1+1):
        m[0][i] = i
    for j in range(l2+1):
        m[j][0] = j
    for j in range(1, l2+1):
        for i in range(1, l1+1):
            if s2[j-1]!=s1[i-1]:
                m[j][i] = min(m[j-1][i-1], m[j-1][i], m[j][i-1]) + 1
            else:
                m[j][i] = m[j-1][i-1]
    return m[l2][l1]<2


if __name__=='__main__':
    s1 = "abcdefg"
    s2 = "alcdhg"
    assert solution(s1, s2) == False
