# --- Bloco de Definições: O Cardápio e as Ferramentas ---

# O Cardápio (Nossa "Fonte da Verdade")
SABORES_VALIDOS = ["MUSSARELA", "CALABRESA", "FRANGO", "PORTUGUESA", "CHOCOLATE BRANCO"]
BORDAS_VALIDAS = ["CATUPIRY", "CHEDDAR", "CHOCOLATE BRANCO", "NUTELLA", "NENHUMA"]
BEBIDAS_VALIDAS = ["COCA-COLA", "GUARANÁ", "CERVEJA", "NENHUMA"]

# A Nossa Ferramenta (Nossa Função)
def fazer_pergunta_validada(pergunta, opcoes_validas):
    """
    Faz uma pergunta ao usuário, valida a resposta contra uma lista de opções
    e retorna a resposta validada.
    """
    while True:
        print(pergunta)
        print(f"As opções são: {', '.join(opcoes_validas)}.")
        resposta = input("> ").strip().upper()
        print(f"\nEntendi, você escolheu {resposta.title()}.")
        if resposta in opcoes_validas:
            return resposta # Sucesso! Devolve a resposta e encerra a função.
            
        else:
            print(f"\nOps! Resposta inválida. Por favor, escolha uma das opções disponíveis.")

# --- INÍCIO DO PROGRAMA PRINCIPAL ---

# --- Bloco 1: Boas-vindas e Nome ---
print("-----------------------------------------")
print(" Bem-vindo à Pizzaria do Gemini! ")
print("-----------------------------------------")
print(f"Olá! Sou a Inteligencia Artificial da Pizzaria Gemini. Qual o seu nome?")
nome_cliente = input("> ").strip().title()
print(f"\nPrazer, {nome_cliente}! Vamos montar seu pedido juntos.")

# --- Bloco 2, 4 e 5: Fazendo as perguntas usando nossa função ---
sabor_pizza = fazer_pergunta_validada("\nQual sabor você quer?", SABORES_VALIDOS)

# A validação de tamanho é um pouco diferente, então mantemos por enquanto.
tamanho_escolhido = ""
while True:
    print(f"\nQual o tamanho da nossa fome hoje? Digite P, M ou G.")
    tamanho_pizza = input("> ").strip().upper()
    if tamanho_pizza == "P":
        tamanho_escolhido = "Pequena"; break
    elif tamanho_pizza == "M":
        tamanho_escolhido = "Média"; break
    elif tamanho_pizza == "G":
        tamanho_escolhido = "Grande"; break
    else:
        print("\nOpção inválida! Por favor, digite apenas P, M ou G.")
print(f"\nEntendi, uma pizza {tamanho_escolhido} de {sabor_pizza.title()}")

borda_pizza = fazer_pergunta_validada("\nDeseja borda recheada?", BORDAS_VALIDAS)
bebida_cliente = fazer_pergunta_validada("\nE para beber?", BEBIDAS_VALIDAS)

# --- Bloco 6: Resumo Final do Pedido ---
print(f"\nPerfeito, {nome_cliente}! Confirmando seu pedido:")
print("--- RESUMO DO PEDIDO ---")
print(f"Uma pizza sabor {sabor_pizza.title()}, tamanho {tamanho_escolhido}, com borda de {borda_pizza.title()} e uma {bebida_cliente.title()}")
print("-----------------------------------------")
print(f"Muito obrigado por escolher a Pizzaria Gemini, até a próxima!")
print("-----------------------------------------")