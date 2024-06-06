#Código feito por Arthur Queiroz.
#Sinta-se livre para usá-lo como base para seus projetos.

import os
import time
import random
import shutil

print("Como você quer aleatorizar?")
print("1- Somente itens")
print("2- Somente blocos")
print("3- Ambos")
print("4- Sair")
print("")
escolha = int(input("Digite sua escolha: "))

def aleatorizar(caminho, passos):
    caminho_pasta_temporaria = "./Renomeados/"
    
    #Array com todas as texturas de itens / blocos da pasta.
    texturas1 = [x for x in os.listdir(caminho) if x.endswith('.png')]
    itensFiltrados = sorted(texturas1)

    def randomizarIMGS(caminho):
        for x in os.listdir(caminho):
            nomeVelho = caminho.removesuffix(".png") + x
            if x.endswith('.png'):
                imgRandom = random.choice(itensFiltrados)
                rand = "./Renomeados/" + imgRandom
                os.rename(nomeVelho, rand)
                itensFiltrados.remove(imgRandom)
            else: pass
        else:
            for x in os.listdir(caminho_pasta_temporaria):
                #texturas_itens2 = [x for x in os.listdir(caminho_pasta_temporaria)]
                shutil.move(caminho_pasta_temporaria + x, caminho)
            else:
                if passos == 2:
                    print("Aleatorizando Blocos")
                    aleatorizar(caminho_blocos, 1)
                else:
                    sair()

    if os.path.isdir("Renomeados"):
        randomizarIMGS(caminho)
    else:
        os.mkdir("./Renomeados")
        randomizarIMGS(caminho)

def sair():
    print("Processos finalizados com sucesso")
    os.rmdir("./Renomeados")
    print("Fechando o programa em:")
    tempo = 6
    while(tempo > 0):
        time.sleep(1)
        tempo -= 1
        print(tempo)
    else:
        pass

caminho_itens = "./assets/minecraft/textures/items/"
caminho_blocos = "./assets/minecraft/textures/blocks/"

match escolha:
    case 1:
        print("Aleatorizando Itens")
        aleatorizar(caminho_itens, 1)
    case 2:
        print("Aleatorizando Blocos")
        aleatorizar(caminho_blocos, 1)
    case 3:
        print("Aleatorizando Itens")
        aleatorizar(caminho_itens, 2)