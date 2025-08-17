import random

def mostrar_titulo():
    print("#" * 52)
    print(" ######  ##    #  #####     #####   #   ##   ##    #")
    print("##       ##    #  ##   #   ##    #  #  ##    ##    #")
    print("##       ##    #  ##    #  ##    #  # ##     ##    #")
    print(" ######  ##    #  ##    #  ##    #  ###      ##    #")
    print("      ## ##    #  ##    #  ##    #  # ##     ##    #")
    print("      ## ##    #  ##   #   ##    #  #  ##    ##    #")
    print("#######   ######  #####     #####   #   ##    ##### ")
    print(" " * 12 + "Tiago e Samuel" + " " * 12)
    print("#" * 52)
    print("\nEscolha a dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil\n")

def criar_tabuleiro():
    base = 3
    lado = base * base

    def posicao(r, c): return (base*(r % base)+r//base+c) % lado
    def embaralhar(s): return random.sample(s, len(s))

    rBase = range(base)
    linhas_embaralhadas = [g*base + r for g in embaralhar(rBase) for r in embaralhar(rBase)]
    colunas_embaralhadas = [g*base + c for g in embaralhar(rBase) for c in embaralhar(rBase)]
    nums = embaralhar(range(1, lado+1))

    board = [[nums[posicao(r, c)] for c in colunas_embaralhadas] for r in linhas_embaralhadas]
    return board

def esconder_numeros(board, dificuldade):
    tabuleiro = [linha[:] for linha in board]
    n = 0
    if dificuldade == 1:
        n = 30
    elif dificuldade == 2: 
        n = 40
    else: 
        n = 55

    for _ in range(n):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        tabuleiro[x][y] = 0
    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    print("\n    1 2 3   4 5 6   7 8 9")
    print("  +-------+-------+-------+")
    for i, linha in enumerate(tabuleiro):
        print(f"{i+1} |", end=" ")
        for j, num in enumerate(linha):
            if num == 0:
                print(".", end=" ")
            else:
                print(num, end=" ")
            if (j+1) % 3 == 0 and j < 8:
                print("|", end=" ")
        print("|")
        if (i+1) % 3 == 0:
            print("  +-------+-------+-------+")

def venceu(tabuleiro, solucao):
    return tabuleiro == solucao

def jogar():
    while True:
        mostrar_titulo()
        escolha = input("Digite 1, 2 ou 3: ")
        if escolha not in ["1", "2", "3"]:
            print("Opção inválida, tente novamente.")
            continue

        dificuldade = int(escolha)
        solucao = criar_tabuleiro()
        tabuleiro = esconder_numeros(solucao, dificuldade)

        while True:
            mostrar_tabuleiro(tabuleiro)
            if venceu(tabuleiro, solucao):
                print(" Parabéns! Você completou o Sudoku! ")
                break

            print("Digite sua jogada (ou 'r' para refazer/embaralhar):")
            comando = input("Linha (1-9 ou 'r'): ")

            if comando.lower() == 'r':
                print("Novo tabuleiro embaralhado!")
                break

            try:
                linha = int(comando) - 1
                coluna = int(input("Coluna (1-9): ")) - 1
                numero = int(input("Número (1-9): "))
            except ValueError:
                print("Entrada inválida, tente novamente.")
                continue

            if 0 <= linha < 9 and 0 <= coluna < 9 and 1 <= numero <= 9:
                if solucao[linha][coluna] == numero:
                    tabuleiro[linha][coluna] = numero
                else:
                    print("Número incorreto, tente novamente!")
            else:
                print("Esta casa ja está preenchida!.")

        jogar_novamente = input("Quer jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            print("Até a próxima!")
            break

jogar()
