

def solution(A):
    temp = [x for x in A if x > 0]
    temp = list(set(temp))
    temp.sort()
    if len(temp) == 0:
        return 1
    else:
        for x in range(len(temp)):
            if temp[x] != x + 1:
                return x + 1
        return len(temp) + 1
