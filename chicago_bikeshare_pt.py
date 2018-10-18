# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

"""
    Função imprimi a quantidade de amostras especificada

    INPUT:
    samples: lista que será utilizada
    quantity: int. Quantidade de amostras a serem exibidas
    text: str. Padrão de texto a ser exibido
    column: int. Coluna especifica a ser exibida

    OUTPUT:
    Imprimi a quantidade de linhas solicitadas com o texto informado
    e se preenchido a coluna especifica das linhas da lista
"""
def get_samples(samples, quantity,text,column=None ):
    line_number = 0
    for line in range(quantity):
        line_number += 1
        if(column != None):
            print(text.format(line_number,samples[line][column]))
        else:
            print(text.format(line_number,samples[line]))


# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])




input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]
#
#line_number = 0
#for index in get_samples(data_list,20):
#    line_number += 1
#    print("Amostra {}: {}".format((line_number), index))
#

get_samples(data_list,20,"Amostra {}: {}")

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
get_samples(data_list,20,"Amostra {}: {}",-2)

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    for line in range(len(data)):
        column_list.append(data[line][index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
not_especified = 0

gender_list = column_to_list(data_list,-2)

"""
    Utilizamos o for para ler acrescentar 1 as variáveis que server de contadoras para cada tipo de genero que retorna,
    para comparar o genero, deixamos como lowercase para que não tenha problemas de comparacao de texto
"""
for gender in gender_list:
    if(gender.lower() == "male"):
        male += 1
    elif (gender.lower() == "female"):
        female += 1
    else:
        not_especified += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
"""
        Função que recebe uma lista, e quantifica o retorno de generos em uma nova lista.

        INPUT:
        data_list: lista que será utilizada

        OUTPUT:
        Retorna uma nova lista com quantidade de gêneros masculino e feminino respectivamente.
"""
def count_gender(data_list):
    gender_list = column_to_list(data_list,-2)
    male = 0
    female = 0
    not_especified = 0

    for gender in gender_list:
        if(gender.lower() == "male"):
            male += 1
        elif (gender.lower() == "female"):
            female += 1
        else:
            not_especified += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

"""
        Função que recebe uma lista, e retorna gênero mais popular da lista principal

        INPUT:
        data_list: lista que será utilizada

        OUTPUT:
        Retorna uma string com o gênero

        Função utiliza de outra função já criada para obter a quantidade de gêneros da lista
"""
def most_popular_gender(data_list):
    answer = ""
    count_gender_list = count_gender(data_list);

    if(count_gender_list[0] > count_gender_list[1] ):
        answer = "Male"
    elif (count_gender_list[0] == count_gender_list[1] ):
        answer = "Equal"
    else:
        answer = "Female"
    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

#def distinct_items (list):
#    distinct_list = []
#
#    for item in list:
#        if( item not in distinct_list ):
#            distinct_list.append(item)
#    return distinct_list


"""
        Função que retorna um dicionario, que contabiliza quantidade de chaves de uma lista

        INPUT:
        main_list: lista que será utilizada
        main_index: Indice da coluna que será lida da lista principal
        item_list: Lista de itens únicos que serão contabilizados

        OUTPUT:
        Retorna um dicionario com cada item do parametro item_list, como 'Key' e quantidade como valor
        do dicionario

"""
# Foi idealizada anteriormente a Tarefa 12, que na minha visão simplifica essa função criada
def count_items(main_list, main_index, item_list):
    dict = {}
    for item in item_list:
        count = 0
        for main in  main_list:
            if(main[main_index] == item):
                count += 1
        dict[item] = count
    return dict

"""
        Função que retorna uma lista de valores contidas no dicionario

        INPUT:
        item: Lista de itens únicos que foram usadas como chaves no dicionario
        dict: dicionario no qual será utilizado para incluir as valores na lista de retorno

        OUTPUT:
        Retorna lista de valores contidos no dicionario
"""
def dictionary_to_list (item, dict):
    content_list = []
    for key in item:
        if(key in dict):
            content_list.append(dict[key])

    return content_list

#Nessa tarefa busquei todos os tipos de usuários disponiveis na lista principal
#para formar um grafico dinamico

user_types_list = column_to_list(data_list,-3)
types = set(user_types_list)
quantities = count_items(data_list,-3,types)
quantity = dictionary_to_list(types,quantities)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuários')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A informação é falsa, pois no arquivo possui gêneros não informados,que estão em branco, com isso não podemos afirmar que a soma dos dois gêneros(masculino e feminino) é igual a quantidade total da gêneros da lista."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

"""
        Função que retorna uma lista de floats

        INPUT:
        list : lista de valores

        OUTPUT:
        Retorna lista de valores convertidos para float, a partir da parâmetro list
"""
def convert_string_list_to_float_list(list):
    float_list = []
    for item in list:
        float_list.append(float(item))
    return float_list

"""
        Função que retorna tempo máximo de uma viagem

        INPUT:
        trip_list: lista de números (float ou int)

        OUTPUT:
        Retorna o maior valor contido no parâmetro trip_list
"""
def get_max_trip(trip_list):
    max_value = 0.
    for trip in trip_list:
        if(trip > max_value):
            max_value = trip
    return max_value

"""
        Função que retorna tempo minimo de uma viagem

        INPUT:
        trip_list: lista de números (float ou int)

        OUTPUT:
        Retorna o menor valor contido no parâmetro trip_list
"""
def get_min_trip(trip_list):
    min_value = 0.
    for trip in trip_list:
        if (min_value == 0):
            min_value = trip
        elif(trip < min_value):
            min_value = trip
    return min_value

"""
        Função que retorna a média de tempo de uma viagem

        INPUT:
        trip_list: lista de números (float ou int)

        OUTPUT:
        Retorna a média de tempo de valores contidos no parâmetro trip_list
"""
def get_average_trip(trip_list):
    total_duration = 0.
    for trip in trip_list:
        total_duration += trip

    return total_duration/len(trip_list)

"""
        Função que retorna a mediana de tempo de uma viagem

        INPUT:
        trip_list: lista de números (float ou int)

        OUTPUT:
        Retorna a mediana de tempo de valores contidos no parâmetro trip_list
"""
def get_median_trip(trip_duration_list):
# Função foi criada baseada na explicação do Thiago do Prado, no slack
    sorted_list = sorted(trip_duration_list)
    mid = len(sorted_list) // 2
    iseven = len(sorted_list) % 2 == 0
    median_trip = 0.

    if(iseven):
        mid_up = sorted_list[mid]
        mid_down = sorted_list[mid-1]
        median_trip = (mid_up + mid_down) / 2
    else:
        median_trip = sorted_list[mid]

    return median_trip


trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = convert_string_list_to_float_list(trip_duration_list)
min_trip = get_min_trip(trip_duration_list)
max_trip = get_max_trip(trip_duration_list)

"""
        Função lambda que retorna a média de uma lista

        INPUT:
        trip_list: lista de números (float ou int)

        OUTPUT:
        Retorna a média dos valores contidos no parâmetro trip_list
"""
avg = lambda list: sum(list)/len(list)
mean_trip = avg(trip_duration_list)

median_trip = get_median_trip(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list,3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


"""
        Função que retorna duas listas uma com itens únicos e outra com a
        quantidade contabilizadas desses itens

        INPUT:
        column_list: lista de valores ou itens a serem contabilizados

        OUTPUT:
        Retorna duas listas item_types e count_items, respectivamente
        com itens únicos contidas no parametro column_list e lista de inteiros
        contabilização desses itens
"""
def count_items(column_list):
    item_types = []
    count_items = []

    item_types = set(column_list);

    for item in item_types:
        count = 0
        for text in  column_list:
            if(text == item):
                count += 1
        count_items.append(count)

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
