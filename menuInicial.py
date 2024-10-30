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

def menu_inicial():
    print(cor.CIANO + "=" *55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO SISTEMA MERCADO CLEAN <<<---- ")
    print("          1 - MÓDULO CARRO ")
    print("          2 - MÓDULO USUARIO ")
    print("          2 - MÓDULO RESERVA ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" *55 + cor.RESET)

    
    
while True:
        menu_inicial()
        op=input("DIGITE SUA OPCAO: ")
        match op:
         case "1":
          carro.main_carro()
         case "2":
          usuario.main_usuario()
         case "3":
              break
        

        
        
        

