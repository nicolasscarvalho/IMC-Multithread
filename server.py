# server.py
import socket
import json
import threading




# process the user data 
class ProcessingDataClient(received):

    def __init__(self):
        self.result = received
        
        self.result['imc'] = generate_imc(received)
        self.result['statusImc'] = analyse_imc(received['imc'])
        self.result['tmb'] = generate_tmb(received)
        self.result['cal'] = generate_cal(received)
        self.result["nutrientes"] = generate_nutrients(received)


    # calculate the IMC value
    def generate_imc(self, dict):
        h = dict['altura']
        p = dict['peso']
        return round(float(p / (h * h)), 2)



    # returns the IMC status
    def analyse_imc(self, imc):
        if imc > 0 and imc < 18.5:
            status = "Abaixo do Peso!"
        elif imc <= 24.9:
            status = "Peso normal!"
        elif imc <= 29.9:
            status = "Sobrepeso!"
        elif imc <= 34.9:
            status = "Obesidade Grau 1!"
        elif imc <= 39.9:
            status = "Obesidade Grau 2!"
        elif imc <= 40.0:
            status = "Obesidade Grau 1!"
        else:
            status = "Valores inválidos"
        return status



    # returns the TMB (Taxa Metabólica Basal)
    def generate_tmb(self, dict):
        sex = dict['sexo']

        if sex in 'Mm':
            tmb = 5 + (10 * dict['peso']) + (6.25 * (dict['altura'] * 100)) - (5 * dict['idade'])

        else:
            tmb = (10 * dict['peso']) + (6.25 * (dict['altura'] * 100)) - (5 * dict['idade']) - 5

        return tmb



    # returns the amount of calories
    def generate_cal(self, dict):
        if dict['nvlAtiv'] == 1:
            fator_ativ = 1.2

        elif dict['nvlAtiv'] == 2:
            fator_ativ = 1.375

        elif dict['nvlAtiv'] == 3:
            fator_ativ = 1.725

        else:
            fator_ativ = 1.9

        return round((dict['tmb'] * fator_ativ), 2)



    # returns the amount of nutrients
    def generate_nutrients(self, dict):
        carb = str(round((dict['cal'] * 0.45), 2))
        prot = str(round((dict['cal'] * 0.3), 2))
        fat = str(round((dict['cal'] * 0.25), 2))

        return {"carboidratos": carb, "proteinas": prot, "gorduras": fat}




# realize the user < --- > server conection
def handle_client(client_socket, addr):
    print('Conectado a {}'.format(str(addr)))

    # recive client data
    received = client_socket.recv(1024).decode()
    print('Os dados recebidos do cliente são: {}'.format(received))

    # server processing
    received = json.loads(received)
    data = ProcessingDataClient(received).result
    print('O resultado do processamento é {}'.format(data))

    # serialising
    result = json.dumps(data)

    # send a result
    client_socket.send(result.encode('ascii'))
    print('Os dados do cliente: {} foram enviados com sucesso!'.format(addr))

    # finish a connection
    client_socket.close()




# create a socket object
print('ECHO SERVER para cálculo do IMC')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# get a local machine name
host = '127.0.0.1'
port = 8000


# bind to the port
server_socket.bind((host, port))


#start listening requests
server_socket.listen()
print('Serviço rodando na porta {}.'.format(port))


while True:
    # establish a connection
    client_socket, addr = server_socket.accept()
    t = threading.Thread(target=handle_client, args=(client_socket, addr))
    t.start()