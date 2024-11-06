from IMC_Project.projeto import calcular_imc, classificar_imc

p = input("Insira seu peso em quilograma: ")
a = input("Insira sua altura em metros: ")

peso = float(p)
altura = float(a)

imc = classificar_imc(calcular_imc(peso, altura))

print('De acordo com o seu peso e sua altura voce esta:', imc)