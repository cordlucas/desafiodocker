#!/Users/drade/Desktop/python/.venv/bin/python3

import requests

url = 'http://api.open-notify.org/astros.json'

info = requests.get(url)
# Realiza uma solicitação GET para a URL especificada e armazena a resposta em 'info'.

if info.status_code == 200:
    # Verifica se a resposta da solicitação foi bem-sucedida (código de status 200).

    data = info.json()
    # Converte a resposta JSON em um objeto Python e o armazena na variável 'data'.

    number = data['number']
    # Extrai o número de astronautas no espaço a partir dos dados recebidos e o armazena em 'number'.

    print(f'\nNúmero de astronautas no espaço: {number}')
    
    #CASO QUEIRA VER OS NOMES

    # astronaut_names = [astronaut['name'] for astronaut in data['people']]
    # # Cria uma lista de nomes de astronautas.

    # print('\nNomes dos astronautas no espaço:')
    # # Exibe um cabeçalho.

    # for name in astronaut_names:
    #     print(f'- {name}')

else:
    print('Falha na solicitação da API')
    # Se a solicitação não for bem sucedida, exibe uma mensagem de falha.
