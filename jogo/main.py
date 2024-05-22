from classes import *
jogo = Jogatina("eitô", "clerinton")
jogo.menu()

jogadorUmDecisao = int(input(f"{jogo.jogadorUm} escolha (1 para Pedra, 2 para Papel, 3 para Tesoura): "))
jogo.limpar_terminal()
jogadorDoisDecisao = int(input(f"{jogo.jogadorDois} escolha (1 para Pedra, 2 para Papel, 3 para Tesoura): "))
jogo.limpar_terminal()

jogo.escolha(jogadorUmDecisao, jogadorDoisDecisao)