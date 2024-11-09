import carro
import usuario
import reserva
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

def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO A PERDIDAS LOCADORA DE VEICULOS <<<---- ")
    print("          1 - MÓDULO CARRO ")
    print("          2 - MÓDULO USUARIO ")
    print("          3 - MÓDULO RESERVA ")
    print("          4 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)

    
    
def main():
    while True:
            os.system('cls')
            menu_inicial()
            op=input("DIGITE SUA OPCAO: ")
            match op:
                case "1":
                    os.system('cls')
                    carro.main_carro()
                case "2":
                    os.system('cls')
                    usuario.main_usuario()
                case "3":
                    os.system('cls')
                    reserva.main_reserva()  
                case "4":
                    break

        
if __name__ == "__main__":
    main()

        
        
        

