

def solution(A):
    checked = []
    for number in A:
        if number not in checked:
            checked.append(number)
            if A.count(number) % 2 != 0:
                return number
