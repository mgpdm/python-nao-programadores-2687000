# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário 
# e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, 
# ano atual e os cursos realizados no LinkedIn Learning separados por virgula em 
# ordem cronológica
dados = {}
dados['nome'] = input('Insira seu nome: ')
dados['ano_em_que_conheceu_o_LinkedIn'] = int(input('Insira o ano em que conheceu o LinkedIn: '))
dados['ano_atual'] = int(input('Insira o ano atual '))
cursos = input('Insira os cursos feitos no LinkedIn (separados por vírgula)')

dados['cursos']= cursos.split(', ')

# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, 
# total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e 
# último curso.
print(f"Oi {dados['nome']}, desde {dados['ano_em_que_conheceu_o_LinkedIn']} você conhece o LinkedIn. Nesses {dados['ano_atual'] - dados['ano_em_que_conheceu_o_LinkedIn']} anos, você realizou {len(dados['cursos'])} cursos, sendo o primeiro curso '{dados['cursos'][0]}' e último '{dados['cursos'][-1]}'.")