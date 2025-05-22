import pandas as pd
# /-----------------/
input_x = False # True se quiser inputs manuais no terminal

print('LISTA\n')
# LISTA [ ]
# Coleção de valores, organizados em ordem
# Acessa os itens pela posição, começa em [ 0 ]
lista1 = [0 , 1, 2, 3, 'João']

# print comum
print(lista1[0], lista1[4])

# print usando f'
print(f'{lista1[0]} {lista1[4]}')

# converter a lista em outros tipos, exemplo str
lista1_str = [str(x) for x in lista1]
print(lista1_str[0] + ' ' + lista1_str[4])

lista1 = [int(lista1_str[0]), int(lista1_str[1]), int(lista1_str[2]), int(lista1_str[3]), lista1_str[4]]

# print com operação numérica
print(f'Soma:{lista1[0] + lista1[2]}')





print('\nDICIONARIO\n')
# DICIONARIO { }
# Cada item tem uma chave e valor -> chave <--> valor
# O acesso é feito pela chave {'chave':'valor']
dicionario1 = {'nome':'Joana','idade':20,'cidade':'Crato'}

print(dicionario1['nome'])



print('\nLISTA [ ] + DICIONÁRIO { }\n')
# LISTA [ ] + DICIONARIO { }

lidic = [{'nome':'Joana','idade': 20,'Cadastro': True},
         {'nome':'Carlos','idade': 30,'Cadastro': False},
         {'nome':'Pedro','idade': 18,'Cadastro': True}]

# f' - > print(f'abc { variavel } abc') -> substitui o que tá dentro da chave pela variável, tipo um .format
print(f'Cadastro de {lidic[0]['nome']}:{lidic[0]['Cadastro']}\n')

# tabela sem pandas

print('Tabela sem pandas')
print(f"{'Nome':<10} {'Idade':<6} {'Cadastro':<8}")
print("-" * 30)
for pessoa in lidic:
    print(f"{pessoa['nome']:<10} {pessoa['idade']:<6} {str(pessoa['Cadastro']):<8}\n")


# tabela com pandas
print('Tabela com pandas')
df = pd.DataFrame(lidic)
print(df)

if input_x == True:
    # input com a intenção de extração de dados pelo console, e não direto no código
    quadrante_lidic = int(input('Qual quadrante da lista_dicionário?(1 a 3): '))
    coluna_lidic = input('Qual coluna da lista_dicionário?(nome,idade,Cadastro): ')

    # se o input da coluna for o mesmo do if, printa o nome do mesmo quadrante selecionado, depois a informação requisitada, se necessário
    if coluna_lidic == 'Cadastro':
        print(f'Cadastro de {lidic[quadrante_lidic]['nome']}:{lidic[quadrante_lidic][coluna_lidic]}')
    if coluna_lidic == 'idade':
        print(f'Idade de {lidic[quadrante_lidic]['nome']}:{lidic[quadrante_lidic][coluna_lidic]}')
    elif coluna_lidic == 'nome':
        print(f'Nome selecionado:{lidic[quadrante_lidic][coluna_lidic]}')




print('\nTUPLA\n')
# TUPLA ( )
# É uma lista, porém imutável
tupla1 = (0, 1, 2, 'Pedro')
print(f'{tupla1[0]},{tupla1[3]}')

print('\nCONJUNTO / SET\n')
# CONJUNTO { }
# Uma coleção sem ordem e sem repetição
# usa {} mas não é dicionário
conjunto1 = {1, 2, 2, 3, 3, 3}
print(conjunto1)
# é basicamente um dicionario sem repetição, e sem especificar um campo


print('\nDATAFRAME\n')
# DATAFRAME ex: df = pd.DataFrame( variável )
# Retorna uma tabela da Lidic

df = pd.DataFrame(lidic)
print('Dataframe exemplo:\n', df)


