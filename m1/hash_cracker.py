#Ítalo de Andrade Teles Ocimar Lima

import hashlib
import time
from array import array

def deco_senha(senha_hash):
    inicio = time.time()

    with open('wordlist.txt', 'r', encoding='utf-8', errors='ignore') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            senha_wrd = linha.strip()
            senha_wrd2 = senha_wrd.encode('utf-8')
            obj_sha = hashlib.sha256()
            obj_sha.update(senha_wrd2)
            senha_wrd_hash = obj_sha.hexdigest()
            if senha_wrd_hash == senha_hash:
                fim = time.time()
                tempo_decorrido = fim - inicio
                print("Senha normal:", senha_wrd)
                print("Tempo decorrido para decriptar:", tempo_decorrido, "segundos")
                return senha_wrd
    print("Senha não encontrada na wordlist.")



            


def ler_wordlist():
    with open('usuarios.txt', 'r') as arquivo_us:
        linhas = arquivo_us.readlines()
        for linha in linhas:
            partes = linha.strip().split(', ')
            for parte in partes:
                if parte.startswith('usuario:'):
                    usuario = parte.split(': ')[1]
                elif parte.startswith('senha:'):
                    senha_usuario = parte.split(': ')[1]
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Usuário:", usuario)
            print("Senha:", senha_usuario)
            deco_senha(senha_usuario)


ler_wordlist()
