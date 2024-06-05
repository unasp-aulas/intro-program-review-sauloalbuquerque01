salario = float(input("Qual é o seu salario: "))
cargo = input("Qual é o seu cargo: ")
    
def main(salario, cargo):
    if cargo == "junior":
        return salario * 1.15  
    elif cargo == "pleno":
        return salario * 1.26 
    elif cargo == "senior":
        return salario * 1.34 
    else:
        return -1  
        
    novo_salario = calcular_aumento(salario, cargo)
    if novo_salario == -1:
        return("Cargo invalido!")


