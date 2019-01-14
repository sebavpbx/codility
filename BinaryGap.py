

def solution(A):

    numbers = str(bin(A))[2:]
    lenght = len(numbers)
    maxgap = lenght - 2

    if lenght > 2 and '0' in numbers and '1' in numbers:
        while maxgap > 0:
            if ('1' + maxgap * '0' + '1') in numbers:
                return maxgap
            else:
                maxgap -= 1
        return 0
    else:
        return 0
