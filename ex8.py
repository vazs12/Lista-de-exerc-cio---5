nome = input("Digite o seu nome: ")
nota1 = int(input("Digite a sua 1º nota: "))
nota2 = int(input("Digite a sua 2º nota: "))
nota3 = int(input("Digite a sua 3º nota: "))
resultado = (nota1 + nota2 + nota3)/3
if resultado > 7:
    print("Parabéns ",nome, "!", "você foi aprovado(a)")
if resultado ==7>5:
    print("Você ficou com media ", resultado, " e esta de recuperação")
if resultado <5:
    print( nome, " você esta reprovado(a)")