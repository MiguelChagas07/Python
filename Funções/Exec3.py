#Exec3 - Miguel Chagas
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
n = int(input("Digite um número: "))
par_ou_impar(n)