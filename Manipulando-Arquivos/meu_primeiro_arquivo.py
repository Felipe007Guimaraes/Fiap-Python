""" Neste primeiro método vemoe como criar um arquivo com with.

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nMeu primeiro arquivo escrito em linguagem python! \nCurso da FIAP ON.")

Com o método with não se usa o método 'arquivo.close()' pois ele fecha automaticamente.


Esta é a segunda maneira de criar um arquivo

 arquivo = open("primeiro_arquivo.txt", "a")
arquivo.write("Meu primeiro arquivo escrito em linguagem python! \nCurso da FIAP ON.")
arquivo.close()  

Manipulando arquivos:"""

with open("primeiro_arquivo.txt", "r") as arquivo:
    for linhas in arquivo.readlines():
        print(linhas)
 
"""Como salvar arquivos de um dicionário"""
def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave,valor in dicionario.items ():
            arquivo.write(chave + ":" + str(valor))

 