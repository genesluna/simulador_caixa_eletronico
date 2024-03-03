from os import system, name
from caixa_eletronico import CaixaEletronico


def limpar_tela():
    # Verifica o sistema operacional e executa o comando apropriado para limpar a tela
    if name == "nt":  # Windows
        system("cls")
    else:  # Mac e Linux
        system("clear")


def voltar():
    print("\n")
    input("Pressione enter para voltar...")
    limpar_tela()


def main():
    # Inicializa o caixa eletrônico com o saldo inicial de R$ 1000
    caixa = CaixaEletronico(1000)

    limpar_tela()

    while True:
        # Apresenta o menu principal
        print("=" * 40)
        print(f"{'Simulador de Caixa Eletrônico':^40}")
        print("=" * 40)
        print("1. Consultar Saldo")
        print("2. Depositar Dinheiro")
        print("3. Sacar Dinheiro")
        print("4. Sair")

        # Solicita a escolha do usuário
        escolha = input("\nEscolha a opção desejada (1-4): ")
        limpar_tela()

        # Executa a ação com base na escolha do usuário
        if escolha == "1":
            # Consulta o saldo e exibe na tela
            print(caixa.consultar_saldo())
            voltar()
        elif escolha == "2":
            # Solicita o valor a ser depositado, realiza o depósito e exibe o resultado
            valor_deposito = input("Digite o valor a ser depositado: ")
            retorno = caixa.depositar(valor_deposito)
            print(retorno)
            voltar()
        elif escolha == "3":
            # Solicita o valor a ser sacado, realiza o saque e exibe o resultado
            valor_saque = input("Digite o valor a ser sacado: ")
            retorno = caixa.sacar(valor_saque)
            print(retorno)
            voltar()
        elif escolha == "4":
            # Exibe mensagem de saída e encerra o loop
            print("Saindo do simulador. Obrigado!")
            break
        else:
            # Mensagem de opção inválida
            print("Opção inválida. Tente novamente.")
            voltar()


if __name__ == "__main__":
    # Chama a função principal quando o script é executado
    main()
