#Aluno: Leonam Fonseca da Conceição Silva
#Data: 06/10/2026
#Professor: Rodrigo Medeiros Vilela

# ========================================
#   DESAFIO DEV: MINI-QUIZ DE TECNOLOGIA
# ========================================

print("=== BEM-VINDO AO QUIZ TECH CEJO/SENAI ===")
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Responda às perguntas com A, B ou C:\n")

pontuacao = 0

# --- PERGUNTA 1 ---
print("1) Qual linguagem estamos aprendendo nesta aula?")
print("A)HTML")
print("B)Phyton")
print("C)C+++")
resposta1 = input("Sua resposta: ").upper()

if resposta1 == "B":
    print("\nResposta correta! +1 ponto.\n")
    pontuacao = pontuacao +1

else:
    print("\nResposta incorreta. A resposta correta era B)Phyton.\n")
# --- PERGUNTA 2 ---
print("2) O que significa a sigla SGBD em Banco de Dados?")
print("A) Sistema de Gerenciamento de Banco de Dados")
print("B) Sistema Geral de Busca Digital")
print("C) Sofware de Gravação de Baixo Desempenho")
resposta2 = input("Sua resposta: ").upper()
if resposta2 == "A":
    print("\nResposta correta +1 ponto.\n")
    pontuacao = pontuacao +1
else:
    print("\nResposta incorreta. A correta era A) Sistema de Gerenciamento de Banco de Dados.\n")

# --- PERGUNTA 3 ---
print("3) Qual comando em Phyton é usado para exibir mensagens na tela?")
print("A) input()")
print("B)print()")
print("C)import()")
resposta3 = input("Sua resposta: ").upper()

if resposta3 == "B":
    print("\nResposta correta +1 ponto.\n")
    pontuacao = pontuacao +1
else:
     print("\nResposta incorreta. A correta era B)print().\n")


# --- PERGUNTA 4 ---
print("4) Qual é o tipo de dado usado para armazenar texto em Python?")
print("A) int()")
print("B) float()")
print("C) str()")
resposta4 = input("Sua resposta: ").upper()

if resposta4 == "C":
    print("\nResposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("\nResposta incorreta. A correta era C) str.\n")

# --- PERGUNTA 5 ---
print("5) Qual caractere é usado para fazer um comentário de uma linha em Python?")
print("A) #")
print("B) //")
print("C) /*")
resposta5 = input("Sua resposta: ").upper()

if resposta5 == "A":
    print("\nResposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("\nResposta incorreta. A correta era A) #.\n")

# --- RESULTADO FINAL ---
print("===================================================")
print(f"Fim do Quiz, {nome}!")
print(f"Sua pontuação final foi: {pontuacao} de 5 pontos.")

if pontuacao == 5:
    print("Exelente! Você acertou tudo!")
elif pontuacao >=1:
    print("Bom trabalho! Dá para melhorar revisando o conteúdo.")
else:
    print("Melhorar um pouco mais!")
print("===================================================")
