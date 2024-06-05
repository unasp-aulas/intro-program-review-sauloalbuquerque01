def calcular_aumento(salario, cargo):
    if cargo == "junior":
        return salario * 1.15  
    elif cargo == "pleno":
        return salario * 1.26 
    elif cargo == "senior":
        return salario * 1.34 
    else:
        return -1  

def main():
    salario = float(input("Qual é o seu salario: "))
    cargo = input("Qual é o seu cargo: ")

    novo_salario = calcular_aumento(salario, cargo)
    if novo_salario == -1:
        print("Cargo invalido!")
    else:
        print("Novo salario: R$ {:.2f}".format(novo_salario))

if __name__ == "__main__":
    main()

