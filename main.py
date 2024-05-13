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

    cache = incializar_cache(10)
    imprimir_cache(cache)

    for posicao in pos_memoria:
        for key in cache.keys():
            posicao_cache = posicao % tam_cache

            if key == posicao_cache and cache[key] != -1:
                cache[key] = posicao
                hits += 1

                imprimir_cache(cache)

                print(f"hits: {hits}")
                print(f"miss: {miss}")
            elif key == posicao_cache:
                cache[key] = posicao
                miss+= 1
                imprimir_cache(cache)

                print(f"hits: {hits}")
                print(f"miss: {miss}")


lista_posicao = [0, 2, 7, 2, 101]

mapeamento_direto(10, lista_posicao)