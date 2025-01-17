nome="teste"
type(nome)
#print(nome)
print(type(nome))

numero= 1j*1J
print(type(numero))

var1 = True
var2 = False

print(type(var1))
print(type(var2))


nome = 'Daniel'
print(nome[0:3]) 

nome = "Daniel"
print(nome[-2])

nome = 'Eduardo'
print("R",nome[3])
print(id(nome))
nome = 'Felipe'
print(id(nome))

#nome = 'Eduardo'
#nome[6] = 'a'

nome_1 = 'Rodrigo'
nome_2 = 'Ana'

print(len(nome_1)) # 7
print(len(nome_2)) # 3

nome = 'Daniel'
sobrenome = 'Silva'

nome_completo = nome + ' ' + sobrenome

print(nome_completo) # Daniel Silva

nome_1 = 'Eduardo'
nome_2 = 'Eduardo'

if nome_1 == nome_2:
    print('iguais')
else:
    print('diferentes')

nome_1 = 'Eduardo'
nome_2 = 'Eduardo'

if nome_1 is nome_2:
    print('iguais')
else:
    print('diferentes')

mensagem = 'Estou aprendendo Python na DevMedia'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem)) # type 'list'
print(nova_mensagem) # ['Estou', 'aprendendo', 'Python', 'na', 'DevMedia']

nome = 'João da Silva'
print(nome)