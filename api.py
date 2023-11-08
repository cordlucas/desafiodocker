import requests

def api_astronaut_info():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Falha na solicitação da API de astronautas')
        return None

def api_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Falha na solicitação da API da ISS')
        return None

def numberAstronauts(data):
    if data:
        number = data['number']
        print(f'\nNúmero de astronautas no espaço: {number}')

def astronautNames(data):
    if data:
        names = [astronaut['name'] for astronaut in data['people']]
        print('\nNomes dos astronautas no espaço:')
        for name in names:
            print(f'- {name}')

def iss_position(data):
    if data:
        timestamp = data['timestamp']
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']

        print(f'Timestamp: {timestamp}')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')

def notFound():
    print("Erro, escolha uma das opções!")

def switch_case(case):
    astronaut_all_info = api_astronaut_info()
    iss_all_info = api_iss_position()
    options = {
        '1': numberAstronauts,
        '2': astronautNames,
        '3': iss_position
    }
    
    selected_function = options.get(case, notFound)
    
    if selected_function == notFound:
        selected_function()
    elif case == '1':
        selected_function(astronaut_all_info) 
        #enviando informação da api para a função "numberAstronauts"
    elif case == '2':
        selected_function(astronaut_all_info)
        #enviando informação da api para a função "astronautsNames"
    elif case == '3':
        selected_function(iss_all_info)
        #enviando informação da api (iss) para a função "iss_position"

user_input = input("Escolha uma das opções:\n1 - Número de astronautas no Espaço\n2 - Nome dos astronautas no espaço\n3 - Informações da ISS\nOpção:")
switch_case(user_input)
