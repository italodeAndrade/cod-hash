import getpass
import hashlib
def logar_usuario(nome_usuario, senha):
    with open('usuarios.txt', 'r') as login_arquivo:
        linhas = login_arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(',')
            usuario = None
            senha_usuario = None
            for parte in partes:
                if 'usuario' in parte:
                    usuario = parte.split(':')[1].strip()
                elif 'senha' in parte:
                    senha_usuario = parte.split(':')[1].strip()
            if usuario == nome_usuario and senha_usuario == senha:
                return True
    return False

def cadastrar_usuario():
    print("insira usuario e senha com apenas 4 caracteres")
    usuario = input("Insira o seu perfil de usuário (ou digite 0 para sair): ")
    while len(usuario) > 4 or len(usuario) <0:
        print("!!digite um usuario com apenas 4 caracteres!!")
        usuario = input("Insira o seu perfil de usuário (ou digite 0 para sair): ")
    if usuario == '0':
        return
    
    senha = getpass.getpass(prompt='Insira a sua senha: ')
    senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')
    while len(senha)>4 or len(senha)<0 or len(senha2)>4 or len(senha) < 0:
        print("!!insira uma senha que contenha apenas 4 caracteres!!")
        senha = getpass.getpass(prompt='Insira a sua senha: ')
        senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')
    
    while senha != senha2:
        print("As senhas digitadas não correspondem. Tente novamente.")
        senha = getpass.getpass(prompt='Insira a sua senha: ')
        senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')
        while len(senha)>4 or len(senha)<0 or len(senha2)>4 or len(senha) < 0:
            print("!!insira uma senha que contenha apenas 4 caracteres!!")
            senha = getpass.getpass(prompt='Insira a sua senha: ')
            senha2 = getpass.getpass(prompt='Insira novamente a sua senha: ')                    
    senha_codificada=senha.encode('utf-8')
    obj_sha=hashlib.sha256()
    obj_sha.update(senha_codificada)
    senha=obj_sha.hexdigest()
    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f"usuario: {usuario}, senha: {senha}\n")

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
            print("1-sim \n 2-não")
            esc=int(input("sair?"))
            while esc==2:
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("(\⑅(\ ")     
                print("(ᴗ͈  ̫ᴗ͈*)")        
                print("(UU   )ଓ ")
                print("U U")
                print("1-sim \n 2-não")
                esc=int(input("sair? "))
        else:
            print("Usuário ou senha incorretos!")
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida.")
