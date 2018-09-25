def solution(s):
    char_set = set()
    for i in s:
        if i in char_set:
            char_set.discard(i)
        else:
            char_set.add(i)
    return len(char_set)<2
