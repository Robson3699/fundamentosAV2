import os
import json
import carro

# variável com caminho do arquivo json
arquivo = os.path.join(os.path.dirname(__file__), "reservas.json")

#verifica se o arquivo json existe e joga arquivo json para dentro de uma variável
def load_reservas():
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as file:
            json.dump([], file, indent=2)

    with open(arquivo, "r") as file:
        return json.load(file)

def insere_reserva():
    data = load_reservas()
    carros = carro.carregar_veiculos()
    switch = False

    id_reserva = f"{(len(data)+1):04d}" #retorna sempre um número com quatro caracteres
    placa = input("Insira a placa do veículo ")
    cpf = input("Insira o CPF do cliente ")
    data_inicial = input("Insira a data do início de aluguel ")
    data_final = input("Insira a data do fim do aluguel ")

    reserva = {
        "IdReserva": id_reserva,
        "Placa": placa,
        "CPF": cpf,
        "DataAluguel": data_inicial,
        "DataDevolucao": data_final,
        "Ativo": True #será usado para esconder reservas canceladas
    }

    for veiculo in carros:
        if reserva["Placa"] == veiculo["placa"]:
            switch = True

    if (switch == True):
        data.append(reserva)
        with open(arquivo, "w") as file:
            json.dump(data, file, indent=2)
    else:
        print("Erro! Veículo não encontrado")

def exibe_reservas():
    data = load_reservas()

    print("1-Exibir reservas ativas")
    print("2-Exibir reservas canceladas")
    print("3-Exibir todas as reservas")
    
    switch = int(input())

    match (switch):
        case 1:
            novovetor = []
            for reserva in data:
                if reserva["Ativo"] == True:
                    novovetor.append(reserva)
            if novovetor == []:
                print("Não há reservas ativas")
            else:
                print("ID\tPlaca\tCPF\tReserva\tDevolução")
                for reserva in novovetor:
                    print(f"{reserva["IdReserva"]}\t{reserva["Placa"]}\t{reserva["CPF"]}\t{reserva["DataAluguel"]}\t{reserva["DataDevolucao"]}")
        
        case 2:
            novovetor = []
            for reserva in data:
                if reserva["Ativo"] == False:
                    novovetor.append(reserva)
            if novovetor == []:
                print("Não há reservas canceladas")
            else:
                print("ID\tPlaca\tCPF\tReserva\tDevolução")
                for reserva in novovetor:
                    print(f"{reserva["IdReserva"]}\t{reserva["Placa"]}\t{reserva["CPF"]}\t{reserva["DataAluguel"]}\t{reserva["DataDevolucao"]}")

        case 3:
            print("ID\tPlaca\tCPF\tReserva\tDevolução")
            for reserva in data:
                print(f"{reserva["IdReserva"]}\t{reserva["Placa"]}\t{reserva["CPF"]}\t{reserva["DataAluguel"]}\t{reserva["DataDevolucao"]}")

insere_reserva()