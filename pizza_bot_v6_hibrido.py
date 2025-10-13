import spacy
from spacy.pipeline import EntityRuler

# --- Bloco de Definições: O cardápio, Preços, IA e Ferramentas --- 

# 1. Configurações da IA (Analisador de Pedidos)
print("Carregando o modelo de linguagem...")
nlp = spacy.load("pt_core_news_lg") 

SABORES = ["MUSSARELA", "CALABRESA", "FRANGO", "PORTUGUESA", "CHOCOLATE BRANCO"]
TAMANHOS = ["PEQUENA", "MÉDIA", "GRANDE"]
BORDAS = ["CATUPIRY", "CHEDDAR", "CHOCOLATE BRANCO", "NENHUMA"]
BEBIDAS = ["COCA-COLA", "GUARANÁ", "CERVEJA"]

patterns = []

for sabor in SABORES:
    patterns.append({"label": "SABOR", "pattern": sabor})

for tamanho in TAMANHOS:
    patterns.append({"label": "TAMANHO", "pattern": tamanho})

for borda in BORDAS:
    patterns.append({"label": "BORDA", "pattern": borda})

for bebida in BEBIDAS:
    patterns.append({"label": "BEBIDAS", "pattern": bebida})


ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns)
print("Cérebro carregado com sucesso!")


# 2. Tabela de Preços (Nossa "Fonte da verdade para valores") 
PRECOS_TAMANHO = {"PEQUENA": 25.00, "MÉDIA": 40.00, "GRANDE": 50.00}
PRECOS_BORDA = {"CATUPIRY": 5.00, "CHEDDAR": 8.00, "CHOCOLATE BRANCO": 10.00, "NUTELLA": 12.00, "NENHUMA": 0.00}
PRECOS_BEBIDA = {"COCA-COLA": 10.00, "GUARANÁ": 7.00, "CERVEJA": 5.00, "NENHUMA": 0.00}


# 3. Funções: A Nossa Ferramentas de Perguntas e Validações
def fazer_pergunta_validada(pergunta, opcoes_validas): 
    while True:
        print(pergunta)
        print(f"As opções são: {', '.join(opcoes_validas).replace('_', ' ')}.")
        resposta = input("> ").strip().upper()

        if resposta in opcoes_validas:
            print(f"\nEntendi, você escolheu {resposta.title()}.")
            return resposta # Sucesso! Devolve a resposta e encerra a função.
            
        else:
            print(f"\nOps! Resposta inválida. Por favor, escolha uma das opções disponíveis.")

# --- INÍCIO DO PROGRAMA PRINCIPAL ---

# --- Bloco 1: Boas-vindas e Nome ---
print("\n-----------------------------------------")
print(" Bem-vindo à Pizzaria do Gemini! (v6 - Híbrido)")
print("-----------------------------------------")
print(f"Olá! Sou a Inteligencia Artificial da Pizzaria Gemini. Qual o seu nome?\n")
nome_cliente = input("> ").strip().title()
preco_total = 0.0

# CORAÇÃO DO BOT HÍBRIDO: Análise de Texto com IA
#1. O PRONTUÁRIO DO PEDIDO (Estrutura de Dados)
#Usamos um dicionario para guardar as informações. 'None" significa que ainda não temos o valor.

pedido = { # Esta é a mudança mais importante do bot híbrido. Em vez de multiplas variáveis, usamos um dicionário.
    "SABOR": None,
    "TAMANHO": None,
    "BORDA": "NENHUMA", # valor padrão, pode ser alterado pela IA ou pelo cliente
    "BEBIDA": "NENHUMA" # valor padrão, pode ser alterado pela IA ou pelo cliente
}

#2. A ANAMNESE (Coleta de Dados) (A pergunta aberta)
print(f"\nPrazer, {nome_cliente}! Sou um bot especialista em pizzas. O que você gostaria de pedir hoje?")
frase_pedido = input("> ") # Simples mas poderoso, damos ao usuário a liberdade de escrever o que quiser.

#3. O DIAGNÓSTICO (Análise do Texto com IA)
# Passamos a frase para a IA processar. Usamos .upper() para combinar com nossos padrões em maiúsculas
doc = nlp(frase_pedido.upper()) # O momento mágico onde a IA lê e interpreta a frase.

#4. O RECEITUÁRIO (Interpretação dos Resultados)
# Agora, vamos verificas quais entidades nosso "Professor Particular" encontrou.
for ent in doc.ents: # O loop que inspeciona os resultados da IA
    if ent.label_ in pedido: # Se a entidade é uma que nos interessa (SABOR, TAMANHO, BORDA, BEBIDA)
        texto_entidade = ent.text.replace("MEDIA", "MÉDIA") # Corrige possíveis erros de acentuação
        pedido[ent.label_] = texto_entidade # A linha que efetivamente conecta o cérebro ao corpo. Ela pega a entidade encontrada e a coloca no prontuário do pedido.

#5. A CHECAGEM E O INTERROGATÓRIO (A rede de segurança)
# Agora, vamos garantir que temos todas as informações necessárias. Se faltar algo, perguntamos.
print("\nEntendido. Deixe-me apenas confirmar alguns detalhes...")
# --- Especialista em Sabores ---
# Chega se o SABOR ainda está vazio (None) no nosso prontuário
if pedido["SABOR"] is None:
    # Se estiver vazio, fazemos a pergunta validada
    print("\n[Lógica de Regras ATIVADA]: Não identifiquei o sabor.") # Indicador visual para o usuário
    # Usamos nossa função antiga e confiável para fazer a pergunta.
    # O resultado preencherá a lacuna e ir direto para o prontuário do pedido.
    pedido["SABOR"] = fazer_pergunta_validada("Qual sabor você gostaria?", SABORES)

# --- Especialista em TAMANHOS ---
# Checa se o TAMANHO ainda está vazio (None) no nosso prontuário
if pedido["TAMANHO"] is None:
    # Se estiver vazio, o especialista em tamanho faz a pergunta validada
    print("\n[Lógica de Regras ATIVADA]: Não identifiquei o tamanho.") # Indicador visual para o usuário
    # A pergunta de tamanho é especial (P, M, G), então nao usamos a função genérica
    # Reutilizamos a lógica exata do pizza_bot para esta tarefa específica.
    while True:
        print(f"Qual seria o tamanho da pizza?")
        print(f"Digite P para Pequena, M para Média ou G para Grande.")
        tamanho_pizza = input("> ").strip().upper()

        # A grande mudança: em vez de salvar em "tamanho_escolhido", salvamos direto no prontuário do pedido.
        if tamanho_pizza == "P":
            pedido["TAMANHO"] = "PEQUENA"
            break # 'break' encerra o loop assim que temos uma resposta válida
        elif tamanho_pizza == "M":
            pedido["TAMANHO"] = "MÉDIA"
            break
        elif tamanho_pizza == "G":
            pedido["TAMANHO"] = "GRANDE"
            break
        else:
            # Se a resposta for inválida, o loop continua, perguntando de novo
            print(f"\nOpção inválida. Por favor, Digite P, M ou G.")

print(f"\nDEBUG: Estado final do pedido antes do cálculo de preços: {pedido}\n") # Linha de debug para ver o estado do pedido+

# 6. O TRATAMENTO (Cálculo do Preço)
# Agora que temos todas as informações, vamos calcular o preço total.
# Usamos try/except para garantir que não haverá erros se algo inesperado acontecer.
try:
    #1. CÁLCULO FINAL DE PREÇOS
    # Buscamos os valores diretamente do nosso dicionário de 'pedido'
    preco_total = 0.0 # Reiniciamos o preço total
    preco_total += PRECOS_TAMANHO[pedido["TAMANHO"]] # Preço do tamanho
    preco_total += PRECOS_BORDA[pedido["BORDA"]] # Preço da borda
    preco_total += PRECOS_BEBIDA[pedido["BEBIDA"]] # Preço da bebida

    #2. APRESENTAÇÃO DO RESUMO (A parte mais importante para o cliente)
    # Também lemos os valores do dicionário de 'pedido'
    print(f"\nPerfeito, {nome_cliente}! Confirmando seu pedido:")
    print("----------- RESUMO DO PEDIDO ------------")
    print(f"-Pizza: {pedido['SABOR'].title()}")
    print(f"-Tamanho: {pedido['TAMANHO'].title()}")
    print(f"-Borda: {pedido['BORDA'].title()}")
    print(f"-Bebida: {pedido['BEBIDA'].title()}")
    print("-----------------------------------------")
    print(f"VALOR TOTAL: R$ {preco_total:.2f}")
    print("-----------------------------------------")
    print(f"Seu pedido foi enviado para a cozinha e estará pronto em breve.")
    print(f"Muito obrigado por escolher a Pizzaria Gemini, até a próxima!")
    print("-----------------------------------------")

except KeyError:
    #  Bloco de segurança, se por algum motivo uma chave não for encontrada.
    # Damos uma mensagem amigável ao usuário em vez de quebrar o programa.
    print("\nDesculpe, ocorreu um erro ao calcular o preço do seu pedido. Vamos reiniciar o processo.")
    print("Por favor, tente fazer seu pedido novamente.")
    print("-----------------------------------------")