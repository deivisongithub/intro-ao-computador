#Aluno: Deivison rodrigues jordao
#encriptador e desencriptador de cifra de cesar

#Definicoes de variaveis
texto_crip_final = ""

#Definicao de funcoes

def cod_cesar(texto,chave):
    texto_crip = ""
    for i in texto:
        numero_crip = ord(i) + chave
        if(numero_crip > 126):
            numero_crip = 31 + (numero_crip % 126)
        numero_descrip = chr(numero_crip)
        texto_crip = texto_crip + numero_descrip
    return texto_crip

def decod_cesar(texto,chave):
    texto_crip = ""
    for i in texto:
        numero_crip = ord(i) - chave
        if(numero_crip > 126):
            numero_crip = 31 + (numero_crip % 126)
        numero_descrip = chr(numero_crip)
        texto_crip = texto_crip + numero_descrip
    return texto_crip

#Processamento
 
selecao_da_operacao = int(input("Caso voce queria codificar uma mensagem digite (1) ,se quiser decodificar uma mensagem digite (0): "))

filename = input("digite aqui o nome do arquivo que esta sua mensagem ex: test.txt (garanta que o arquivo esteja no mesmo diretorio que o codigo) : ")
chave = int(input("digite a chave da criptografia(numero que e equivalente ao numeros de letras serao puladas ): "))

if(selecao_da_operacao == 1):
    with open(filename, 'r', errors='ignore') as file:
        for line in file:
            texto_crip_final = texto_crip_final + cod_cesar(line,chave) + "\n"
        file.close()
        arquivo = open('test_crip.txt' , 'w')
        arquivo.write( texto_crip_final)
        arquivo.close()
        print("seu arquivo foi criptografado e esta no endereco test_crip.txt ")

if(selecao_da_operacao == 0):
    with open(filename, 'r', errors='ignore') as file:
        for line in file:
            texto_crip_final = texto_crip_final + decod_cesar(line,chave) + "\n"
        file.close()
        arquivo = open('test_decrip.txt' , 'w')
        arquivo.write( texto_crip_final)
        arquivo.close()
        print("seu arquivo foi descriptografado e esta no endereco test_decrip.txt ")
    