

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
    max_no = A.count(N + 1)
    if max_no == 0:
        for licznik in range(N):
            counters[licznik] = A.count(licznik + 1)
    else:
        pass
    return counters
    
# lista = [1,2,3,1,6,4,4,4,3,2,1,2,3,3,3,6,1,2,1,1,3,4,5,6,2,3,4,3,3,3,5,6,6,1,2,2,2,3,4,5,5,5,5,6,1,2,3,2,1,1,6,1]
lista = [1,2,3,1,2,4,4,4,3,2,1,2,3,3,3,1,1,2,1,1,3,4,5,5,2,3,4,3,3,3,5,4,3,1,2,2,2,3,4,5,5,5,5,2,1,2,3,2,1,1,1,1]

print(solution(5, lista))
print(solution1(5, lista))