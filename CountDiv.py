

def solution(A, B, K):

    if A == 0:
        addition = 1
    else:
        addition = 0

    difference = B - A

    if K > B:
        if A % K == 0:
            return 1
        else:
            return 0
    elif K == B or ((K == A) and (K == B)):
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
                    return 1 + int(difference / K)
            elif K > A:
                return 1 + int((B - K) / K) + addition
            else:
                if A % K == 0:
                    return int(difference / K + 1) + addition
                else:
                    if B % K == 0:
                        return int(difference / K + 1) + addition
                    else:
                        return int(difference / K) + addition
            
print(solution(1, 1, 1))
