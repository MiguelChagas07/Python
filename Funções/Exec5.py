#Exec5 - Miguel Chagas
def mostrar_nomes(lista):
    for nome in lista:
        print("Nome:", nome)
nomes = []

quantidade = int(input("Quantos nomes você quer digitar? "))
for i in range(quantidade):
    nome = input("Digite um nome: ")
    nomes.append(nome)

mostrar_nomes(nomes)