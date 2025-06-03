# Atividade de burnout

Pontifícia Universidade Católica do Paraná
BCC – Bacharelado em Ciência da Computação
Raciocínio Algorítmico - Turma “U” – 1ºP
RA BCC Pág.: 1/5

Projeto Colaborativo – 2

Análise Computacional de Risco de Burnout

OBJETIVO: Desenvolver um programa em Python capaz de analisar sintomas
relacionados ao Burnout a partir de uma matriz (lista de listas) realista, calculando
o score por pessoa avaliada, bem como o nível de risco (baixo, moderado, alto),
considerando os pesos fornecidos e sugerindo ações para minimizar o risco.

ETAPAS OBRIGATÓRIAS DA ENTREGA:

1. Código-fonte principal (main.py) – VALOR 5,0 PONTOS
• Leitura da matriz proveniente do arquivo dados_coletados.py
• Chamada das funções desenvolvidas (gravadas em funções.py)
• Menu interativo com usuário abrindo as seguintes opções:
• Ação para minimização dos efeitos (conforme pergunta)
• Score e nível de risco para pessoa solicitada
• Impressão de todas as pessoas (considerando score obtido e
classificação de risco)
• Percentual de pessoas com nível de risco baixo
• Percentual de pessoas com nível de risco moderado
• Percentual de pessoas com nível de risco alto
• Encerrar o programa

2. Biblioteca própria (funções.py) – VALOR 3,0 PONTOS
• Contendo, no mínimo, 7 funções desenvolvidas pela equipe, bem
comentadas e organizadas. Assim:
• TelaAbertura()
• CalculaScoreIndividual()
• ClassificaNivelRisco()
• SugereMinimizacaoSintomas()
• CalculaPercentual()
• AtualizaMatrizScoreRisco()
• ImprimeMatrizScoreRisco()

3. Relatório em .PDF (máximo 2 páginas) – VALOR 2,0 PONTOS
• Nome completo dos integrantes (até 5) e devidamente cadastrados
no Canvas no grupo PROJETO-2;
• Dificuldades encontradas;
• Aprendizado obtido;
• Descrição detalhada do uso de ferramentas de IA e indicação da(s)
ferramenta(s) usada(s) propriamente dita(s);

## REGRAS TÉCNICAS

1. Proibido o uso de bibliotecas externas (NumPy, Pandas, SciPy,etc);
2. Proibido o uso de List Comprehensions
3. Proibido o uso de eval() ou exec();
4. Código modular, limpo e bem comentado;
5. Os programas main.py e funções.py devem funcionar com o arquivo dados_coletados.py padrão (sem alterações nos dados);

## MATERIAIS FORNECIDOS

• dados_coletados.py
• tabela de pesos e níveis de risco

## CRONOGRAMA

• Liberação: 03/06/2025
• Apresentação em aula para Professora: 10/06/2025 – VALE 25% NOTA
• Entrega: 17/06/2025 – mesma data da 2ª Avaliação Parcial - VALE 75% NOTA

## COMPETÊNCIAS DESENVOLVIDAS:

• Lógica algorítmica e modularização
• Manipulação de listas e funções
• Aplicação ética e humana na computação
• Trabalho em equipe e comunicação

## IMPACTO

Este trabalho conecta o pensamento computacional com um tema relevante e
atual: Burnout. Ao usar a programação para analisar dados de saúde mental, o
estudante aprende como a Computação pode trazer melhorias para a vida humana
e não apenas automatizar processos.

Burnout – Contexto atual e Análise de Dados
Burnout é uma síndrome reconhecida pela Organização Mundial da Saúde
(OMS), relacionada ao esgotamento físico e mental provocado por estresse
crônico, especialmente no ambiente de estudo ou trabalho. Ele se manifesta
por sintomas como exaustão constante, desmotivação, sensação de
ineficácia e distanciamento emocional das atividades.
Nos dias de hoje, com rotinas aceleradas, alta pressão por desempenho,
falta de pausas e estímulos constantes por meio da tecnologia, cada vez
mais estudantes e profissionais enfrentam sintomas de burnout, muitas
vezes sem perceber.

Neste contexto, esta matriz fornecida representa um conjunto simulado de
respostas de 120 pessoas a perguntas ligadas a sintomas de Burnout. O
objetivo ao manipular esses dados é obter estatísticas que ajudem a
identificar padrões de risco, compreender como certos comportamentos
se relacionam com níveis de esgotamento e estimular decisões mais
conscientes sobre bem-estar e saúde mental, especialmente em ambientes
acadêmicos e profissionais.

## TABELA DE PESOS E NÍVEIS DE RISCO

Pergunta Peso(0 a 3) Justificativa Pesos das respostas (0, 1, 2 ou 3) Ação para minimização dos efeitos

1. Cansaço físico 3 Principal sintoma de exaustão Nunca: 0, Às vezes: 1, Frequentemente: 2, Todos os dias: 3 Evite estudar até tarde e reduza o uso de telas à noite. Incorpore pausas estratégicas durante o dia (técnica Pomodoro, por exemplo).
2. Energia para tarefas 2 Indica o impacto funcional Sim: 0, Com dificuldade: 1, Não conseguiu: 2 Organize sua rotina começando por pequenas vitórias, como arrumar a cama ou tomar café — isso ativa o cérebro e gera estímulo.
3. Motivação pelo trabalho 3 Indicador chave de desengajamento Sim: 0, Neutro: 1, Nada motivado(a): 2 Busque aplicar conteúdos em projetos reais, participar de hackathons, ou explorar temas que te inspiram dentro do curso.
4. Procrastinação 2 Reflete fuga e baixa produtividade Não: 0, Um pouco: 1, Sim constantemente: 2 Use listas com entregas claras e realistas por dia. Elimine distrações e crie um ambiente de foco (limpo, silencioso, com metas visíveis).
5. Sentido no trabalho 3 Relacionado à autoeficácia reduzida Não: 0, Às vezes: 1, Quase sempre: 2 Converse com colegas e professores, entenda o impacto do que você está estudando e crie conexões com seus valores pessoais.
6. Pensamentos negativos 3 Indica sofrimento mental severo Não: 0, Já tive essa semana: 1, Tenho todos os dias: 2 Reconheça o limite entre cansaço e sofrimento. Conversar com alguém que compreenda sua trajetória pode aliviar a sobrecarga emocional.
7. Isolamento emocional 2 Afeta estabilidade emocional Não: 0, Levemente: 1, Muito: 2 Mesmo em poucos minutos, práticas como respiração guiada ou alongamentos reduzem o acúmulo emocional.
8. Isolamento social 2 Sinal de desconexão afetiva
Não: 0, Com esforço: 1, Me isolei totalmente: 2 Uma ligação de 5 minutos ou uma pausa para café com alguém confiável ajuda a recuperar o senso de pertencimento.
9. Fez algo prazeroso 2 Relaciona-se à anedonia (ausência de prazer)
Sim: 0, Não tive tempo: 1, Nem vontade tive: 2 Desenhar, ouvir música, assistir algo leve, cozinhar... O
prazer gratuito recarrega energia emocional e combate a
anedonia.

Na matriz, um dos principais objetivos é que o programa calcule e atualize a matriz assim: adicione uma coluna chamada score e que armazenará para cada pessoa (cada lista da matriz) o score total de Burnout e uma outra coluna chamada risco que armazenará também para cada pessoa a classificação final em:

Baixo risco (≤ 10),
Moderado risco (11–20),
Alto risco (> 20).

Alguns exemplos:
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
nomes = ["ana", "joão", "bia"]
maiusculos = [nome.upper() for nome in nomes]
nomes_filtrados = [nome for nome in nomes if len(nome) > 3]
