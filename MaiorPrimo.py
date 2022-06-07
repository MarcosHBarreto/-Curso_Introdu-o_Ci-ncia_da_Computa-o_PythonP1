def maior_primo(x):
    while x >= 2:
        z = x - 1
        x % 1 == 0
        return x


def Primo(y):
    z = 2
    s_primo = 0
    while z < y:
        if y % z == 0:
            break
        else:
            z = z + 1

    if z == y:
        s_primo = False
        return False
    else:
        s_primo = True
        return True