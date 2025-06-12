from dados_coletados import lista_respostas
import time
from funcoes import *


def minimizar_efeitos():
    print("\n--- Ação para minimização dos efeitos ---")
    time.sleep(2)
    print("lógica para 'Ação para minimização dos efeitos' .")


def calcular_score_risco():
    print("\n---Score w nivel de risco ---")
    time.sleep(2)
    print("lógica para 'Score e nível de risco para pessoa solicitada'.")


def imprimir_pessoas():
    print("\n--- Impressão de todas as pessoas (score e classificação) ---")
    time.sleep(2)
    print("lógica para 'Impressão de todas as pessoas'.")


def calcular_percentual_risco_baixo():
    print("\n--- Percentual de pessoas com nível de risco baixo ---")
    
    time.sleep(2)
    
    riscoCount = 0
    pessoaCount = 0
    
    for pessoa in lista_respostas:
        if (pessoa[0] != "Pessoa"):
            pessoaCount += 1
            result, risco = CalculaScoreIndividual(pessoa[0])
            if risco == "Baixo risco":
                riscoCount += 1
    
    print(f'O percentual de pessoas com nível de risco baixo é de {(riscoCount/pessoaCount)*100:.2f}%.')
    time.sleep(2)


def calcular_percentual_risco_moderado():
    print("\n--- Percentual de pessoas com nível de risco moderado ---")
    
    time.sleep(2)
    
    riscoCount = 0
    pessoaCount = 0
    
    for pessoa in lista_respostas:
        if (pessoa[0] != "Pessoa"):
            pessoaCount += 1
            result, risco = CalculaScoreIndividual(pessoa[0])
            if risco == "Moderado risco":
                riscoCount += 1
    
    print(f'O percentual de pessoas com nível de risco moderado é de {(riscoCount/pessoaCount)*100:.2f}%.')
    time.sleep(2)


def calcular_percentual_risco_alto():
    print("\n--- Percentual de pessoas com nível de risco alto ---")
    
    time.sleep(2)
    
    riscoCount = 0
    pessoaCount = 0
    
    for pessoa in lista_respostas:
        if (pessoa[0] != "Pessoa"):
            pessoaCount += 1
            result, risco = CalculaScoreIndividual(pessoa[0])
            if risco == "Alto risco":
                riscoCount += 1
    
    print(f'O percentual de pessoas com nível de risco alto é de {(riscoCount/pessoaCount)*100:.2f}%.')
    time.sleep(2)


def CalculaScoreIndividual(pessoa_nome):
    result = 0
    risco = ""
    pesos = [3, 2, 3, 2, 3, 3, 2, 2, 2]
    pessoa_index = None

    while pessoa_index is None:
        for lista in lista_respostas:
            if pessoa_nome in lista and pessoa_nome != "Pessoa":
                pessoa_index = lista_respostas.index(lista)
                break
        if not pessoa_index:
            deseja_tentar_novamente = input(
                "Pessoa não encontrada. Deseja tentar um nome diferente? (S/N) "
            ).upper()
            while deseja_tentar_novamente != "N" and deseja_tentar_novamente != "S":
                print("Opção inválida! Tente novamente respondendo com S ou N.")
                deseja_tentar_novamente = input(
                    "Pessoa não encontrada. Deseja tentar um nome diferente? (S/N) "
                ).upper()
            if deseja_tentar_novamente == "N":
                return
            pessoa_nome = input("Digite o novo nome para busca: ")

    if lista_respostas[pessoa_index][1] == "Nunca":
        result += 0 * pesos[0]
    elif lista_respostas[pessoa_index][1] == "Às vezes":
        result += 1
    elif lista_respostas[pessoa_index][1] == "Frequentemente":
        result += 2
    elif lista_respostas[pessoa_index][1] == "Todos os dias":
        result += 3
    # energia pra tarefas
    if lista_respostas[pessoa_index][2] == "Sim":
        result += 0
    elif lista_respostas[pessoa_index][2] == "Com dificuldade":
        result += 1
    elif lista_respostas[pessoa_index][2] == "Não conseguiu":
        result += 2
    # motivaçao pelo trabalho
    if lista_respostas[pessoa_index][3] == "Sim":
        result += 0
    elif lista_respostas[pessoa_index][3] == "Neutro":
        result += 1
    elif lista_respostas[pessoa_index][3] == "Nada motivado(a)":
        result += 2
    # procrastinaçao
    if lista_respostas[pessoa_index][4] == "Não":
        result += 0
    elif lista_respostas[pessoa_index][4] == "Um pouco":
        result += 1
    elif lista_respostas[pessoa_index][4] == "Sim constantemente":
        result += 2
    # sentido no trabalho
    if lista_respostas[pessoa_index][5] == "Não":
        result += 0
    elif lista_respostas[pessoa_index][5] == "Às vezes":
        result += 1
    elif lista_respostas[pessoa_index][5] == "Quase sempre":
        result += 2
    # pensamentos negativos
    if lista_respostas[pessoa_index][6] == "Não":
        result += 0
    elif lista_respostas[pessoa_index][6] == "Já tive essa semana":
        result += 1
    elif lista_respostas[pessoa_index][6] == "Tenho todos os dias":
        result += 2
    # isolamento emocional
    if lista_respostas[pessoa_index][7] == "Não":
        result += 0
    elif lista_respostas[pessoa_index][7] == "Levemente":
        result += 1
    elif lista_respostas[pessoa_index][7] == "Muito":
        result += 2
    # isolamento social
    if lista_respostas[pessoa_index][8] == "Não":
        result += 0
    elif lista_respostas[pessoa_index][8] == "Com esforço":
        result += 1
    elif lista_respostas[pessoa_index][8] == "Me isolei totalmente":
        result += 2
    # fez algo prazeroso
    if lista_respostas[pessoa_index][9] == "Sim":
        result += 0
    elif lista_respostas[pessoa_index][9] == "Não tive tempo":
        result += 1
    elif lista_respostas[pessoa_index][9] == "Nem vontade tive":
        result += 2

    if result <= 10:
        risco = "Baixo risco"
    elif 11 <= result <= 20:
        risco = "Moderado risco"
    elif result > 20:
        risco = "Alto risco"

    return result, risco


def TelaAbertura():
    # Verifica se o número 'deseja' está entre 1 e 7 (inclusive).
    def verificar_opcao_int(opcao):
        if opcao.isdigit():
            opcao = int(opcao)
            return (
                1 <= opcao <= 7
            )  # Retorna true se a opção estiver dentro do range de 1 e 7, e false do contrário.
        return False

    # Função para validar a escolha de continuar ou não no menu.
    def verificar_opcao_string(opcao):
        return (
            opcao == "N" or opcao == "S"
        )  # Retorna true se opção for uma das strings válidas e do contrário false

    # Menu interativo
    while True:
        print("Bem Vindo ao programa de Análise de Risco de Burnout!")
        # time.sleep(3)
        print("Pronto para começar?")
        # time.sleep(2)
        print("Escolha uma opção:")
        # time.sleep(1)
        menu_interativo = print(
            "1 - Ação para minimização dos efeitos\n"
            "2 - Score e nível de risco para pessoa solicitada\n"
            "3 - Impressão de todas as pessoas (considerando score obtido e classificação de risco)\n"
            "4 - Percentual de pessoas com nível de risco baixo\n"
            "5 - Percentual de pessoas com nível de risco moderado\n"
            "6 - Percentual de pessoas com nível de risco alto\n"
            "7 - Encerrar o programa\n"
        )
        # time.sleep(1)

        opcao_valida = False

        opcao_menu = input(
            "Digite a opção desejada. Use apenas os números validos (1-7):\n"
        )
        # Estrutura de repetição da pergunta caso valido = false
        while opcao_valida == False:
            opcao_valida = verificar_opcao_int(opcao_menu)
            if not opcao_valida:
                print("Erro! Entrada inválida.")
                opcao_menu = input(
                    "Tente novamente usando apenas os números validos (1-7):\n"
                )

        opcao_menu = int(opcao_menu)
        # Ação para minimização dos efeitos
        if opcao_menu == 1:
            pass
            # SugereMinimizacaoSintomas()
        # Score e nível de risco para pessoa solicitada
        elif opcao_menu == 2:
            nome_pessoa = input(
                "Digite o nome da pessoa que deseja calcular o score e nível de risco de burnout: "
            )
            resultado = CalculaScoreIndividual(nome_pessoa)
            print(resultado)
        # Impressão de todas as pessoas (considerando score obtido e classificação de risco)
        elif opcao_menu == 3:
            pass
            # ImprimeMatrizScoreRisco()
        # Percentual de pessoas com nível de risco baixo
        elif opcao_menu == 4:
            calcular_percentual_risco_baixo()
        # Percentual de pessoas com nível de risco moderado
        elif opcao_menu == 5:
            calcular_percentual_risco_moderado()

        # Percentual de pessoas com nível de risco alto
        elif opcao_menu == 6:
            calcular_percentual_risco_alto()
        # Encerrar o programa caso a opção celecionada seja 7
        else:
            print(
                "Encerrando o programa.\n"
                "Obrigado pela participação no programa de Análise de Risco de Burnout.\n"
                "Tenha um otimo dia, até mais!"
            )
            break

        opcao_valida = False

        # Estrutura de repetição da pergunta para continuar
        opcao_continuar = input("\nVoltar para a tela inicial? (S/N)\n").upper()

        while opcao_valida == False:
            opcao_valida = verificar_opcao_string(opcao_continuar)
            if not opcao_valida:
                print("Erro! Entrada inválida.")
                opcao_continuar = input(
                    "Tente novamente usando apenas os caracteres validos(S/N):\n"
                ).upper()

        # Encerrar o programa caso a resposta para continuar seja N
        if opcao_continuar == "N":
            print(
                "Encerrando o programa.\n"
                "Obrigado pela participação no programa de Análise de Risco de Burnout.\n"
                "Tenha um otimo dia, até mais!"
            )
            break
