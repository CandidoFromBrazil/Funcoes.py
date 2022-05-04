
def div(numerador, divisor): #div(Váriaveis declaradas da minha função)
    divisao = (numerador/divisor)
    return divisao #retorno de uma terceira variavel, não declarada antes na função

a =  eval(input('Entre com o numerador: '))
b = eval(input('Entre com o numerador: '))

divisao = div(a, b) # "linkando" a função e suas variaveis locais, com a variavel global

print(f'{divisao}')
