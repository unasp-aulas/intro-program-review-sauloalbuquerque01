def soma_sequencia_ate_n(n):
    return sum(range(n + 1))

def main():
    ultimo_numero = int(input("Digite o último número da sequência: "))
    resultado = soma_sequencia_ate_n(ultimo_numero)
    print("A soma da sequência até", ultimo_numero, "é:", resultado)

if __name__ == "__main__":
    main()
