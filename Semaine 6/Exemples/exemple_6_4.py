def somme_1_a_n(n: int) -> int:

    somme = 0
    for i in range(1, n + 1):
        somme += i  # somme = somme + i
    return somme


print(somme_1_a_n(5))
print(somme_1_a_n(100))
