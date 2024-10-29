import json
import os
carros_json = 'carros.json'


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'



arquivo = os.path.join(os.path.dirname(__file__), 'carros.json')


def carregar_veiculos():
    
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    
    
    with open(arquivo, 'r') as f:
        return json.load(f)

def carregar_carros(placa, modelo,kilometragem):
    carros = carregar_veiculos()

    carros.append({'placa': placa, 'modelo': modelo,'kilometragem':kilometragem})

    with open(arquivo, 'w') as f:
        json.dump(carros, f, indent=4, ensure_ascii=False)
    print("🚗 CARRO ADICIONADO COM SUCESSO!")

def listar_carros():
    carros = carregar_veiculos()

    if carros:
        print("=" *50)
        print(centralizar_texto(cor.AZUL+"LISTA DE CARROS....:"+cor.RESET, largura ))
        print("=" *50)
        print(f"{'Placa':<16}{'Modelo':<15}{'Kilometragem':<15}")
        print("-" * 50)
        for carro in carros:
            
            print(f"{carro['placa']:<17}{carro['modelo']:<15}{carro['kilometragem']:<15}")
            
    else:
        print("🛑 NENHUM VEICULO CADASTRADO.")

def atualizar_carro(placa, km_novo):
    carros = carregar_veiculos()

    for carro in carros:
        if carro['placa'] == placa:
            carro['kilometragem'] = km_novo
            break

    with open(arquivo, 'w') as f:
        json.dump(carros, f, indent=4, ensure_ascii=False)
    print("🚙 VEICULO ATUALIZADO COM SUCESSO!")

def excluir_carro(placa):
    carros = carregar_veiculos()

    for carro in carros:  
        if carro['placa'] == placa:
            carros.remove(carro)

    with open(arquivo, 'w') as f:
        json.dump(carros, f, indent=4, ensure_ascii=False)
    print("🚓 VEICULO EXCLUÍDO COM SUCESSO!")

def buscar_carro(placa):
    carros = carregar_veiculos()
    
    encontrado = False

    for carro in carros:
        

        if carro['placa'] == placa:
            print("-" *50)
            print(f"{'Placa':<16}{'Modelo':<15}{'Kilometragem':<15}")
            print("-" * 50)
            print(f"{carro['placa']:<17}{carro['modelo']:<15}{carro['kilometragem']:<15}")
            encontrado = True
    if not encontrado:
        print("🛴 NENHUM VEICULO CADASTRADO.")
    

def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']

def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO A PERDIDAS LOCADORA DE VEICULOS <<<---- ")
    print("          1 - MÓDULO VEICULO ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)
    
def exibir_menu_veiculo():
    print("\nMENU:")
    print("1. ADICIONAR CARRO")
    print("2. ATUALIZAR  KM DO CARRO PELA PLACA")
    print("3. EXCLUIR CARRO")
    print("4. LISTAR CARROS CADASTRADOS")
    print("5. PROCURAR CARRO PELA PLACA")
    print("6. VOLTAR AO MENU ANTERIOR")

def centralizar_texto(texto, largura):
    return texto.center(largura)

largura = 50


def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match (opcao_inicial):
            

            case 1:
                while True: 
                    exibir_menu_veiculo()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        os.system('cls')
                        print("=" * largura)
                        print(centralizar_texto(cor.VERDE+"ADICIONANDO UM VEICULO....:"+cor.RESET, largura ))
                        print("=" * largura)
                        
                        placa = input(" 🚧 DIGITE A PLACA:\n>>> ")
                        carros = carregar_veiculos()
                        
                        if any(carro['placa'].lower() == placa.lower() for carro in carros):
                            print("🚫 Placa já cadastrada.")
                            opc=input("APERTE ENTER PARA CONTINUAR")
                            if(opc=="enter"):
                                exibir_menu_veiculo()
                            os.system('cls')
                       
                        else:
                            modelo = input(" 🦽 DIGITE O MODELO:\n>>> ")
                            kilometragem = input("⏱ DIGITE A KILOMETRAGEM ATUAL:\n>>> ")
                            carregar_carros(placa, modelo, kilometragem)
                           
                            opc=input("APERTE ENTER PARA CONTINUAR")
                            if(opc=="enter"):
                                exibir_menu_veiculo()
                            os.system('cls')
                   
                    elif opcao == "4":
                        os.system('cls')
                        listar_carros()
                        
                        opc=input("APERTE ENTER PARA CONTINUAR")
                        if(opc=="enter"):
                            exibir_menu_veiculo()
                        os.system('cls')
                    
                    elif opcao == "2":
                        os.system('cls')
                        print("=" * largura)
                        print(centralizar_texto(cor.AMARELO+"ATUALIZANDO....:"+cor.RESET, largura ))
                        print("=" * largura)
                        placa = input("🚧 DIGITE A PLACA DO CARRO A SER ATUALIZADO:\n>>>")
                        carros = carregar_veiculos()
                        if not any(carro['placa'].lower() == placa.lower() for carro in carros):
                            print("🚫 VEICULO NÃO ESTÁ CADASTRADO NA BASE DE DADOS")
                        else:    
                            km_novo = input("⏱ DIGITE A NOVA KILOMETRAGEM:\n>>>")
                            atualizar_carro(placa,km_novo)
                    elif opcao == "3":
                        placa = input("🛺 DIGITE A PLACA DO CARRO A SER EXCLUÍDO:\n>>>")
                        excluir_carro(placa)
                    elif opcao == "5":
                        placa = input("🦼 DIGITE A PLACA DO CARRO:\n>>>")
                        buscar_carro(placa)
                        opc=input("APERTE ENTER PARA CONTINUAR")
                        if(opc=="enter"):
                            
                            exibir_menu_veiculo()
                        os.system('cls')
                    elif opcao == "6":
                        print("🐌 VOLTANDO AO MENU ANTERIOR...")
                        break
                    else:
                        print("❌ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print("🏍 SAINDO...")
                break
            case __:
                print("❌ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()