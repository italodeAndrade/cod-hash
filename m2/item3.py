#Ítalo de Andrade Teles Ocimar Lima
#Theo Machado Ravaglia
import getpass
import hashlib
import random
import string

def gerar_caracteres_aleatorios(tamanho=3):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def logar_usuario(nome_usuario, senha):
    with open('usuarios.txt', 'r') as login_arquivo:
        linhas = login_arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(', ')
            usuario = None
            senha_usuario = None
            salt_inicio = None
            salt_fim = None
            for parte in partes:
                if 'usuario' in parte:
                    usuario = parte.split(': ')[1].strip()
                elif 'senha' in parte:
                    senha_usuario = parte.split(': ')[1].strip()
                elif 'salt_inicio' in parte:
                    salt_inicio = parte.split(': ')[1].strip()
                elif 'salt_fim' in parte:
                    salt_fim = parte.split(': ')[1].strip()
            if usuario == nome_usuario:
                senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
                senha_modificada = salt_inicio + senha_hash + salt_fim
                senha_codificada = hashlib.sha256(senha_modificada.encode('utf-8')).hexdigest()
                if senha_usuario == senha_codificada:
                    return True
    return False

def cadastrar_usuario():
    print("Insira usuário e senha com apenas 4 caracteres")
    usuario = input("Insira o seu perfil de usuário (ou digite 0 para sair): ")
    while len(usuario) > 4 or len(usuario) < 0:
        print("!!Digite um usuário com apenas 4 caracteres!!")
        usuario = input("Insira o seu perfil de usuário (ou digite 0 para sair): ")
    if usuario == '0':
        return
    
    senha = getpass.getpass(prompt='Insira a sua senha: ')
    senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')
    while len(senha) > 4 or len(senha) < 0 or len(senha2) > 4 or len(senha2) < 0:
        print("!!Insira uma senha que contenha apenas 4 caracteres!!")
        senha = getpass.getpass(prompt='Insira a sua senha: ')
        senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')
    
    while senha != senha2:
        print("As senhas digitadas não correspondem. Tente novamente.")
        senha = getpass.getpass(prompt='Insira a sua senha: ')
        senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')
        while len(senha) > 4 or len(senha) < 0 or len(senha2) > 4 or len(senha2) < 0:
            print("!!Insira uma senha que contenha apenas 4 caracteres!!")
            senha = getpass.getpass(prompt='Insira a sua senha: ')
            senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')
    
    senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
    
    salt_inicio = gerar_caracteres_aleatorios()
    salt_fim = gerar_caracteres_aleatorios()
    
    senha_modificada = salt_inicio + senha_hash + salt_fim
    senha_codificada = hashlib.sha256(senha_modificada.encode('utf-8')).hexdigest()
    
    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f"usuario: {usuario}, senha: {senha_codificada}, salt_inicio: {salt_inicio}, salt_fim: {salt_fim}\n")

while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("3 - Sair")
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    escolha = input("Insira a sua escolha: ")
    
    if escolha == '3':
        print("TCHAU :3")
        break
    elif escolha == '2':
        cadastrar_usuario()
    elif escolha == '1':
        usuario_login = input("Insira o seu usuário: ")
        senha_login = getpass.getpass(prompt='Insira a sua senha: ', stream=None)
        login_valido = logar_usuario(usuario_login, senha_login)
        if login_valido:
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("(\⑅(\ ")     
            print('(ᴗ͈  ̫ᴗ͈*)')        
            print("(UU   )ଓ ")
            print("  U U")
            print("1-sim \n2-não")
            esc = int(input("Sair? "))
            while esc == 2:
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("(\⑅(\ ")     
                print("(ᴗ͈  ̫ᴗ͈*)")        
                print("(UU   )ଓ ")
                print("U U")
                print("1-sim \n 2-não")
                esc = int(input("Sair? "))
        else:
            print("Usuário ou senha incorretos!")
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida.")
