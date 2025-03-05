#Realiza la división euclideana vista en el curso de matemáticas
#muestra el procedimiento paso por paso
#muestra el Máximo Común Divisor de los números dados
def main():
    a = int(input("Define a: "))
    b = int(input("Define b: "))
    mcd = divide_euc(a, b)
    print("MCD = " + str(mcd))


def divide_euc(a, b):
    q = a // b
    r = a % b
    print(f"{a}/{b} = {q}   r = {r}     {a} = {q}({b}) + {r}")
    if r == 0:
        if b == 1:
            print("Los números son coprimos.")
        return b
    else:
        return divide_euc(b, r)





if __name__ == "__main__":
    main()
