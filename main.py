# -*- coding: utf-8 -*-

import time
from funcoes import *


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
    time.sleep(1)

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

    # Ação para minimização dos efeitos
    if opcao_menu == 1:
        minimizar_efeitos()

    # Score e nível de risco para pessoa solicitada
    elif deseja == 2:
        from funções import score_risco

        print("\n---Score w nilvel de risco ---")
        time.sleep(2)

        print("lógica para 'Score e nível de risco para pessoa solicitada'.")

    # Impressão de todas as pessoas (considerando score obtido e classificação de risco)
    elif deseja == 3:
        from funções import imprimir_pessoas

        print("\n--- Impressão de todas as pessoas (score e classificação) ---")
        time.sleep(2)

        print("lógica para 'Impressão de todas as pessoas'.")

    # Percentual de pessoas com nível de risco baixo
    elif deseja == 4:
        from funções import percentual_risco_baixo

        print("\n--- Percentual de pessoas com nível de risco baixo ---")
        time.sleep(2)

        print("lógica para 'Percentual de pessoas com nível de risco baixo' .")

    # Percentual de pessoas com nível de risco moderado
    elif deseja == 5:
        from funções import percentual_risco_moderado

        print("\n--- Percentual de pessoas com nível de risco moderado ---")
        time.sleep(2)

        print("lógica para 'Percentual de pessoas com nível de risco moderado' .")

    # Percentual de pessoas com nível de risco alto
    elif deseja == 6:
        from funções import percentual_risco_alto

        print("\n--- Percentual de pessoas com nível de risco alto ---")
        time.sleep(2)

        print("lógica para 'Percentual de pessoas com nível de risco alto' .")

    # Encerrar o programa caso a opção celecionada seja 7
    else:
        print(
            "Encerrando o programa.\n"
            "Obrigado pela participação no programa de Análise de Risco de Burnout "
            "Tenha um otimo dia, até mais!"
        )
        time.sleep(3)
        break
    # Estrutura de repetição da pergunta para continuiar
    Continue = input("\nVoltar para o menu? (S/N)\n").upper()

    valido_continue = comparaçao2(Continue)  # quando true, volta ao menu interativo

    # estrurura de repetição da pergunta caso a letra dada naão seja S/N
    while valido_continue == False:
        Continue = input("ERRO!!!! Use N para não ou S para sim.\n").upper()
        valido_continue = comparaçao2(Continue)

    # Encerrar o programa caso a resposta para continuar seja N
    if Continue == "N":
        print(
            "Encerrando o programa.\n"
            "Obrigado pela participação no programa de Análise de Risco de Burnout "
            "Tenha um otimo dia, até mais!"
        )
        time.sleep(3)
        break
