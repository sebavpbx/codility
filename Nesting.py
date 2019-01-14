

def solution(A):
    opened = 0
    for element in A:
        if element == '(':
            opened += 1
        else:
            opened -= 1
            if opened < 0:
                return 0
    if opened == 0:
        return 1
    else:
        return 0
