#função multiplicadora
def multi(numerador,multiplicador):
    multiplicado = numerador * multiplicador
    return multiplicado #final da função multi

x = eval(input('Entre com um numerador: '))
y = eval(input('Entre com um multiplicador: '))

multiplicador = multi(x,y) # trazendo a <função <multi>> que é local(dentro da função), para o programa principal!

print(f'{multiplicador}')