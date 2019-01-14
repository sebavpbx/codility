

def solution(X, A):
    if len(A) >= X:
        pozycje = set()
        licznik = 0
        for element in A:
            pozycje.add(element)
            if len(pozycje) == X:
                return licznik
            licznik += 1
    return -1
