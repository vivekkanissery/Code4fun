def solution(inp1, inp2):
    if len(inp1)!=len(inp2):
        return False
    test_str = inp1 + inp1
    return inp2 in test_str
