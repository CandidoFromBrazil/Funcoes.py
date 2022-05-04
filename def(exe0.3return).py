def contagem(n): #variavél da função
    lista = [] #variavél lista (dentro da função)
    for num in range(0,n*6): #comando de repetição for (de 1 até n-y) // continua valendo o n-1, por ser uma lista
        lista.append (num) #.append = O que se quer adicionar na lista// lista.append (num), quero adicionar (num)
        #(lista)=objeto,(.append)=metodo, um metodo é: uma (função), mas de um (objeto-apenas)
    return lista #retorno da variavél lista, sempre que requisitada

print (contagem(10)) #O tamanho da minha lista
q = contagem(5)
print(q)
#@

def AdiconaLista(a):
    z = []
    z.append(a)
    for i in range(10):
        z.append(i)
    return z
u = AdiconaLista(10)
print(u)

