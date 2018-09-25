def solution(s):
    char_set = set()
    for i in s:
        if i in char_set:
            return False
        else:
            char_set.add(i)
    return True


if __name__=='__main__':
    tests = [
        ("abcd", True),
        ("aaa", False),
        ("", True),
        ("aba", False)
    ]
    for i, o in tests:
        assert solution(i)==o
