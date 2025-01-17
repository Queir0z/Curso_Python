#Aula - 4
# Lista

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(programadores)) # type ‘list’
print(len(programadores)) # 5
print(programadores[4]) # Luana

#Como Alterar uma lista
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

programadores[1] = 'Carolina'
print(programadores) # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana']

#Adicionando novos argumentos na lista
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana

programadores.append('Renato')
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana', 'Renato']

#Adicionando novos argumentos na lista dizendo a posição
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
programadores.insert(1, 'Rafael')

print(programadores) # ['Victor', 'Rafael', 'Juliana', 'Samuel', 'Caio', 'Luana']

#Removendo argumentos da lista
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

programadores.remove('Victor')
print(programadores) # ['Juliana', 'Samuel', 'Caio', 'Luana']

#Removendo argumentos da lista dizendo a posição
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

programadores.pop(0)
print(programadores) # ['Juliana', 'Samuel', 'Caio', 'Luana']

