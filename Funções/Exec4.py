#Exec4 - Miguel Chagas 
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado
num = int(input("Digite um número para calcular o fatorial: "))
print("Fatorial de", num, "é:", fatorial(num))