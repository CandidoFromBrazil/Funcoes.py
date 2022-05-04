
def CalculaDelta (coef1,coef2,coef3):
  #Delta = b² - 4.a.c
  delta = coef2*coef2 - 4*coef1*coef3 #A variavel delta, so "vive" enquanto def CalculaDelta estiver em RUNTIME
  return delta

a = eval(input("Entre com o coeficiente a da equação: "))
b = eval(input("Entre com o coeficiente b da equação: "))
c = eval(input("Entre com o coeficiente c da equação: "))

delta = CalculaDelta(a, b, c) #chamando a função (CalculaDelta) no programa principal
#delta != delta into def,
print(f'O valor calculado do delta foi: {delta}')

#delta > 0 : equação tem duas raizes reais
#delta == 0 : equação tem uma raiz real
#delta - 0 : equação não possui raiz real

if delta > 0:
    print("A equação tem duas raizes reais")
elif delta == 0:
    print("A equação tem uma raiz real")
else:
    print("A equação não possui raiz real")


