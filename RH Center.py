import os
import time
import csv

funcionarios = []

def linha():
    print("=" * 60)

def titulo(texto):
    limpar_tela()
    linha()
    print(texto.center(60))
    linha()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def ler_funcionarios_csv():
    funcionarios = []

    try:
        with open("funcionarios.csv","r", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                funcionarios.append({
                    "Nome" : linha["Nome"],
                    "Idade" : int(linha["Idade"]),
                    "Salario_bruto" : float(linha["Salario_bruto"])
                })

    except FileNotFoundError:
        pass

    return funcionarios

def cad_funcionarios () :

    while True:

        titulo("CADASTRO DE FUNCIONÁRIOS")

        nome = input("Informe o nome completo: ")
        
        while True :
            try :
                salario_bruto = float(input("Infome sua renda Bruta: "))
                idade = int(input("Informe sua idade: "))
                
                if idade <=0 or idade >100 :
                    print("Idade Invalida, Por favor digite novamente: ")
                    continue
            
                break
            except ValueError:
                print("Informe um valor Válido")
                time.sleep(1.2)
 
        funcionarios.append({
            "Nome": nome,
            "Idade": idade,
            "Salario_bruto": salario_bruto
        })

        arquivo = "funcionarios.csv"
        existe = os.path.exists(arquivo)
        vazio = os.path.getsize(arquivo) == 0 if existe else True


        with open (arquivo, "a", newline="") as funcionario :
            cadastro = csv.DictWriter(funcionario, fieldnames=["Nome", "Idade", "Salario_bruto"])

            if vazio:
                cadastro.writeheader()
            
            cadastro.writerow({
                "Nome": nome,
                "Idade": idade,
                "Salario_bruto": salario_bruto
            })
         
        print("Funcionário Cadastrado\n")

        opcao_cad_funcionario = int(input("Pressione (1) para novo cadastro ou (0) para voltar ao menu: "))

        if opcao_cad_funcionario == 0 :
            print("Retornando . . . . .\n")
            time.sleep(1.2)
            limpar_tela()
            return

def relatorios () :
    
    dados = ler_funcionarios_csv()

    while True :
        titulo("RELATÓRIOS")

        print("\nSetor de Relatórios, escolha uma das opções abaixo:")
        opcao_relatorio = int(input("( 1 ) - Média Salarial \n( 2 ) - Nome e Idade do Funcionario com maior salário \n( 3 ) - Total de Funcionários Cadastrados \n( 4 ) - Voltar \n( 0 ) Sair\n"))

        if len(dados) == 0 and opcao_relatorio in (1, 2, 3):
            print("\nNão há funcionários cadastrados!\n")
            input("\nPressione ENTER para voltar ao menu...")
            continue
         
        if opcao_relatorio == 1 :
           media_salario = sum(f["Salario_bruto"] for f in dados) / len (dados)
           # Formata com duas casas, troca ponto por vírgula
           media_formatada = f"{media_salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
           print(f"\nMédia Salarial: R$ {media_formatada}\n")
           input("\nPressione ENTER para voltar ao menu...")

        elif opcao_relatorio == 2 :
           maior = max(dados, key=lambda f: f["Salario_bruto"])
           valor_formatado = f"{maior['Salario_bruto']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
           print(f"\nNome: {maior['Nome']} - Idade: {maior['Idade']} - Salário: R$ {valor_formatado}\n")
           input("\nPressione ENTER para voltar ao menu...")

        elif opcao_relatorio == 3 :
           total_funcionarios = len(dados)
           print(f"\nTotal de Funcionários: {total_funcionarios}\n")
           input("\nPressione ENTER para voltar ao menu...")

        elif opcao_relatorio == 4 :
           return

        elif opcao_relatorio == 0 :
           return "sair"

        else :
            print("\n Opção invalida")
            input("\nPressione ENTER para voltar ao menu...")

def main () :
      
    while True:
        
        try:
            titulo("SISTEMA RH CENTER")

            print("Seja Bem-Vindo ao RH CENTER selecione uma das opções abaixo: ")
            opcao = int(input("( 1 ) - Cadastrar Funcionário \n( 2 ) - Relatório de Funcionários \n( 0 ) - Sair \n"))
        
            if opcao == 1 :
                cad_funcionarios()

            elif opcao == 2 :
                resultado = relatorios()
                if resultado == "sair":
                    print("\nObrigado por usar nossos recursos\n")
                    break

            elif opcao == 0 :
                print("\nObrigado por usar nossos recursos\n")
                break
            else :
                print("Opção Invalida")
                return

        except ValueError:
            print("Opção Invalida")
            time.sleep(1.2)

if __name__ == "__main__":
    main()