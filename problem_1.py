def main(salario, cargo):
    if cargo == "junior":
        return salario * 1.15
    elif cargo == "pleno":
        return salario * 1.26
    if cargo == "senior":
        return salario * 1.34
    else:
        return salario - 1
