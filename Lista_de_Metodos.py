#ATIVIDADES MÉTODOS EM PYTHON

#Exercício 1A = strip()
nome = input("Digite seu nome: ")
print("Seu nome é: ", nome.strip())

#Exercício 1B = strip()
termo = input("Digite o termo que deseja usar: ")
print("Termo pesquisado: ", termo.strip())



#Exercício 2A = lower()
comando_sair = input("Digite o comando: ")
print("Comando utilizado: ", comando_sair.lower())
print("Saindo...")

#Exercício 2B = lower()
email = input("Digite seu email: ")
print("Vamos comparar seu email com uma versão minúscula: ")
print("O email inserido: ", email)
print("Email em minúsculo: ", email.lower())



#Exercício 3A = upper()
codigo_produto = input("Digite o código do produto: ")
print("O código do seu produto é: ", codigo_produto.upper())

#Exercício 3B = upper()
estado = input("Digite um estado: ")
print("O estado escolhido foi: ", estado.upper())



#Exercício 4A = title()
nome_completo = input("Digite seu nome completo: ")
print("Seu nome completo é: ", nome_completo.title())

#Exercício 4B = title()
titulo_evento = input("Digite o título do evento: ")
print("")
print("")
print(titulo_evento.title())
print("")
print("")


#Exercício 5A = replace()
num_telefone = input("Digite seu telefone (formato 99999-9999): ")
print("O numero de telefone é: ", num_telefone.replace("-", " "))

#Exercício 5B = replace()
valor_digitado = input("Digite o valor com os centavos (ex: 19,90): ")
print("O valor é: ", valor_digitado.replace(",", "."))



#Exercício 6A = split()
nome_idade_cidade = input("Digite o nome, a idade e a cidade separados por ponto e vírgula: ")
print(nome_idade_cidade.split(";"))

#Exercício 6B = split()
palavras_chave = input("Digite as palavras chave separadas por vírgula: ")
print(palavras_chave.split(","))



#Exercício 7A = join()
integrantes = input("Digite os integrantes da equipe separados por vírgula: ")
lista_integrantes = integrantes.split(",")
print(", ".join(lista_integrantes))

#Exercício 7B = join()
opcoes_menu = input("Digite as opções percorridas no menu, separadas por vírgula: ")
lista_opcoes = opcoes_menu.split(",")
print(" > ".join(lista_opcoes))



#Exercício 8A = count()
frase = input("Digite uma frase curta: ")
print("A letra 'a' aparece: ", frase.count("a"), "vezes")

#Exercício 8B = count()
anotacao = input("Digite uma anotação: ")
print("A palavra 'erro' aparece: ", anotacao.count("erro"), "vezes")



#Exercício 9A = startswith()
comando = input("Digite um comando: ")
print("É um comando especial: ", comando.startswith("/"))

#Exercício 9B = startswith()
codigo = input("Digite um código de produto: ")
print("Começa com o prefixo PROD-: ", codigo.startswith("PROD-"))



#Exercício 10A = endswith()
arquivo = input("Digite o nome de um arquivo: ")
print("Termina com .csv: ", arquivo.endswith(".csv"))

#Exercício 10B = endswith()
email_institucional = input("Digite um e-mail institucional: ")
print("Termina com @ufrpe.br: ", email_institucional.endswith("@ufrpe.br"))



#Exercício 11A = find()
email_arroba = input("Digite um e-mail: ")
print("O caractere '@' está na posição: ", email_arroba.find("@"))

#Exercício 11B = find()
entrada = input("Digite uma entrada no formato comando:valor: ")
print("O caractere ':' está na posição: ", entrada.find(":"))



#Exercício 12A = isalpha()
primeiro_nome = input("Digite um primeiro nome: ")
print("Contém apenas letras: ", primeiro_nome.isalpha())

#Exercício 12B = isalpha()
categoria = input("Digite uma categoria (ex: livros, jogos): ")
print("Contém apenas letras: ", categoria.isalpha())



#Exercício 13A = isdigit()
opcao_menu = input("Digite a opção do menu: ")
print("Contém apenas dígitos: ", opcao_menu.isdigit())

#Exercício 13B = isdigit()
idade = input("Digite sua idade: ")
print("Contém apenas números: ", idade.isdigit())



#Exercício 14A = isalnum()
codigo_acesso = input("Digite um código de acesso: ")
print("É alfanumérico (sem símbolos ou espaços): ", codigo_acesso.isalnum())

#Exercício 14B = isalnum()
identificador = input("Digite um identificador de produto: ")
print("É alfanumérico: ", identificador.isalnum())



#Exercício 15A = isspace()
observacao = input("Digite um campo de observação: ")
print("Contém apenas espaços em branco: ", observacao.isspace())

#Exercício 15B = isspace()
resposta = input("Digite uma resposta: ")
print("Contém apenas espaços ou tabulações: ", resposta.isspace())



#Exercício 16A = isupper()
sigla = input("Digite uma sigla: ")
print("Está toda em maiúsculas: ", sigla.isupper())

#Exercício 16B = isupper()
codigo_categoria = input("Digite um código de categoria: ")
print("O formato está correto (maiúsculas): ", codigo_categoria.isupper())



#Exercício 17A = islower()
comando_minusculo = input("Digite um comando (deve estar em minúsculas): ")
print("O formato está correto (minúsculas): ", comando_minusculo.islower())

#Exercício 17B = islower()
nome_usuario = input("Digite um nome de usuário: ")
print("Está todo em minúsculas: ", nome_usuario.islower())



#Exercício 18A = zfill()
senha_atendimento = input("Digite o número da senha de atendimento: ")
print("Senha formatada: ", senha_atendimento.zfill(5))

#Exercício 18B = zfill()
numero_pedido = input("Digite o número da nota ou pedido: ")
print("Número formatado: ", numero_pedido.zfill(8))

