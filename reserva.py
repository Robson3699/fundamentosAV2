import os
import json
import carro
import usuario

# variável com caminho do arquivo json
arquivo = os.path.join(os.path.dirname(__file__), "reservas.json")

#não possui menu central chamar função por função


#verifica se o arquivo json existe e joga arquivo json para dentro de uma variável
def load_reservas():
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as file:
            json.dump([{"contador":0}], file, indent=2)

    with open(arquivo, "r") as file:
        return json.load(file)

def valida(vetor, valor, keyname): #verifica a existência do usuário ou carro dentro do json, retornando true caso exista
    for elemento in vetor:
        if elemento[keyname] == valor:
            return True
    
    return False

def filtra_reservas(vetor, valor, keyname, modeid):
    novovetor=[]
    for elemento in vetor:
        if elemento[keyname] == valor:
            novovetor.append(elemento)
            if(modeid == True): #se operar com o modeid em True, deve parar a função assim que a primeira reserva for encontrada, pois cada reserva tem um id único
                return novovetor

    return novovetor


def insere_reserva():
    data = load_reservas()
    carros = carro.carregar_veiculos()
    usuarios = usuario.carregar_usuarios()


    
    placa = input("Insira a placa do veículo ")
    
    switch = valida(carros, placa, "placa")
    if (switch == False): 
        print("ERRO! Carro não encontrado")
        return None
    
    cpf = input("Insira o CPF do cliente ")
    
    switch = valida(usuarios, cpf, "cpf")
    if (switch == False): 
        print("ERRO! Cliente não encontrado")
        return None

    data_inicial = input("Insira a data do início de aluguel ")
    data_final = input("Insira a data do fim do aluguel ")
    
    data[0]["contador"]+=1
    id_reserva = f"{(data[0]["contador"]):04d}" #retorna sempre um número com quatro caracteres

    reserva = {
        "idreserva": id_reserva,
        "placa": placa,
        "cpf": cpf,
        "dataaluguel": data_inicial,
        "datadevolucao": data_final,
        
    }

    
    data.append(reserva)
    with open(arquivo, "w") as file:
        json.dump(data, file, indent=2)
    

def exibe_reservas():
    data = load_reservas()
    data.pop(0) #remove o contador de reservas
    
    print("1-Exibir todas as reservas")
    print("2-Exibir reserva por ID da reserva")
    print("3-Exibir reserva por cliente")
    print("4-Exibir reserva por carro")
    print("0-Retornar ao menu anterior")
    
    switch = int(input())

    if (switch == 0):
        return None
    
    match (switch):
        case 1:
            print("ID\tPlaca\tCPF\tReserva\tDevolução")
            for reserva in data:
                print(f"{reserva["idreserva"]}\t{reserva["placa"]}\t{reserva["cpf"]}\t{reserva["dataaluguel"]}\t{reserva["datadevolucao"]}")

        case 2:
            id = input("Insira o ID da reserva: ")
            data = filtra_reservas(data, id, "idreserva", True)
            if(data==[]):
                print("Reserva não encontrada")
            else:
                print("ID\tPlaca\tCPF\tReserva\tDevolução")
                for reserva in data:
                    print(f"{reserva["idreserva"]}\t{reserva["placa"]}\t{reserva["cpf"]}\t{reserva["dataaluguel"]}\t{reserva["datadevolucao"]}")
        case 3:
            cpf = input("Insira o CPF do cliente: ")
            data = filtra_reservas(data, cpf, "cpf", False)
            if(data==[]):
                print("Reserva não encontrada")
            print("ID\tPlaca\tCPF\tReserva\tDevolução")
            for reserva in data:
                print(f"{reserva["idreserva"]}\t{reserva["placa"]}\t{reserva["cpf"]}\t{reserva["dataaluguel"]}\t{reserva["datadevolucao"]}")
        case 4:
            placa = input("Insira a placa do carro: ")
            data = filtra_reservas(data, placa, "placa", False)
            if(data==[]):
                print("Reserva não encontrada")
            print("ID\tPlaca\tCPF\tReserva\tDevolução")
            for reserva in data:
                print(f"{reserva["idreserva"]}\t{reserva["placa"]}\t{reserva["cpf"]}\t{reserva["dataaluguel"]}\t{reserva["datadevolucao"]}")
        case _:
            print("Comando inválido")
        
def atualiza_reserva():
    data = load_reservas()
    counter = data.pop(0) #remove o contador, lembre de inserir após atualizar
    clientes = usuario.carregar_usuarios()
    carros = carro.carregar_veiculos()
    
    reserva = input("Insira o número da reserva: ")
    switch = valida(data, reserva, "idreserva")
    
    if (switch == False):
        print("Reserva não encontrada")
        return None
    
    for i in range(len(data)):
        if data[i]["idreserva"] == reserva:
            save_pos = i #salva a posição do elemento no vetor
            break
    
    print("ID\tPlaca\tCPF\tReserva\tDevolução")
    print(f"{data[save_pos]["idreserva"]}\t{data[save_pos]["placa"]}\t{data[save_pos]["cpf"]}\t{data[save_pos]["dataaluguel"]}\t{data[save_pos]["datadevolucao"]}")

    # copia valores para comparacao e manipulação
    placa = data[save_pos]["placa"]
    cpf = data[save_pos]["cpf"]
    nova_dataa = data[save_pos]["dataaluguel"]
    nova_datad = data[save_pos]["datadevolucao"]

    print("1 - Alterar placa")
    print("2 - Alterar cpf")
    print("3 - Alterar data de reserva")
    print("4 - Alterar data de devolução")
    opcao = input("Insira uma ou mais opções ")

    if "1" in opcao:
        print("Insira uma nova placa ")
        while True:
            placa = input ()
            switch = valida (carros, placa, "placa")

            if (placa.lower() == "sair"):
                return None
                
            if (switch == True):
                break
            else :
                print("Placa não encontrada.")
                print("Insira uma nova placa ou escreva \"sair\" para sair")

    if "2" in opcao:
        print("Insira uma novo CPF ")
        while True:
            cpf = input ()
            switch = valida (clientes, cpf, "cpf")

            if (cpf.lower() == "sair"):
                return None
                
            if (switch == True):
                break
            else :
                print("CPF não encontrado.")
                print("Insira um novo CPF ou escreva \"sair\" para sair")

    if "3" in opcao:
        nova_dataa = input("Insira uma nova data de reserva ")

    if "4" in opcao:
        nova_datad = input("Insira uma nova data de devolução ")

    print("Antiga reserva:")
    print("ID\tPlaca\tCPF\tReserva\tDevolução")
    print(f"{data[save_pos]["idreserva"]}\t{data[save_pos]["placa"]}\t{data[save_pos]["cpf"]}\t{data[save_pos]["dataaluguel"]}\t{data[save_pos]["datadevolucao"]}")
    print("\nNova reserva:")
    print("ID\tPlaca\tCPF\tReserva\tDevolução")
    print(f"{data[save_pos]["idreserva"]}\t{placa}\t{cpf}\t{nova_dataa}\t{nova_datad}")

    switch = input("Confirma? [S/N]\n")

    while True:
        if switch not in ["S","s", "N", "n"]:
            print("Comando Inválido")
        else:
            break

    if (switch.lower() == "n"):
        print("Operação cancelada!")
    else :
        print("Reserva atualizada!")
        data[save_pos]["placa"] = placa
        data[save_pos]["cpf"] = cpf
        data[save_pos]["dataaluguel"] = nova_dataa
        data[save_pos]["datadevolucao"] = nova_datad

        data.insert(0,counter) #reinsere o contador

        with open (arquivo, "w") as file:
            json.dump(data, file, indent=2)

def deleta_reserva():
    data = load_reservas()
    counter = data.pop(0) #remove o contador de reservas e salva para ser reinserido
    reserva = input("Insira o número da reserva: ")
    
    switch = valida(data, reserva, "idreserva")

    if not switch:
        print("Reserva não encontrada")
        return None
    
    for i in range(len(data)):
        if data[i]["idreserva"] == reserva:
            save_pos = i #salva a posição do elemento no vetor
            break
    
    print("Reserva encontrada:")
    print("ID\tPlaca\tCPF\tReserva\tDevolução")
    print(f"{data[save_pos]["idreserva"]}\t{data[save_pos]["placa"]}\t{data[save_pos]["cpf"]}\t{data[save_pos]["dataaluguel"]}\t{data[save_pos]["datadevolucao"]}")
    
    switch = input("Confirma? [S/N]\n")

    while True:
        if switch not in ["S","s", "N", "n"]:
            print("Comando Inválido")
        else:
            break

    if (switch.lower() == "n"):
        print("Operação cancelada!")
    else :
        data.pop(save_pos)
        data.insert(0, counter) #reinsere o contador
        
        with open (arquivo, "w") as file:
            json.dump(data, file, indent=2)


#não possui menu central chamar função por função