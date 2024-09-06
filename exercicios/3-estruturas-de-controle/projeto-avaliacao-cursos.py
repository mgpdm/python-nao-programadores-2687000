# Nesse desafio você verificará dentro de uma lista se o item está contido nela, 
# caso verdadeiro deverá imprimir na tela essa informação, além disso deverá 
# solicitar avaliação para o item e armazená-la em um dicionário.

# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida 
# na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o 
# valor a nota

cursos = ['Introdução ao PowerBI','Introdução ao SQL','Curso de linguagem R',
          'Lógica de programação','Curso de linguagem .NET']
curso_access = 'Curso de Microsoft Access'
curso_r = 'Curso de linguagem R'
curso_dotnet = 'Curso de linguagem .NET'

notas = {}

if curso_dotnet in cursos:
  print('O curso',curso_dotnet,'está no catálogo. Por favor, avalie.')
  notas[curso_dotnet]=int(input('Por favor, insira a sua nota para o curso de .NET: '))
if notas[curso_dotnet] > 5:
  print('Por gentileza, insira uma nota entre 0 e 5.')
  notas[curso_dotnet]=int(input('Por favor, insira a sua nota para o curso de .NET: '))
if notas[curso_dotnet] <= 5:
  print('Obrigado por avaliar o curso de .NET com a nota',notas[curso_dotnet],'.')

if curso_r in cursos:
  print('O curso',curso_r,'está no catálogo. Por favor, avalie.')
  notas[curso_r]=int(input('Por favor, insira a sua nota para o curso de linguagem R: '))
if notas[curso_r] > 5:
  print('Por gentileza, insira uma nota entre 0 e 5.')
  notas[curso_r]=int(input('Por favor, insira a sua nota para o curso de linguagem R: '))
if notas[curso_r] <= 5:
  print('Obrigado por avaliar o curso de R com a nota',notas[curso_r],'.')

print(notas)