class Jogatina:
    def __init__(self, jogadorUm, jogadorDois):
        self.jogadorUm = jogadorUm
        self.jogadorDois = jogadorDois
        self.vitoria = False
        self.opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

    def menu(self):
        print("Bem-vindos ao jogo de Pedra, Papel e Tesoura!")
        print(f"Jogador 1: {self.jogadorUm}")
        print(f"Jogador 2: {self.jogadorDois}")
        print("Escolhas disponíveis: 1 = Pedra, 2 = Papel, 3 = Tesoura")

    def escolha(self, decisaoUm, decisaoDois):
        if self.vitoria:
            print("O jogo já acabou, comece outro.")
            return

        if decisaoUm not in self.opcoes or decisaoDois not in self.opcoes:
            print("Digite um número válido!")
            return

        print(f"{self.jogadorUm} escolheu {self.opcoes[decisaoUm]}")
        print(f"{self.jogadorDois} escolheu {self.opcoes[decisaoDois]}")

        resultado = self.vencedorFinal(decisaoUm, decisaoDois)
        self.vitoria = True
        print(resultado)

    def vencedorFinal(self, decisaoUm, decisaoDois):
        if decisaoUm == decisaoDois:
            return "Empate!"

        if (decisaoUm == 1 and decisaoDois == 3) or (decisaoUm == 2 and decisaoDois == 1) or (decisaoUm == 3 and decisaoDois == 2):
            return f"{self.jogadorUm} vence!"
        else:
            return f"{self.jogadorDois} vence!"

    def limpar_terminal(self):
        print("\n" * 100)