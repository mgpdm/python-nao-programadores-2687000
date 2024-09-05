# Crie uma lista apenas com elementos numéricos
lista = [1,2,3,78,92]
print(lista)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu 
# até agora
lista1 = ['Matheus',4.4, 5,['Citi',3,'Londres','Roma'],0==1,34,5.987]
print(lista1)
# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista1[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
lista2 = [3,'python','yoga',3,9,4,3,'alexa']
lista3 = lista2[0::2]
print(lista3)
# Remova da lista o último item
lista2.pop(-1)
print(lista2)
# Insira na lista um novo item
lista4 = lista2.append('mouse')
print(lista4)
# Remova da lista um item específico
