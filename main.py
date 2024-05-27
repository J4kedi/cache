def incializar_cache(tam_cache):
    cache = {}

    for i in range(tam_cache):
        cache[i] = -1

    return cache

def imprimir_cache(cache):
    print("-------------------------------------")
    print("Posição principal  | Posição Memória ")

    for chave, valor in cache.items():
        print(f"        {chave}          |        {valor}")

def mapeamento_direto(tam_cache, pos_memoria):
    hits = 0
    miss = 0
    linha = 0
    status = ""

    cache = incializar_cache(tam_cache)
    print("Cahce Inicial")
    print(f"Tamanho da Cache:                  {tam_cache}")
    imprimir_cache(cache)

    for posicao in pos_memoria:
        for key in cache.keys():
            posicao_cache = posicao % tam_cache

            if key == posicao_cache and cache[key] == posicao:
                hits += 1
                status = "Hit"
            elif key == posicao_cache:
                cache[key] = posicao
                miss += 1
                status = "Miss"

        print("\n-------------------------------------")
        print(f"Linha {linha} | Posição de memória desejada {posicao}")
        print(f"Status: {status}")
        print(f"Tamanho da Cache: {tam_cache}")

        imprimir_cache(cache)

        linha += 1

    print("Conectividade em Sistemas Ciberfisicos - Mapeamento Direto")
    print("*--------------------------------------------------------*")
    print(f"Memórias acessadas: {len(pos_memoria)}")
    print(f"Número de hits: {hits}")
    print(f"Número de misses: {miss}")
    print(f"Taxa de acertos (hits): {(hits/len(pos_memoria) * 100):.2f}%")

def mapeamento_associativo_conjunto(tam_conjunto, pos_memoria):
    if tam_conjunto == 1:
        return

    hits = 0
    miss = 0
    linha = 0
    status = ""

    tam_cache = tam_conjunto

    cache = incializar_cache(tam_cache)
    print("Cahce Inicial")
    print(f"Tamanho da Cache:                  {tam_cache}")
    imprimir_cache(cache)

    for posicao in pos_memoria:
            for key in cache.keys():
                posicao_cache = posicao % tam_cache

                if key == posicao_cache and cache[key] == posicao:
                    hits += 1
                    status = "Hit"
                elif key == posicao_cache:
                    cache[key] = posicao
                    miss += 1
                    status = "Miss"

            print("\n-------------------------------------")
            print(f"Linha {linha} | Posição de memória desejada {posicao}")
            print(f"Status: {status}")
            print(f"Tamanho da Cache: {tam_cache}")

            imprimir_cache(cache)

            linha += 1

    print("Conectividade em Sistemas Ciberfisicos - Mapeamento Associativo por Conjunto")
    print("*--------------------------------------------------------------------------*")
    print(f"Memórias acessadas: {len(pos_memoria)}")
    print(f"Número de hits: {hits}")
    print(f"Número de misses: {miss}")
    print(f"Taxa de acertos (hits): {(hits/len(pos_memoria) * 100):.2f}%")



listas_posicoes = [[0, 1, 2, 3, 1, 4, 5, 6], [0,1,2,2,22,32,42,20,1,10,11,12,13]
,  [1,6,1,11,1,16,1,21,1,26]]
tamanho_cache = 4

for lista_posicao in listas_posicoes:
    mapeamento_direto(tamanho_cache, lista_posicao)

tamanho_bloco = 2


# numero de blocos * conjuntos
# mapeamento_associativo_conjunto(tamanho_conjunto, lista_posicao)