n = int(input('Digite o valor de n: '))

def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n -1
    return fat
print(fatorial(n))