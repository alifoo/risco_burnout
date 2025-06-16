from dados_coletados import lista_respostas
import time
from funcoes import *

scores_em_cache = False
lista_respostas_cache = []


# Verifica se o número 'deseja' está entre número inicial e final (inclusive).
def verificar_opcao(opcao, numero_inicial, numero_final):
    if opcao.isdigit():
        opcao = int(opcao)
        return (
            numero_inicial <= opcao <= numero_final
        )  # Retorna true se a opção estiver dentro do range passado, e false do contrário.
    return False


# Função para validar a escolha de continuar ou não no menu.
def verificar_opcao_string(opcao):
    return (
        opcao == "N" or opcao == "S"
    )  # Retorna true se opção for uma das strings válidas e do contrário false


def validar_input_sn(texto_input):
    opcao_valida = False
    opcao_continuar = input(texto_input).upper()

    while opcao_valida == False:
        opcao_valida = verificar_opcao_string(opcao_continuar)
        if not opcao_valida:
            print("Erro! Entrada inválida.")
            opcao_continuar = input(
                "Tente novamente usando apenas os caracteres validos(S/N):\n"
            ).upper()
    return opcao_continuar


def classificar_nivel_risco(resultado):
    if resultado > 20:
        return "Alto risco"
    elif resultado >= 11:
        return "Moderado risco"
    elif resultado >= 0:
        return "Baixo risco"
    else:
        return "Inválido"


def calcular_resultado(pessoa_index):
    resultado = 0
    # cansaço fisico
    if lista_respostas[pessoa_index][1] == "Nunca":
        resultado += 0 * 3
    elif lista_respostas[pessoa_index][1] == "Às vezes":
        resultado += 1 * 3
    elif lista_respostas[pessoa_index][1] == "Frequentemente":
        resultado += 2 * 3
    elif lista_respostas[pessoa_index][1] == "Todos os dias":
        resultado += 3 * 3
    # energia pra tarefas
    if lista_respostas[pessoa_index][2] == "Sim":
        resultado += 0 * 2
    elif lista_respostas[pessoa_index][2] == "Com dificuldade":
        resultado += 1 * 2
    elif lista_respostas[pessoa_index][2] == "Não conseguiu":
        resultado += 2 * 2
    # motivaçao pelo trabalho
    if lista_respostas[pessoa_index][3] == "Sim":
        resultado += 0 * 3
    elif lista_respostas[pessoa_index][3] == "Neutro":
        resultado += 1 * 3
    elif lista_respostas[pessoa_index][3] == "Nada motivado(a)":
        resultado += 2 * 3
    # procrastinaçao
    if lista_respostas[pessoa_index][4] == "Não":
        resultado += 0 * 2
    elif lista_respostas[pessoa_index][4] == "Um pouco":
        resultado += 1 * 2
    elif lista_respostas[pessoa_index][4] == "Sim, constantemente":
        resultado += 2 * 2
    # sentido no trabalho
    if lista_respostas[pessoa_index][5] == "Não":
        resultado += 0 * 3
    elif lista_respostas[pessoa_index][5] == "Às vezes":
        resultado += 1 * 3
    elif lista_respostas[pessoa_index][5] == "Quase sempre":
        resultado += 2 * 3
    # pensamentos negativos
    if lista_respostas[pessoa_index][6] == "Não":
        resultado += 0 * 3
    elif lista_respostas[pessoa_index][6] == "Já tive essa semana":
        resultado += 1 * 3
    elif lista_respostas[pessoa_index][6] == "Tenho todos os dias":
        resultado += 2 * 3
    # isolamento emocional
    if lista_respostas[pessoa_index][7] == "Não":
        resultado += 0 * 2
    elif lista_respostas[pessoa_index][7] == "Levemente":
        resultado += 1 * 2
    elif lista_respostas[pessoa_index][7] == "Muito":
        resultado += 2 * 2
    # isolamento social
    if lista_respostas[pessoa_index][8] == "Não":
        resultado += 0 * 2
    elif lista_respostas[pessoa_index][8] == "Com esforço":
        resultado += 1 * 2
    elif lista_respostas[pessoa_index][8] == "Me isolei totalmente":
        resultado += 2 * 2
    # fez algo prazeroso
    if lista_respostas[pessoa_index][9] == "Sim":
        resultado += 0 * 2
    elif lista_respostas[pessoa_index][9] == "Não tive tempo":
        resultado += 1 * 2
    elif lista_respostas[pessoa_index][9] == "Nem vontade tive":
        resultado += 2 * 2

    return resultado


def calcular_score_individual(pessoa_nome):
    resultado = 0
    risco = ""
    pessoa_index = None

    if "Score" not in lista_respostas[0]:
        lista_respostas[0].append("Score")
    if "Risco" not in lista_respostas[0]:
        lista_respostas[0].append("Risco")

    while pessoa_index is None:
        for lista in lista_respostas:
            if pessoa_nome in lista and pessoa_nome != "Pessoa":
                pessoa_index = lista_respostas.index(lista)
                break
        if not pessoa_index:
            deseja_tentar_novamente = validar_input_sn(
                "Pessoa não encontrada. Deseja tentar um nome diferente? (S/N) "
            )
            if deseja_tentar_novamente == "N":
                return None, None
            pessoa_nome = input("Digite o novo nome para busca: ")

    # primeiro checa o cache
    if len(lista_respostas_cache[pessoa_index]) > 10:
        return (
            lista_respostas_cache[pessoa_index][10],
            lista_respostas_cache[pessoa_index][11],
        )
    if len(lista_respostas[pessoa_index]) > 10:
        return lista_respostas[pessoa_index][10], lista_respostas[pessoa_index][11]
    else:
        resultado = calcular_resultado(pessoa_index)
        risco = classificar_nivel_risco(resultado)

        lista_respostas[pessoa_index].append(str(resultado))
        lista_respostas[pessoa_index].append(risco)
        return resultado, risco


def calcular_lista_respostas_cache():
    global scores_em_cache
    if len(lista_respostas_cache) == 0:
        for pessoa_info in lista_respostas:
            lista_respostas_cache.append(pessoa_info)

    for i, pessoa_info in enumerate(lista_respostas_cache):
        if len(pessoa_info) <= 10 and pessoa_info[0] != "Pessoa":
            resultado = calcular_resultado(i)
            grau_risco = classificar_nivel_risco(resultado)

            pessoa_info.extend([resultado, grau_risco])

    scores_em_cache = True


def calcular_percentual_risco(nivel):
    print(
        "========================== INÍCIO DO CÁLCULO DOS DADOS ==========================\n"
    )
    if scores_em_cache == False:
        calcular_lista_respostas_cache()

    riscoCount = 0
    pessoaCount = 0

    if nivel == "baixo":
        for pessoa_info in lista_respostas_cache:
            if pessoa_info[0] != "Pessoa":
                pessoaCount += 1
            if pessoa_info[0] != "Pessoa" and pessoa_info[11] == "Baixo risco":
                riscoCount += 1
        print(
            f"O percentual de pessoas com nível de risco baixo é de {(riscoCount/pessoaCount)*100:.2f}%.\n"
        )
    elif nivel == "moderado":
        for pessoa_info in lista_respostas_cache:
            if pessoa_info[0] != "Pessoa":
                pessoaCount += 1
            if pessoa_info[0] != "Pessoa" and pessoa_info[11] == "Moderado risco":
                riscoCount += 1
        print(
            f"O percentual de pessoas com nível de risco moderado é de {(riscoCount/pessoaCount)*100:.2f}%.\n"
        )
    elif nivel == "alto":
        for pessoa_info in lista_respostas_cache:
            if pessoa_info[0] != "Pessoa":
                pessoaCount += 1
            if pessoa_info[0] != "Pessoa" and pessoa_info[11] == "Alto risco":
                riscoCount += 1
        print(
            f"O percentual de pessoas com nível de risco alto é de {(riscoCount/pessoaCount)*100:.2f}%.\n"
        )

    print(
        "========================== FIM DO CÁLCULO DOS DADOS ==========================\n"
    )


def exibir_score_individual():
    nome_pessoa = input(
        "Digite o nome da pessoa que deseja calcular o score e nível de risco de burnout: "
    )
    resultado, grau_risco = calcular_score_individual(nome_pessoa)
    if resultado is None or grau_risco is None:
        print("Operação cancelada pelo usuário. Score individual não foi calculado.")
    else:
        print(
            f"O score de burnout de {nome_pessoa} é de {resultado}, resultando em um {grau_risco} de burnout."
        )
    deseja_calcular_novamente = validar_input_sn(
        "Deseja calcular o score de mais uma pessoa? (S/N) "
    )
    if deseja_calcular_novamente == "S":
        exibir_score_individual()


def imprimir_todos_os_scores():
    contador_scores_obtidos = 0
    for pessoa_info in lista_respostas:
        if len(pessoa_info) > 10 and pessoa_info[0] != "Pessoa":
            if contador_scores_obtidos == 0:
                print(
                    "========================== INÍCIO DA IMPRESSÃO DOS DADOS ==========================\n"
                )
            contador_scores_obtidos += 1
            print(
                f"Exibindo informações de {pessoa_info[0]}:\n Score de burnout obtido: {pessoa_info[10]}. Nível de risco: {pessoa_info[11]}.\n\n"
            )
    if contador_scores_obtidos == 0:
        print(
            "Nenhum score ou nível de risco encontrado. Por favor, realize o cálculo de score e nível de risco de ao menos um usuário antes de realizar a impressão dos dados."
        )
    else:
        print(
            "========================== FIM DA IMPRESSÃO DOS DADOS =========================="
        )


def sugerir_minimizacao_sintomas():
    acoes_para_minimizacao = [
        "Evite estudar até tarde e reduza o uso de telas à noite. Incorpore pausas estratégicas durante o dia (técnica Pomodoro, por exemplo).",
        "Organize sua rotina começando por pequenas vitórias, como arrumar a cama ou tomar café — isso ativa o cérebro e gera estímulo. ",
        "Busque aplicar conteúdos em projetos reais, participar de hackathons, ou explorar temas que te inspiram dentro do curso.",
        "Use listas com entregas claras e realistas por dia. Elimine distrações e crie um ambiente de foco (limpo, silencioso, com metas visíveis).",
        "Converse com colegas e professores, entenda o impacto do que você está estudando e crie conexões com seus valores pessoais.",
        "Reconheça o limite entre cansaço e sofrimento. Conversar com alguém que compreenda sua trajetória pode aliviar a sobrecarga emocional.",
        "Mesmo em poucos minutos, práticas como respiração guiada ou alongamentos reduzem o acúmulo emocional.",
        "Uma ligação de 5 minutos ou uma pausa para café com alguém confiável ajuda a recuperar o senso de pertencimento.",
        "Desenhar, ouvir música, assistir algo leve, cozinhar... O prazer gratuito recarrega energia emocional e combate a anedonia.",
    ]

    print(
        "Escolha um dos sintomas do burnout abaixo para obter sugestões de ação para minimizá-lo."
    )
    print(
        "1 - Cansaço Físico\n"
        "2 - Energia para Tarefas\n"
        "3 - Motivação pelo Trabalho\n"
        "4 - Procrastinação\n"
        "5 - Sentido no Trabalho\n"
        "6 - Pensamentos Negativos\n"
        "7 - Isolamento Emocional\n"
        "8 - Isolamento Social\n"
        "9 - Falta de atividades prazerosas\n"
    )
    opcao_valida = False
    opcao_menu = input(
        "Escolha um dos sintomas acima para receber uma sugestão de ação para minimizar efeitos negativos (1-9): \n"
    )

    while opcao_valida == False:
        opcao_valida = verificar_opcao(opcao_menu, 1, 9)
        if not opcao_valida:
            print("Erro! Entrada inválida.")
            opcao_menu = input(
                "Tente novamente usando apenas os números validos (1-9):\n"
            )

    indice_acao = int(opcao_menu) - 1
    print(
        f"Para minimizar os efeitos do sintoma selecionado: {acoes_para_minimizacao[indice_acao]}"
    )


def tela_abertura():
    print(
        r"""
    _   _  _   __ _    ___ ___ ___   ___  ___   ___ ___ ___  ___ ___    ___  ___   ___ _   _ ___ _  _  ___  _   _ _____ 
   /_\ | \| | /_/| |  |_ _/ __| __| |   \| __| | _ \_ _/ __|/ __/ _ \  |   \| __| | _ ) | | | _ \ \| |/ _ \| | | |_   _|
  / _ \| .` |/--\| |__ | |\__ \ _|  | |) | _|  |   /| |\__ \ (_| (_) | | |) | _|  | _ \ |_| |   / .` | (_) | |_| | | |  
 /_/ \_\_|\_/_/\_\____|___|___/___| |___/|___| |_|_\___|___/\___\___/  |___/|___| |___/\___/|_|_\_|\_|\___/ \___/  |_|  
        """
    )
    # Menu interativo
    while True:
        print("Análise de Risco de Burnout - Tela inicial")
        time.sleep(1)
        print("Escolha uma opção:\n")
        time.sleep(1)
        print(
            "1 - Receber sugestão de ação para minimização de sintomas\n"
            "2 - Obter score e nível de risco de burnout individual\n"
            "3 - Imprimir todos os scores e níveis de risco calculados\n"
            "4 - Percentual de pessoas com nível de risco baixo\n"
            "5 - Percentual de pessoas com nível de risco moderado\n"
            "6 - Percentual de pessoas com nível de risco alto\n"
            "7 - Encerrar o programa\n"
        )
        opcao_valida = False

        opcao_menu = input(
            "Digite a opção desejada. Use apenas os números validos (1-7):\n"
        )
        # Estrutura de repetição da pergunta caso valido = false
        while opcao_valida == False:
            opcao_valida = verificar_opcao(opcao_menu, 1, 7)
            if not opcao_valida:
                print("Erro! Entrada inválida.")
                opcao_menu = input(
                    "Tente novamente usando apenas os números validos (1-7):\n"
                )

        opcao_menu = int(opcao_menu)

        # Ação para minimização dos efeitos
        if opcao_menu == 1:
            sugerir_minimizacao_sintomas()

        # Score e nível de risco para pessoa solicitada
        elif opcao_menu == 2:
            exibir_score_individual()

        # Impressão de todas as pessoas (considerando score obtido e classificação de risco)
        elif opcao_menu == 3:
            imprimir_todos_os_scores()

        # Percentual de pessoas com nível de risco baixo
        elif opcao_menu == 4:
            calcular_percentual_risco("baixo")

        # Percentual de pessoas com nível de risco moderado
        elif opcao_menu == 5:
            calcular_percentual_risco("moderado")

        # Percentual de pessoas com nível de risco alto
        elif opcao_menu == 6:
            calcular_percentual_risco("alto")

        # Encerrar o programa caso a opção celecionada seja 7
        else:
            print(
                "Obrigado por utilizar o programa de Análise de Risco de Burnout.\n"
                "Encerrando o programa."
            )
            break
        # Estrutura de repetição da pergunta para continuar
        opcao_continuar = validar_input_sn("\nVoltar para a tela inicial? (S/N)\n")

        # Encerrar o programa caso a resposta para continuar seja N
        if opcao_continuar == "N":
            print(
                "Obrigado por utilizar o programa de Análise de Risco de Burnout.\n"
                "Encerrando o programa."
            )
            break
