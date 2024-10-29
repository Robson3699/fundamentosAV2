import json
import os
##from time import sleep


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


# Definindo o caminho do arquivo no escopo global
arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.json')


def carregar_usuarios():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=7)
    
    # Carrega o conteúdo do arquivo
    with open(arquivo, 'r') as f:
        return json.load(f)

def adicionar_usuario(nome, idade, cpf, endereco, tel):
    usuarios = carregar_usuarios()
    usuarios.append({'nome': nome, 'idade': idade, 'cpf': cpf, 'endereco': endereco,'tel':tel})

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=7, ensure_ascii=False)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")
    
def listar_usuarios():
    usuarios = carregar_usuarios()

    if usuarios:
        print("=" *50)
        print("LISTA DE USUÁRIOS:")
        print("-" *50)
        for usuario in usuarios:
            print("*" *50)
            print(f"NOME: {usuario['nome']}\nIDADE: {usuario['idade']}\nCPF: {usuario['cpf']}\nENDERECO: {usuario['endereco']}\nTELEFONE: {usuario['tel']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

def atualizar_usuario(cpf_antigo, novo_nome, nova_idade, novo_cpf,novo_endereco,novo_tel):
    usuarios = carregar_usuarios()
    encontrado=False

    for usuario in usuarios:
        if usuario['cpf'] == cpf_antigo:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            usuario['cpf'] = novo_cpf
            usuario['endereco'] = novo_endereco
            usuario['tel'] = novo_tel
            encontrado=True
            
    if not encontrado:
        return print("USUARIO NAO ENCONTRADO")

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=7, ensure_ascii=False)
    print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_usuario(cpf):
    usuarios = carregar_usuarios()
    exclusao=False
    for usuario in usuarios:  
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            exclusao=True
    if not exclusao:
        return print("USUARIO NAO EXISTE NA BASE DE DADOS")    
            

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=7, ensure_ascii=False)
    print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")

def buscar_usuario(cpf):
    usuarios = carregar_usuarios()
    
    encontrado = False

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("=" *50)
            print("USUARIO ENCONTRADO:")
            print("-" *50)
            print("*" *50)
            print(f"NOME: {usuario['nome']}\nIDADE: {usuario['idade']}\nCPF: {usuario['cpf']}\nENDERECO: {usuario['endereco']}\nTELEFONE: {usuario['tel']}")
            print("*" *50)
            print("=" *50)
            encontrado=True
    if not encontrado:
         print("😒 NENHUM USUÁRIO CADASTRADO.")
         return encontrado
    
def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']

def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO SISTEMA MERCADO CLEAN <<<---- ")
    print("          1 - MÓDULO USUÁRIO ")
    print("          2 - MÓDULO ESTOQUE ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)
    
def exibir_menu_usuario():
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. BUSCAR USUARIO POR CPF")
    print("6. VOLTAR AO MENU ANTERIOR")
def menu_att():
    print("MENU DE ATUALIZACAO INDIVUAL\n")
    print("1. ATUALIZAR TUDO: ")
    print("2. ATUALIZAR NOME: ")
    print("3. ATUALIZAR CPF: ")
    print("4. ATUALIAZAR IDADE: ")
    print("5. ATUALIZAR ENDERECO: ")
    print("6. ATUALIZAR TELEFONE: ")


def main_usuario():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match (opcao_inicial):
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 1:
                while True: 
                    exibir_menu_usuario()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        os.system('cls')
                        print("ADICIONANDO USUARIO\n")
                        nome = input(" DIGITE O NOME:\n>>>").lower()
                        idade = input(" DIGITE A IDADE:\n>>>")
                        idade_int=int(idade)
                        if idade_int<18:
                            os.system('cls')
                            print(cor.VERDE+("VOLTA PARA ESCOLA MLK"))
                            break
                        cpf = input(cor.VERMELHO+"DIGITE O CPF:\n>>>"+cor.RESET)
                        usuarios=carregar_usuarios()
                        if any(usuario['cpf'] == cpf for usuario in usuarios):
                            os.system('cls')
                            print("USUARIO JA CADASTRADO")
                            break
                        endereco = input(" DIGITE O ENDERECO:\n>>>").lower()
                        tel = input(" DIGITE O TELEFONE:\n>>>")
                        adicionar_usuario(nome, idade, cpf, endereco, tel)
                        
                    elif opcao == "2":
                        os.system('cls')
                        listar_usuarios()
                    elif opcao == "3":
                         os.system('cls')
                         cpf_antigo = input(cor.VERMELHO+"DIGITE O CPF A SER ATUALIZADO:\n>>>"+cor.RESET)
                         if buscar_usuario(cpf_antigo) == False:
                             break
                         novo_nome = input("DIGITE O NOVO NOME:\n>>>").lower()
                         nova_idade = input("DIGITE A NOVA IDADE:\n>>>")
                         nova_idade_int=int(nova_idade)
                         if nova_idade_int<18:
                             print("IDADE MENOR QUE 18 ANOS")
                             break
                         novo_cpf = input(cor.VERMELHO+"DIGITE O NOVO CPF:\n>>>"+cor.RESET)
                         novo_endereco = input("DIGITE O NOVO ENDERECO:\n>>>").lower()
                         novo_tel = input("DIGITE O NOVO TELEFONE:\n>>>")
                         atualizar_usuario(cpf_antigo, novo_nome, nova_idade, novo_cpf,novo_endereco,novo_tel)
                    elif opcao == "4":
                        os.system('cls')
                        cpf = input(cor.VERMELHO+"DIGITE O CPF DO USUÁRIO A SER EXCLUÍDO:\n>>>"+cor.RESET)
                        excluir_usuario(cpf)
                    elif opcao == "5":
                        os.system('cls')
                        cpf = input(cor.VERMELHO+"DIGITE O CPF DO USUÁRIO:\n>>>"+cor.RESET)
                        buscar_usuario(cpf)
                    elif opcao == "6":
                        os.system('cls')
                        print("VOLTAR AO MENU ANTERIOR...")
##                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print("🚀 SAINDO...")
 ##               sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main_usuario()
