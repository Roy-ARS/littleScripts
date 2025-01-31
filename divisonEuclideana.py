#Realiza la división euclideana vista en el curso de matemáticas y muestra el procedimiento paso por paso
def main():
    a = int(input("Define a: "))
    b = int(input("Define b: "))
    mcd, interactions = divide_euc(a, b, -1)
    print("MCD = " + str(mcd))


def divide_euc(a, b, inter):
    q = a // b
    r = a % b
    print(f"{a}/{b} = {q}   r = {r}     {a} = {q}({b}) + {r}")
    if r == 0:
        if b == 1:
            print("Los números son coprimos.")
        return b, inter
    else:
        inter += 1
        return divide_euc(b, r, inter)





if __name__ == "__main__":
    main()
