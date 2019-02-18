

def solution(N, A):
    counters = [0] * N
    maximum = 0
    for element in A:
        if element > N:
            counters = [maximum] * N
        else:
            counters[element - 1] += 1
            if counters[element - 1] > maximum:
                maximum = counters[element - 1]
    return counters

def solution1(N, A):
    counters = [0] * N
    

print(solution(5, [1,2,3,1,6,6,1,2,1,1,3,4,5,6,6,1,2,2,2,3,4,5,5,5,5,6,6,1]))