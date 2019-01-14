

def solution(N, A):
    counters = [0]*N
    for element in A:
        if element > N:
            maximum = max(counters)
            counters = [maximum] * N
        else:
            counters[element - 1] += 1
    return counters
