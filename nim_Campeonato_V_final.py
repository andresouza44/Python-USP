"""
Jogo do Nim:
Tarefa Proposta no Curso da USP (Cousera) Introdução à Ciência da Computação com Python Parte 1
Neta Versão o Computador sempre sai como vencedor

"""
def partida ():
    n = int(input("Quantas peças? " ))
    m = int(input("Limite de peças por jogada? " ))
    saldo = n
    tira=0
    vez = quem_comeca(n,m) # 1 para PC e 2 para Usuario
    while saldo !=0:
        if vez == 1:
            saldo=saldo - computador_escolhe_jogada(saldo,m)
            vez = 2
        else:
            saldo = saldo - usuario_escolhe_jogada(saldo,m)
            vez =1
        if saldo==1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        if saldo!=0 and saldo!=1:
            print("Agora restam",saldo,"peças no tabuleiro.")
            print()
    if vez!=1:
        print("Fim do jogo! O computador ganhou!")
        placar = True
        return placar
    else:
         print("Você ganhou!")
         placar = False
         return placar

def quem_comeca(n,m): # Escolhe quem começa
    print()
    if n%(m+1) == 0:
        vez = 2 # Usuario começa
        print("Voce começa!")
        print()
    else:
        vez = 1 # PC começa
        print("Computador começa!")
        print()
    return vez


def computador_escolhe_jogada(saldo,m): # quantas peças Computador irá retirar
    
    if saldo<=m:
        tira = saldo
    if saldo%(m+1) > 0:
        tira = saldo%(m+1)
    else:
        tira = m 
        
    if tira == 1:
        print("O computador tirou uma peça")
    else:
        print("O computador tirou",tira,"peças")
    vez = 2    
    return tira


def usuario_escolhe_jogada(saldo,m): # usuário escolhe jogada
    tira=m+1
    while (tira> m or tira > saldo or tira<=0):
        tira =int(input("Quantas peças você vai tirar? "))
        print()
        if (tira> m or tira > saldo or tira<=0):
            print("Oops! Jogada inválida! Tente de novo")
            print()            
    if tira == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou",tira,"peças.")
    return tira

def campeonato():
    placarPc = 0
    placarUser = 0
    print("Você escolheu um campeonato!")
    rodada = 1
    while rodada<4:
        print()
        print("**** Rodada",rodada,"****")
        print()
        if partida()== True:                    
            placarPc +=1
        else:
            placarUser +=1
        rodada +=1
    print()    
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você",placarUser,"X",placarPc,"Computador")
       

        
print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("Você conhece o jogo do NIM ? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.")
print("Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um.")
print("Quem tirar as últimas peças possíveis ganha o jogo.")
print()

print("Escolha:")
print("1 - para jogar uma partida isolada.")
print("2 - para jogar um campeonato de 3 rodadas.")

jogo =int(input())

if jogo == 1:
    partida()
else:
    campeonato()



