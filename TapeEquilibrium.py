

def solution3(A):
    differences = set()
    suma = sum(A)
    part1 = 0
    for cut in range(len(A) - 1):
        part1 += A[cut]
        part2 = suma - part1
        differences.add(abs(part1 - part2))
    return min(differences)
