from dados_coletados import lista_respostas

def minimizar_efeitos():
    print("\n--- Ação para minimização dos efeitos ---")
    time.sleep(2)
    print("lógica para 'Ação para minimização dos efeitos' .")


def calcular_score_risco():
    print("\n---Score w nilvel de risco ---")
    time.sleep(2)
    print("lógica para 'Score e nível de risco para pessoa solicitada'.")


def imprimir_pessoas():
    print("\n--- Impressão de todas as pessoas (score e classificação) ---")
    time.sleep(2)
    print("lógica para 'Impressão de todas as pessoas'.")


def calcular_percentual_risco_baixo():
    print("\n--- Percentual de pessoas com nível de risco baixo ---")
    time.sleep(2)
    #print("lógica para 'Percentual de pessoas com nível de risco baixo' .")


def calcular_percentual_risco_moderado():
    print("\n--- Percentual de pessoas com nível de risco moderado ---")
    time.sleep(2)
    print("lógica para 'Percentual de pessoas com nível de risco moderado' .")


def calcular_percentual_risco_alto():
    print("\n--- Percentual de pessoas com nível de risco alto ---")
    time.sleep(2)
    print("lógica para 'Percentual de pessoas com nível de risco alto' .")

def CalculaScoreIndividual(pessoa_nome):
    result = 0
    pesos = [3, 2, 3, 2, 3, 3, 2, 2, 2]
    pessoa = 0
    
    for lista in lista_respostas:
        if pessoa_nome in lista:
            pessoa = lista_respostas.index(lista)
    
    #oh wow essa funçao ta gigante
    #cansaço fisico
    if lista_respostas[pessoa][1] == 'Nunca':
        result += 0 * pesos[0]
    elif lista_respostas[pessoa][1] == 'Às vezes':
        result += 1 * pesos[0]
    elif lista_respostas[pessoa][1] == 'Frequentemente':
        result += 2 * pesos[0]
    elif lista_respostas[pessoa][1] == 'Todos os dias':
        result += 3 * pesos[0]
    #energia pra tarefas
    if lista_respostas[pessoa][2] == 'Sim':
        result += 0 * pesos[1]
    elif lista_respostas[pessoa][2] == 'Com dificuldade':
        result += 1 * pesos[1]
    elif lista_respostas[pessoa][2] == 'Não conseguiu':
        result += 2 * pesos[1]
    #motivaçao pelo trabalho
    if lista_respostas[pessoa][3] == 'Sim':
        result += 0 * pesos[2]
    elif lista_respostas[pessoa][3] == 'Neutro':
        result += 1 * pesos[2]
    elif lista_respostas[pessoa][3] == 'Nada motivado(a)':
        result += 2 * pesos[2]
    #procrastinaçao
    if lista_respostas[pessoa][4] == 'Não':
        result += 0 * pesos[3]
    elif lista_respostas[pessoa][4] == 'Um pouco':
        result += 1 * pesos[3]
    elif lista_respostas[pessoa][4] == 'Sim constantemente':
        result += 2 * pesos[3]
    #sentido no trabalho
    if lista_respostas[pessoa][5] == 'Não':
        result += 0 * pesos[4]
    elif lista_respostas[pessoa][5] == 'Às vezes':
        result += 1 * pesos[4]
    elif lista_respostas[pessoa][5] == 'Quase sempre':
        result += 2 * pesos[4]
    #pensamentos negativos
    if lista_respostas[pessoa][6] == 'Não':
        result += 0 * pesos[5]
    elif lista_respostas[pessoa][6] == 'Já tive essa semana':
        result += 1 * pesos[5]
    elif lista_respostas[pessoa][6] == 'Tenho todos os dias':
        result += 2 * pesos[5]
    #isolamento emocional
    if lista_respostas[pessoa][7] == 'Não':
        result += 0 * pesos[6]
    elif lista_respostas[pessoa][7] == 'Levemente':
        result += 1 * pesos[6]
    elif lista_respostas[pessoa][7] == 'Muito':
        result += 2 * pesos[6]
    #isolamento social
    if lista_respostas[pessoa][8] == 'Não':
        result += 0 * pesos[7]
    elif lista_respostas[pessoa][8] == 'Com esforço':
        result += 1 * pesos[7]
    elif lista_respostas[pessoa][8] == 'Me isolei totalmente':
        result += 2 * pesos[7]
    #fez algo prazeroso
    if lista_respostas[pessoa][9] == 'Sim':
        result += 0 * pesos[8]
    elif lista_respostas[pessoa][9] == 'Não tive tempo':
        result += 1 * pesos[8]
    elif lista_respostas[pessoa][9] == 'Nem vontade tive':
        result += 2 * pesos[8]
        
    return result