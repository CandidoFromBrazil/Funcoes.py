def nomeidade(): #minha função. Se escreve a função assim sem(<variavel>), somente quando não optar por colocar
    #O que autera a forama como chamamos a  função
    nome = input("Qual o seu nome: ")
    idade = eval(input("Coloque a sua idade: "))
    print(f"{nome}, tem idade igual a {idade},\nPróximo!\n")

#se chama a função assim, somente quando não optar por retorno, assim evitar erros de type e name
nomeidade() #chamando a função
nomeidade() #chamando a função
nomeidade() #chamando a função

