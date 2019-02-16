

def solution(N, A):
    counters = [0]*N
    maximum = 0
    for element in A:
        if element > N:
            counters = [maximum] * N
        else:
            counters[element - 1] += 1
            if counters[element - 1] > maximum:
                maximum = counters[element - 1]
    return counters

print(solution(5, [1,2,3,1,6,6]))