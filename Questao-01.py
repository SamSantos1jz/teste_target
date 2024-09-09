input_number = int(input("Digite um numero entre [0] e [100]"))

a = 0
b = 1

pertence = False

for _ in range(100):
    if b == input_number:
        pertence = True
        break

    novo_b = a + b #Calcula o proximo valor de B

    # Atualizando a e b
    novo_a = b
    a = novo_a
    b = novo_b

if pertence:
    print("O número digitado pertence à sequência de Fibonacci!")
else:
    print("Desculpe, mas o número digitado NÃO pertence à sequência de Fibonacci!")