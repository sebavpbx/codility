

def solution(X, Y, D):
    diff = Y - X
    counter = diff / D
    if counter * D < diff:
        return counter + 1
    else:
        return counter
