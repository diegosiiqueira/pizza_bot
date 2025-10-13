#Traz toda a biblioteca do spacy para dentro do nosso código.
import spacy
#Importa a classe EntityRuler de dentro do spacy, será o nosso professor particular que nos permite criar regras personalizadas para reconhecer entidades.
from spacy.pipeline import EntityRuler

print("Carregando o modelo de linguagem...")
# Acorda a IA, dando-lhe o modelo de linguagem em português
nlp = spacy.load("pt_core_news_lg") # Modelo grande, mais preciso
print("Modelo carregado com sucesso!") 

# Nosso conhecimento específico que iremos ensinar para a IA
SABORES = ["MUSSARELA", "CALABRESA", "FRANGO", "PORTUGUESA", "CHOCOLATE BRANCO"]
TAMANHOS = ["PEQUENA", "MÉDIA", "GRANDE"]
BORDAS = ["CATUPIRY", "CHEDDAR", "CHOCOLATE BRANCO", "NENHUMA"]
BEBIDAS = ["COCA-COLA", "GUARANÁ", "CERVEJA"]

#Criamos uma lista vazia que será nosso "livro de regras"
patterns = []

#usamos loops para criar regras automaticamente
for sabor in SABORES:
    patterns.append({"label": "SABOR", "pattern": sabor})

for tamanho in TAMANHOS:
    patterns.append({"label": "TAMANHO", "pattern": tamanho})

for borda in BORDAS:
    patterns.append({"label": "BORDA", "pattern": borda})

for bebida in BEBIDAS:
    patterns.append({"label": "BEBIDAS", "pattern": bebida})

#Criamos uma instância do EntityRuler e o adicionamos ao pipeline do Spacy
ruler = nlp.add_pipe("entity_ruler", before="ner")


#Entregamos o "livro da magia" para o professor. A aula está dada!
ruler.add_patterns(patterns)

# A frase que vamos usar é para testar nossa IA
frase_pedido = "Boa noite, quero pedir uma pizza média de frango com borda de catupiry e a bebida é cerveja, por favor."
print(f"\n--- Analisando a frase: '{frase_pedido}' ---")

# Passamos a frase para a IA processar. Usamos .upper() para combinar com nossos padrões em maiúsculas
doc = nlp(frase_pedido.upper())

print("\n--- Entidades de Pizza Encontradas: ---")

# Agora, vamos verificas quais entidades nosso "Professor Particular" encontrou.
for ent in doc.ents:
    # Filtramos para mostrar apenas as entidades que NÓS ensinamos
    if ent.label_ in ["SABOR", "TAMANHO", "BORDA", "BEBIDA"]:
        print(f"  -> {ent.label_}: '{ent.text}'")