palavra = input("Digite uma palavra: ")

qtd_letra = palavra.lower().count('a')

existe_a = qtd_letra > 0

if existe_a:
    print(f"A letra 'a' maiúscula ou minúscula ocorre {qtd_letra} vez(es) existe na palavra digitada.")
else:
    print("A letra 'a' maiúscula ou minúscula não existe.")


