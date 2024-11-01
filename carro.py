import json
import os



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
    if not any(carro['placa'].lower() == placa.lower() for carro in carros):
            print("🚫 VEICULO NÃO ESTÁ CADASTRADO NA BASE DE DADOS")
            opc=input("APERTE ENTER PARA VOLTAR AO MENU INICIAL")
            if(opc=="enter"):
                exibir_menu_veiculo()
            os.system('cls')
            
            
    else:    
        buscar_carro(placa)
        opc=input("Voce deseja excluir? S/N")
        if(opc=="s" or opc=="S"):
            for carro in carros:  
                if carro['placa'] == placa:
                    
                    carros.remove(carro)
            
            with open(arquivo, 'w') as f:
                json.dump(carros, f, indent=4, ensure_ascii=False)
            print("🚓 VEICULO EXCLUÍDO COM SUCESSO!")
            opc=input("APERTE ENTER PARA VOLTAR AO MENU INICIAL")
            if(opc=="enter"):
                exibir_menu_veiculo()
            os.system('cls')
        else:
             exibir_menu_veiculo()
                 



def buscar_carro(placa=None, modelo=None):
    carros = carregar_veiculos()
    
    encontrado = False


    for carro in carros:
        

        if carro['placa'] == placa:
             print("-" *50)
             print(f"{'Placa':<16}{'Modelo':<15}{'Kilometragem':<15}")
             print("-" * 50)
             print(f"{carro['placa']:<17}{carro['modelo']:<15}{carro['kilometragem']:<15}")
             encontrado = True
        elif (carro['modelo'] == modelo):
            
    
             print(f"{carro['placa']:<17}{carro['modelo']:<15}{carro['kilometragem']:<15}")
             encontrado = True    
    if not encontrado:
        print("🛴 NENHUM VEICULO CADASTRADO.")
    

def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']


    
def exibir_menu_veiculo():
    print("\nMENU:")
    print("1. ADICIONAR CARRO")
    print("2. ATUALIZAR  KM DO CARRO PELA PLACA")
    print("3. EXCLUIR CARRO")
    print("4. LISTAR CARROS CADASTRADOS")
    print("5. PROCURAR CARRO PELA PLACA")
    print("6. VERIFICAR CARROS CADASTRADOS POR MODELO")
    print("7. VOLTAR AO MENU ANTERIOR")


def centralizar_texto(texto, largura):
    return texto.center(largura)

largura = 50


def match_2():
    os.system('cls')
    print("=" * largura)
    print(centralizar_texto(cor.AMARELO+"ATUALIZANDO....:"+cor.RESET, largura ))
    print("=" * largura)
    placa = input("🚧 DIGITE A PLACA DO CARRO A SER ATUALIZADO:\n>>>")
    carros = carregar_veiculos()

    if not any(carro['placa'].lower() == placa.lower() for carro in carros):
        print("🚫 VEICULO NÃO ESTÁ CADASTRADO NA BASE DE DADOS")
        opc=input("APERTE ENTER PARA VOLTAR AO MENU INICIAL OU I PARA INSERIR NOVAMENTE A PLACA: \n")
        if(opc=="enter"):
            exibir_menu_veiculo()
        os.system('cls')    
        if(opc=="i" or opc=="I"):
            match_2()
            os.system('cls')

    

    else:    
        km_novo = input("⏱ DIGITE A NOVA KILOMETRAGEM:\n>>>")
        atualizar_carro(placa,km_novo)
        opc=input("APERTE ENTER PARA CONTINUAR: \n")
        if(opc=="enter"):
            exibir_menu_veiculo()
        os.system('cls')


def main_carro():
     while True:  
         exibir_menu_veiculo()
         opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")
         match (opcao):
                
                
                        
            case '1':
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
                    modelo = input(" 🦽 DIGITE O MODELO:\n>>> ").lower()
                    kilometragem = input("⏱ DIGITE A KILOMETRAGEM ATUAL:\n>>> ")
                    carregar_carros(placa, modelo, kilometragem)
                
                    opc=input("APERTE ENTER PARA CONTINUAR")
                    if(opc=="enter"):
                        exibir_menu_veiculo()
                    os.system('cls')
                        
            case '4':
                os.system('cls')
                listar_carros()
                
                opc=input("APERTE ENTER PARA CONTINUAR")
                if(opc=="enter"):
                    exibir_menu_veiculo()
                os.system('cls')
                            
            case '2':
                match_2()
                            
            case  '3':
                os.system('cls')
                placa = input("🛺 DIGITE A PLACA DO CARRO A SER EXCLUÍDO:\n>>>")
                excluir_carro(placa)
                

            case '5':
                os.system('cls')
                print("=" * largura)
                print(centralizar_texto(cor.AZUL+"PROCURANDO VEICULO....:"+cor.RESET, largura ))
                print("=" * largura)
                placa = input("🦼 DIGITE A PLACA DO CARRO:\n>>>").lower()
                buscar_carro(placa)
                opc=input("APERTE ENTER PARA CONTINUAR")
                if(opc=="enter"):
                    
                    exibir_menu_veiculo()
                os.system('cls')
            
            
            case  '6':
                os.system('cls')
                modelo = input("🦼 DIGITE O MODELO DO CARRO:\n>>>").lower()
                print("-" *50)
                print(f"{'Placa':<16}{'Modelo':<15}{'Kilometragem':<15}")
                print("-" * 50)
                buscar_carro(modelo=modelo)
                opc=input("APERTE ENTER PARA CONTINUAR")
                if(opc=="enter"):
                    
                    exibir_menu_veiculo()
                os.system('cls')
            case '7':
                os.system('cls')
                print("🏍 SAINDO...")
                break
               
            case __:
                print("❌ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    main_carro()