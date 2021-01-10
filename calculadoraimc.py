def imc(peso, altura):
  altura_ao_quadrado = altura ** 2
  meu_imc = peso / altura_ao_quadrado
  print(f'Seu IMC é de: {meu_imc:.2f}')
  return meu_imc

def classificacao(meu_imc):
  if meu_imc > 40.0:
    print("Classificado como: Obesidade Grave")
  if meu_imc >= 30.0 and (meu_imc <= 39.9):
    print("Classificado como: Obesidade")
  if meu_imc >= 25.0 and (meu_imc <= 29.9):
    print("Classificado como: Sobrepeso")
  if meu_imc >= 18.5 and (meu_imc <= 24.9):
    print("Classificado como: Normal")
  if meu_imc < 18.5:
    print("Classificado como: Magreza")

meu_imc = imc(68,1.53)
classificacao(meu_imc)
