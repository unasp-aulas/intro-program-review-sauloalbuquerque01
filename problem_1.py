salario = float(input("Qual é o seu salario: "))
cargo = input("Qual é o seu cargo: ")

def main(salario, cargo):
    if cargo == "junior":
        novo_salario = salario * 1.15  
    elif cargo == "pleno":
        novo_salario = salario * 1.26 
    elif cargo == "senior":
        novo_salario = salario * 1.34 
    else:
        return "Cargo invalido!"
    
    return f"O novo salário é: {novo_salario:.2f}"

