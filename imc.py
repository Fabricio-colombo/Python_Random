def calcula_imc(peso, altura):
    imc = peso / altura**2
    return imc

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = calcula_imc(peso, altura)

print("Seu IMC é: {:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Seu peso está dentro da faixa saudável.")
elif imc < 30:
    print("Você está acima do peso.")
else:
    print("Você está obeso.")
