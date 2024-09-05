# Criaremos um script que imprimirá na tela o total de 
# horas que uma pessoa # estudou durante um determinado 
# período:

# 1. Crie uma variável chamada "nome" e, usando o método 
# input(), atribua a ela 
# um nome;
nome = input('Digite o seu nome: ')

# 2. Crie uma variável chamada "total_dias" e, usando o 
# método input(), solicite o total de dias dedicados ao 
# estudo por semana;
total_dias = input('Insira o total de dias de estudo: ')

# 3. Crie uma variável chamada "total_horas" e, usando o 
# método input(), solicite a média de horas estudada por 
# dia;
total_horas = input('Insira a média de horas de estudo diária: ')

# 4. Crie uma variável chamada "curso" e, usando o método 
# input(), solicite o título do curso desejado;
curso = input('Insira o curso desejado: ')

# 5. Imprima na tela uma frase informando o nome da 
# estudante, o total_dias dedicados aos estudos, o total 
# horas semanais e o curso.
print('O aluno ',nome, '','estudou um total de', total_dias,'dias','e por',total_horas,'horas ', 'no curso de ',curso)