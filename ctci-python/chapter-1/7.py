def solution(m):
    reversed_m = m[::-1]
    transposed_and_reversed_m = zip(*reversed_m)
    return [list(i) for i in transposed_and_reversed_m]

if __name__=='__main__':
    inp = [list('abc'), list('def'), list('ghi')]
    assert solution(inp) == [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f','c']]
