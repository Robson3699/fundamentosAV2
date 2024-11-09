import os
import json
import carro
import usuario

class cor:
    PRETO = '\033[30m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'
    RESET = '\033[0m'


# variável com caminho do arquivo json
arquivo = os.path.join(os.path.dirname(__file__), "reservas.json")



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

def menu_status(status):
    print("=" *80)
    print(f" ---------------------->>> {status} <<<---------------------- ")
    print("=" *80)


def insere_reserva():
    data = load_reservas()
    carros = carro.carregar_veiculos()
    usuarios = usuario.carregar_usuarios()

    os.system("cls")
    menu_status("INSERINDO RESERVA")
    
    placa = input("🚗Insira a placa do veículo\n")
    
    os.system("cls")

    switch = valida(carros, placa, "placa")
    if (switch == False): 
        print("🚫ERRO! Carro não encontrado")
        opc = input("Pressione ENTER para continuar")
        return None
    
    menu_status("INSERINDO RESERVA")
    cpf = input("🧑Insira o CPF do cliente\n")

    os.system("cls")
    
    switch = valida(usuarios, cpf, "cpf")
    if (switch == False): 
        print("🚫ERRO! Cliente não encontrado")
        opc = input("Pressione ENTER para continuar")
        return None

    menu_status("INSERINDO RESERVA")
    data_inicial = input("Insira a data do início de aluguel\n")
    os.system("cls")
    menu_status("INSERINDO RESERVA")
    data_final = input("Insira a data do fim do aluguel\n")
    os.system("cls")
    
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

    menu_status("✔  Reserva inserida com sucesso!")
    print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
    print(f"{reserva["idreserva"]:<15}{reserva["placa"]:<15}{reserva["cpf"]:<15}{reserva["dataaluguel"]:<15}{reserva["datadevolucao"]:<15}")
    opc = input("Pressione ENTER para continuar")
    

    

def exibe_reservas():
    data = load_reservas()
    data.pop(0) #remove o contador de reservas
    
    os.system("cls")
    menu_status("EXIBIR RESERVAS")
    print("1-Exibir todas as reservas")
    print("2-Exibir reserva por ID da reserva")
    print("3-Exibir reserva por cliente")
    print("4-Exibir reserva por carro")
    print("0-Retornar ao menu anterior")
    
    switch = int(input())

    os.system("cls")

    if (switch == 0):
        return None
    
    match (switch):
        case 1:
           
            if (data==[]):
                print("=" *80)
                print("🚫Não há reservas")
                print("=" *80)
            else:
                    print("=" *80)
                    print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
                    print("=" *80)
                    for reserva in data:
                        print(f"{reserva["idreserva"]:<15}{reserva["placa"]:<15}{reserva["cpf"]:<15}{reserva["dataaluguel"]:<15}{reserva["datadevolucao"]:<15}")

        case 2:
            id = input("Insira o ID da reserva:\n")
            data = filtra_reservas(data, id, "idreserva", True)

            os.system("cls")
            if(data==[]):
                print("=" *80)
                print("🚫Reserva não encontrada")
                print("=" *80)
            else:
                print("=" *80)
                print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
                print("=" *80)
                for reserva in data:
                    print(f"{reserva["idreserva"]:<15}{reserva["placa"]:<15}{reserva["cpf"]:<15}{reserva["dataaluguel"]:<15}{reserva["datadevolucao"]:<15}")
        case 3:
            cpf = input("Insira o CPF do cliente:\n")
            data = filtra_reservas(data, cpf, "cpf", False)
            
            os.system("cls")
            if(data==[]):
                print("=" *80)
                print("🚫Reserva não encontrada")
                print("=" *80)
            else:
                print("=" *80)
                print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
                print("=" *80)
                for reserva in data:
                    print(f"{reserva["idreserva"]:<15}{reserva["placa"]:<15}{reserva["cpf"]:<15}{reserva["dataaluguel"]:<15}{reserva["datadevolucao"]:<15}")
        case 4:
            placa = input("Insira a placa do carro:\n")
            data = filtra_reservas(data, placa, "placa", False)
            
            os.system("cls")
            if(data==[]):
                print("=" *80)
                print("🚫Reserva não encontrada")
                print("=" *80)
            else:
                print("=" *80)
                print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
                print("=" *80)
                for reserva in data:
                    print(f"{reserva["idreserva"]:<15}{reserva["placa"]:<15}{reserva["cpf"]:<15}{reserva["dataaluguel"]:<15}{reserva["datadevolucao"]:<15}")
        case _:
            print("🚫Comando inválido!")
    opc = input("Pressione ENTER para continuar")
        
def atualiza_reserva():
    data = load_reservas()
    counter = data.pop(0) #remove o contador, lembre de inserir após atualizar
    clientes = usuario.carregar_usuarios()
    carros = carro.carregar_veiculos()
    
    os.system("cls")
    menu_status("ATUALIZAR RESERVA")
    reserva = input("Insira o número da reserva:\n")
    switch = valida(data, reserva, "idreserva")
    
    os.system("cls")

    if (switch == False):
        print("🚫Reserva não encontrada")
        opc = input("Pressione ENTER para continuar")
        return None
    
    for i in range(len(data)):
        if data[i]["idreserva"] == reserva:
            save_pos = i #salva a posição do elemento no vetor
            break
    
    print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
    print(f"{data[save_pos]["idreserva"]:<15}{data[save_pos]["placa"]:<15}{data[save_pos]["cpf"]:<15}{data[save_pos]["dataaluguel"]:<15}{data[save_pos]["datadevolucao"]:<15}")

    # copia valores para comparacao e manipulação
    placa = data[save_pos]["placa"]
    cpf = data[save_pos]["cpf"]
    nova_dataa = data[save_pos]["dataaluguel"]
    nova_datad = data[save_pos]["datadevolucao"]

    menu_status("ATUALIZANDO RESERVA")

    print("1 - Alterar placa")
    print("2 - Alterar cpf")
    print("3 - Alterar data de reserva")
    print("4 - Alterar data de devolução")
    opcao = input("Insira uma ou mais opções\n")

    os.system("cls")
    if "1" in opcao:
        menu_status("ATUALIZANDO RESERVA")
        print("Insira uma nova placa\n")
        while True:
            placa = input ()
            switch = valida (carros, placa, "placa")

            if (placa.lower() == "sair"):
                return None
                
            if (switch == True):
                break
            else :
                os.system("cls")
                menu_status("ATUALIZANDO RESERVA")
                print("🚫Placa não encontrada.")
                print("Insira uma nova placa ou escreva \"sair\" para sair")
            
        

    os.system("cls")
    if "2" in opcao:
        menu_status("ATUALIZANDO RESERVA")
        print("Insira uma novo CPF\n")
        while True:
            cpf = input ()
            switch = valida (clientes, cpf, "cpf")

            if (cpf.lower() == "sair"):
                return None
                
            if (switch == True):
                break
            else :
                os.system("cls")
                menu_status("ATUALIZANDO RESERVA")
                print("🚫CPF não encontrado.")
                print("Insira um novo CPF ou escreva \"sair\" para sair")
            
    
    os.system("cls")
    if "3" in opcao:
        menu_status("ATUALIZANDO RESERVA")
        nova_dataa = input("Insira uma nova data de reserva\n")

    os.system("cls")
    if "4" in opcao:
        menu_status("ATUALIZANDO RESERVA")
        nova_datad = input("Insira uma nova data de devolução\n")
    
    os.system("cls")
    menu_status("ATUALIZANDO RESERVA")
    
    print("Antiga reserva:")
    print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
    print(f"{data[save_pos]["idreserva"]:<15}{data[save_pos]["placa"]:<15}{data[save_pos]["cpf"]:<15}{data[save_pos]["dataaluguel"]:<15}{data[save_pos]["datadevolucao"]:<15}")
    print("=" *80)
    print("Nova reserva:")
    print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
    print(f"{data[save_pos]["idreserva"]:<15}{placa:<15}{cpf:<15}{nova_dataa:<15}{nova_datad:<15}")

    switch = input("Confirma? [S/N]\n")
    
    os.system("cls")
    while True:
        if switch not in ["S","s", "N", "n"]:
            print("Comando Inválido")
        else:
            break
        switch = input("Confirma? [S/N]\n")
        os.system("cls")

    os.system("cls")

    if (switch.lower() == "n"):
        menu_status("🚫Operação cancelada!")
    else :
        menu_status("✔  Reserva atualizada!")
        data[save_pos]["placa"] = placa
        data[save_pos]["cpf"] = cpf
        data[save_pos]["dataaluguel"] = nova_dataa
        data[save_pos]["datadevolucao"] = nova_datad

        data.insert(0,counter) #reinsere o contador

        with open (arquivo, "w") as file:
            json.dump(data, file, indent=2)
    opc = input("Pressione ENTER para continuar")
    

def deleta_reserva():
    data = load_reservas()
    counter = data.pop(0) #remove o contador de reservas e salva para ser reinserido
    
    os.system("cls")
    menu_status("DELETAR RESERVA")
    reserva = input("Insira o número da reserva:\n")
    
    switch = valida(data, reserva, "idreserva")
    os.system("cls")
    
    if not switch:
        print("🚫Reserva não encontrada")
        opc = input("Pressione ENTER para continuar")
        return None
    
    for i in range(len(data)):
        if data[i]["idreserva"] == reserva:
            save_pos = i #salva a posição do elemento no vetor
            break
    
    menu_status("DELETAR RESERVA")
    print("Reserva encontrada:")
    print(f"{"ID":<15}{"Placa":<15}{"CPF":<15}{"Reserva":<15}{"Devolução":<15}")
    print(f"{data[save_pos]["idreserva"]:<15}{data[save_pos]["placa"]:<15}{data[save_pos]["cpf"]:<15}{data[save_pos]["dataaluguel"]:<15}{data[save_pos]["datadevolucao"]:<15}")
    
    switch = input("Confirma? [S/N]\n")

    os.system("cls")
    while True:
        if switch not in ["S","s", "N", "n"]:
            print("Comando Inválido")
        else:
            break
        switch = input("Confirma? [S/N]\n")
        os.system("cls")

    os.system("cls")
    if (switch.lower() == "n"):
        menu_status("🚫Operação cancelada!")
    else :
        data.pop(save_pos)
        data.insert(0, counter) #reinsere o contador
        menu_status("✔  Reserva deletada")
        
        with open (arquivo, "w") as file:
            json.dump(data, file, indent=2)
    opc = input("Pressione ENTER para continuar")

def main_reserva():
    while True:
        os.system('cls')
        print(cor.CIANO + "=" *80 + cor.RESET)
        print(cor.VERMELHO + " ---------------------->>> MÓDULO RESERVAS <<<---------------------- ")
        print("          1 - LISTAR RESERVAS ")
        print("          2 - INSERIR RESERVAS ")
        print("          3 - ATUALIZAR RESERVAS ")
        print("          4 - REMOVER RESERVAS ")
        print("          5 - SAIR ")
        print(cor.CIANO + "=" *80 + cor.RESET)

        opc = int(input())

        match (opc):
            case 1:
                exibe_reservas()
            case 2:
                insere_reserva()
            case 3:
                atualiza_reserva()
            case 4:
                deleta_reserva()
            case 5:
                break


