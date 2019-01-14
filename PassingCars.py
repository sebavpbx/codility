

def solution(A):

    listsum = sum(A)
    lenght = len(A)

    if listsum == lenght or listsum == 0 or lenght == 1:
        return 0

    passes = 0

    for element in A:
        if element == 0:
            passes += listsum
            if passes > 1000000000:
                return -1
        elif element == 1:
            listsum -= 1
            if listsum < 1:
                return passes

    return passes

