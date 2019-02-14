

def solution(A, B, K):
    print(A, B, K)
    difference = B - A
    if K > B:
        return 0
    elif K == B:
        return 1
    else:
        if difference == 0:
            if A % K == 0:
                return 1
            else:
                return 0
        else:
            if K == A:
                if difference < K:
                    return 1
                elif difference == K:
                    return 2
                else:
                    
            
print(solution(4, 14, 12))
