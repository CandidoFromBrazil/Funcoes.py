#Função de cadastro por nome e cpf
def cadastro():
    nome = input("Qual o seu nome: ")
    cpf = eval(input('Qual o seu cpf: '))
    print(f'O seu nomeé: {nome}, e seu cpf: {cpf}')

cadastro() #Com essa chamada toda a <função<cadastro> é requisitada, isso sem return, e sm variaveis declaradas na linha 2!!