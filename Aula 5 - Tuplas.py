# Aula 5 - Tuplas
times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

print(type(times_rj)) # class=’tuple’
print(times_rj) # ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

print(times_rj[2]) # Fluminense

#Tuplas precisam de pelo menos 2 argumentos
objeto_string = ('tesoura')
objeto_tupla = ('tesoura',)

print(type(objeto_string)) # class 'str'
print(type(objeto_tupla)) # class 'tuple'

vogais = ('a', 'e', 'i', 'o', 'u')

print(vogais[1]) # e

vogais = ('a', 'e', 'i', 'o', 'u')
# Tuplas não podem ser alteadas (São Imutáveis)
vogais[1] = 'E'