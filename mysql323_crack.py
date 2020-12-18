"""
    A hash à ser crackeada deve ser do tipo "MySQL-323"
"""

from passlib.hash import mysql323 as colidir
import sys
import os
import codecs

def main():
    args = sys.argv
    if (len(args) < 2):
        print('\n Uso: python3 mysql323 [WORDLIST] [HASH] [INÍCIO, PADRÃO 0] \n')
        exit(0)
    

    print('\n\tMysql323 Cracker \n \t\tHash: \t\t'+args[2]+ '\n\n \t\tWordlist:\t'+args[1])
    colidirHash(args[1], args[2], args[3])

def colidirHash(wordlst,hash, inicio = 0):
    arq = codecs.open(wordlst, 'r', encoding='utf-8', errors='ignore')
    descoberto = False
    possivelSenha = ''
    hash = hash.rstrip().replace(' ', '')
    inicio = int(inicio)

    wordlist_len = int(os.popen('wc -l '+wordlst+' | cut -d \" \" -f1').read())
    print('Detectado ' + str(wordlist_len) + ' senhas na wordlist.\n')
    print('\nIniciando em %d' %(int(inicio)))

    try:
        for i in range(0, wordlist_len):
            possivelSenha = arq.readline()
            if (i < inicio):
                continue

            descoberto = colidir.verify(possivelSenha.rstrip(), hash)
            if (descoberto):
                break

            print('[%s] não é a senha. ' %(possivelSenha.rstrip()))
    finally:
        arq.close()
        if descoberto:
            print('\n[SUCESSO] A senha é ' + possivelSenha)
        else:
            print('\n Senha não descoberta, tente outra wordlist.')
        print('\n\t\tFim\n')

if __name__ == "__main__":
    main()    
