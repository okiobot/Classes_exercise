#Senha utilizada para acessar as opções de alteração de dados dos funcionários
senha = 123

subl = ["F1"]

def linha():
    print("="*120)

#Classe pai usadas nas outras classes
class Funcionario():
    def __init__(self, nome, idade = 16, salario = 1000):
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    #Função usada para modificar o nome
    def set_nome(self):
        try:
            linha()
            novonome = input("Digite o novo nome do funcionário: ")
            self.nome = novonome
            print("Nome alterado com sucesso")
        except ValueError:
            print("Valor inválido")
    
    #Função usada para modificar o salário
    def set_salario(self):
        try:
            linha()
            novosalario = float(input("Digite o novo salário do funcionário: "))
            self.salario = novosalario
            print("Salário alterado com sucesso")
        except ValueError:
                print("Valor inválido")
    
    #Função usada para modificar a idade
    def set_idade(self):
        try:
            linha()
            novaidade = int(input("Digite a nova idade do funcionário: "))
            self.idade = novaidade
            print("Idade alterada com sucesso")
        except ValueError:
            print("Valor inválido")
    
    #Função usada para adicionar o bônus ao salário do funcionário
    def bonus(self):
        self.salario = self.salario + (0.20 * self.salario)
    
    #Função usada para escolher e modificar o elemento escolhido
    def mod(self):
        linha()
        w = input("""O que você deseja modificar?
[Nome]
[Salário]
[Idade]                      
""")
        
        #Esta variável torna o input do usuário em maiúsculo, facilitando a leitura 
        change = w.upper()
        if change == "NOME":
            self.set_nome()
        elif change == "SALARIO" or change == "SALÁRIO":
            self.set_salario()
        elif change == "IDADE":
            self.set_idade()
    
    #Função usada para mostrar todas as informações do funcionário
    def tudo(self):
        if self.__class__ == Funcionario:
            linha()
            print(f"O nome do funcionário é: {self.nome} | Idade: {self.idade} | Salário = R${self.salario} | Tipo: Funcionário")
        elif self.__class__ == JovemAprendiz:
            correct = self.__class__.__name__[0:5] + ' ' + self.__class__.__name__[5:]
            linha()
            print(f"O nome do funcionário é: {self.nome} | Idade: {self.idade} | Salário = R${self.salario} | Carga horária: {self.horas}H | Tipo: {correct}")    
        elif self.__class__ == Chefe:
            brackets = str(subl)[1:-1]
            linha()
            print(f"O nome do funcionário é: {self.nome} | Idade: {self.idade} | Salário = R${self.salario} | Seus subordinados são: {brackets} | Tipo: Chefe")
            
#Classe filha de Funcionário    
class JovemAprendiz(Funcionario):
    def __init__(self, nome, idade,salario = 1000,horas = 0):
        super().__init__(nome, idade, salario)
        self.horas = horas        

#Classe filha de Funcionário
class Chefe(Funcionario):
    def __init__(self, nome, idade, salario = 1000, sub = subl ):
        super().__init__(nome, idade, salario)
        self.sub = sub

if __name__ == "__main__":
    F1 = Funcionario("Daniel", 20, 5000)
    F2 = JovemAprendiz("Ana", 17, 1300, 4)
    F3 = Chefe("Maria",36,7000,)

    while True:
        try:
            linha()
            #Input usado para escolher qual ação o usuário deseja realizar
            option = int(input("""Escolha uma das opções:
[1] - Ver todas as informações de um funcionário
[2] - Modificar as informações de um funcionário
[3] - Aplicar um bônus de 20% a um funcionário
"""))
            
            linha()
            #Input usado para ver todas as informações de um funcionário
            if option == 1:
                x = int(input(f"""Escolha o funcionário que você deseja ver as informações: 
[1] - F1
[2] - F2               
[3] - F3
"""))
                if x == 1:
                    F1.tudo()
                elif x == 2:
                    F2.tudo()
                elif x == 3:
                    F3.tudo()
        
            #Input usado para escolher qual funcionário o usuário deseja modificar
            elif option == 2:
                code = int(input("Digite a senha: "))
                if code == senha:
                    linha()
                    mod = int(input(f"""Escolha o funcionário que você deseja modificar as informações: 
[1] - F1
[2] - F2               
[3] - F3
"""))
                else:
                    print("Acesso negado, senha incorreta")
                    continue
                    
                #Dependendo da escolha do usuário, a o elemento respectivo poderá ser modificado
                if mod == 1:
                    F1.mod() 
                if mod == 2:
                    F2.mod()
                if mod == 3:
                    F3.mod()
            
            #Input usado para o usuário escolher qual funcionário deseja aplicar o bônus
            elif option == 3:
                password = int(input("Digite a senha: "))
                if password == senha:
                    linha()
                    y = int(input("""Escolha o funcionário que você deseja aplicar o bônus:
[1] - F1
[2] - F2
[3] - F3
"""))
                    if y == 1:
                        F1.bonus()
                    elif y == 2:
                        F2.bonus()
                    elif y == 3:
                        F3.bonus()
                    print("Bônus aplicado com sucesso")
                
                else:
                    print("Acesso negado, senha incorreta")
                    continue
        
        #Caso o usuário digite algum valor inválido, uma mensagem de erro aparecerá
        except ValueError:
            print("Valor inválido")
                