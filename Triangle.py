

def solution(A):
    A.sort()
    counter = 0
    while counter < len(A) - 2:
        if A[counter] + A[counter + 1] > A[counter + 2]:
            if A[counter + 1] + A[counter + 2] > A[counter]:
                if A[counter + 2] + A[counter] > A[counter + 1]:
                    return 1
        counter += 1
    return 0


