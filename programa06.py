 # Impressão de variáveis

'''
Forma comum de juntar variaveis com textos: (porem o código fica muito poluido)

nome = "joão"
idade = 33
altura = 1.75

print("ola, ", nome, "vi que você tem ",idade, "anos e", altura")
'''


# Forma correta onde não deixa seu texto poluido ( utiliza-se (f) no começo da frase, para que podemos separar as variaveis com colchetes)

nome = "joão"
idade = 33
altura = 1.75

print(f"ola, {nome} vi que você tem {idade} anos e {altura}")