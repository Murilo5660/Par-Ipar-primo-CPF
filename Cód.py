import threading

def par_ou_impar():
    num = int(input("Digite um número para saber se ele é Par ou Ímpar: "))
    if num % 2 == 0:
        print(f"O número {num} é Par")
    else:
        print(f"O número {num} é Ímpar")


def primo():
    numero = int(input("Digite um número para sabe se ele é Primo ou Não: "))
    if numero <= 1:
        print(f"O número {numero} não é Primo")
        return
    if numero == 2:
        print(f"O número {numero} é Primo")
        return
    if numero % 2 == 0:
        print(f"O número {numero} não é Primo")
        return

    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            print(f"O número {numero} não é Primo")
            return
    print(f"O número {numero} é Primo")


def validar_cpf():
    cpf = input("Digite seu CPF para saber se ele é Válido ou Inválido: ")

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        print("CPF Inválido")
        return

    def calcular_digito(cpf, peso_inicial):
        soma = sum(int(dig) * peso for dig, peso in zip(cpf, range(peso_inicial, 1, -1)))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:10], 11)

    if cpf[-2:] == f"{digito1}{digito2}":
        print("CPF Válido")
    else:
        print("CPF Inválido")


# Criando threads para cada função
t1 = threading.Thread(target=par_ou_impar)
t2 = threading.Thread(target=primo)
t3 = threading.Thread(target=validar_cpf)
# Iniciando as threads
t1.start()
t2.start()
t3.start()
# Espera todas terminarem antes de encerrar o programa
t1.join()
t2.join()
t3.join()
#Explicação do uso de threads aqui:
#threading.Thread(target=funcao) → cria uma thread que vai rodar a função funcao.
#start() → inicia a execução da thread.
#join() → faz o programa principal esperar a thread terminar.
#t1 executa par_ou_impar
#t2 executa primo
#t3 executa validar_cpf
