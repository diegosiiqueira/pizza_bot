# --- Bloco de Definições: O Cardápio e as Ferramentas ---

# O Cardápio (Nossa "Fonte da Verdade")
SABORES_VALIDOS = ["MUSSARELA", "CALABRESA", "FRANGO", "PORTUGUESA", "CHOCOLATE BRANCO"]
BORDAS_VALIDAS = ["CATUPIRY", "CHEDDAR", "CHOCOLATE BRANCO", "NUTELLA", "NENHUMA"]
BEBIDAS_VALIDAS = ["COCA-COLA", "GUARANÁ", "CERVEJA", "NENHUMA"]

# Tabela de Preços (Nossa "Fonte da verdade para valores") 
PRECOS_TAMANHO = {"P": 25.00, "M": 40.00, "G": 50.00}
PRECOS_BORDA = {"CATUPIRY": 5.00, "CHEDDAR": 8.00, "CHOCOLATE BRANCO": 10.00, "NUTELLA": 12.00, "NENHUMA": 0.00}
PRECOS_BEBIDA = {"COCA-COLA": 10.00, "GUARANÁ": 7.00, "CERVEJA": 5.00, "NENHUMA": 0.00}


# A Nossa Ferramenta (Nossa Função)
def fazer_pergunta_validada(pergunta, opcoes_validas): 
    """
    Faz uma pergunta ao usuário, valida a resposta contra uma lista de opções
    e retorna a resposta validada.
    """
    while True: # função de repetição até o usuario acertar
        print(pergunta)
        print(f"As opções são: {', '.join(opcoes_validas).replace('_', ' ')}.") # replace para melhorar a exibição e join para formatar a lista
        resposta = input("> ").strip().upper()

        if resposta in opcoes_validas:
            print(f"\nEntendi, você escolheu {resposta.title()}.")
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

preco_total = 0.0 # Variável para acumular o preço total do pedido

#Bloco 2: Seleção e Cálculo do sabor e tamanho
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
        
# Adicionamos o preço do tamanho a conta total
preco_total += PRECOS_TAMANHO[tamanho_pizza]
print(f"\nEntendi, uma pizza {tamanho_escolhido} de {sabor_pizza.title()}")
# bloco 3: Seleção e calculo da borda e bebida                              
borda_pizza = fazer_pergunta_validada("\nDeseja borda recheada?", BORDAS_VALIDAS)
# Adiciona o preço da borda ao total
preco_total += PRECOS_BORDA[borda_pizza] # Adiciona o preço da borda ao total

bebida_cliente = fazer_pergunta_validada("\nE para beber?", BEBIDAS_VALIDAS)
preco_total += PRECOS_BEBIDA[bebida_cliente] # Adiciona o preço da bebida ao total
print(f"\nÓtimo! Uma borda de {borda_pizza.title()} e uma {bebida_cliente.title()}.")

# --- Bloco 4: Resumo Final do Pedido ---
print(f"\nPerfeito, {nome_cliente}! Confirmando seu pedido:")
print("----------- RESUMO DO PEDIDO ------------")
print(f"-Pizza: {sabor_pizza.title()}")
print(f"-Tamanho: {tamanho_escolhido.title()}")
print(f"-Borda: {borda_pizza.title()}")
print(f"-Bebida: {bebida_cliente.title()}")
print("-----------------------------------------")
print(f"VALOR TOTAL: R$ {preco_total:.2f}")
print("-----------------------------------------")
print(f"Seu pedido foi enviado para a cozinha e estará pronto em breve.")

print(f"Muito obrigado por escolher a Pizzaria Gemini, até a próxima!")
print("-----------------------------------------")