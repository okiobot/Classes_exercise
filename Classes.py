#Classe e defs utilizados no código
class Livros():
    def __init__(self, preco, quant_pags, genero, autor):
        self.preco = preco
        self.quant_pags = quant_pags
        self.genero = genero
        self.autor = autor

    def get_preco(self):
        return self.preco

    def get_autor(self):
        return self.autor

    def get_quantP(self):
        return self.quant_pags

    def get_genero(self):
        return self.genero

#Linha usada para demilitar 
def linha():
    print("="*90)

if __name__ == "__main__":
    Metropolis = Livros("R$50.00", "423", "Ficção científica", "Thea Von Harbou")
    Damas_Noir = Livros("R$75,00", "276", "Mistério/Suspense", "Joyce Carol entre outras")
    PAX = Livros("R$29,99", "236", "Romance", "Sara Pennypacker")
    while True:
    
    #Inputs para o usuário decidir qual livro e qual elemento deseja visualizar    
        linha()
        A = input('''
Escolha quais dos seguintes livros você deseja verificar as informações: 
Metropolis
Damas Noir
Pax
''')
        linha()
        B = input('''
Escolha o elemento que você deseja verificar: 
(Autor, Quantidade de Páginas, Gênero, Preço ou Tudo)  
''')
        linha()
        #Para "arrumar" a escrita do usuário para tornar mais fácil de ser lida pelo código
        escolha_livro = A.upper()
        escolha_opcao = B.upper()

        #Dependendo da escolha do usuário, uma das opções abaixo será escolhida
        if escolha_livro == "PAX":
            if escolha_opcao == "PREÇO":
                print("Este livro custa: " + PAX.get_preco())
            if escolha_opcao == "AUTOR":
                print("O autor(a) deste livro é: " + PAX.get_autor())
            if escolha_opcao == "GENERO":
                print("O genêro do livro é: " + PAX.get_genero())
            if escolha_opcao == "QUANTIDADE DE PAGINAS":
                print("O livro possui: " + PAX.get_quantP() + " páginas")
            if escolha_opcao == "TUDO":
                print("Este livro custa: "+PAX.get_preco())
                print("O autor(a) deste livro é: " +PAX.get_autor())
                print("O genêro do livro é: " +PAX.get_genero())
                print("O livro possui: " + PAX.get_quantP()+ " páginas")
        if escolha_livro == "METROPOLIS":
            if escolha_opcao == "PREÇO":
                print("Este livro custa: " + Metropolis.get_preco())
            if escolha_opcao == "AUTOR":
                print("O autor(a) deste livro é: " + Metropolis.get_autor())
            if escolha_opcao == "GENERO":
                print("O genêro do livro é: " + Metropolis.get_genero())
            if escolha_opcao == "QUANTIDADE DE PAGINAS":
                print("O livro possui: " + (Metropolis.get_quantP()) + " páginas")
            if escolha_opcao == "TUDO":
                print("Este livro custa: "+Metropolis.get_preco())
                print("O autor(a) deste livro é: " +Metropolis.get_autor())
                print("O genêro do livro é: " +Metropolis.get_genero())
                print("O livro possui: " + Metropolis.get_quantP()+" páginas")
        if escolha_livro == "DAMAS NOIR":
            if escolha_opcao == "PREÇO":
                print("Este livro custa: " + Damas_Noir.get_preco())
            if escolha_opcao == "AUTOR":
                print("O autor(a) deste livro é: " + Damas_Noir.get_autor())
            if escolha_opcao == "GENERO":
                print("O genêro do livro é: " + Damas_Noir.get_genero())
            if escolha_opcao == "QUANTIDADE DE PAGINAS":
                print("O livro possui: " + Damas_Noir.get_quantP() + " páginas")
            if escolha_opcao == "TUDO":
                print("Este livro custa: "+Damas_Noir.get_preco())
                print("O autor(a) deste livro é: " +Damas_Noir.get_autor())
                print("O genêro do livro é: " +Damas_Noir.get_genero())
                print("O livro possui: " + Damas_Noir.get_quantP()+" páginas")
             
        #Linha de código utilizada para o usuário decidir se quer continuar pesquisando informações ou finalizar o sistema
        linha()
        C = str(input("Deseja continuar? S/N "))
        finalizar = C.upper()
        if finalizar == "N":
            break
        else:
            pass
    