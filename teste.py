import random
def criar_cartela():
    cartela=[]
    B=random.sample(range(1, 16), 5)
    I=random.sample(range(16, 31), 5)
    N=random.sample(range(31, 46), 5)
    G=random.sample(range(46, 61), 5)
    O=random.sample(range(61, 76), 5)
    for i in range(5):
        linha=[B[i], I[i], N[i], G[i], O[i]]
        cartela.append(linha)
    return cartela
def mostrar(c):
    print("B    I     N     G    O")
    print("----------------------")
    for linha in c:
        for num in linha:
            print(f"{num:2}", end=" | ")
        print()
    print()
def marcar(c, n):
    for i in range(5):
        for j in range(5):
            if c[i][j]==n:
                c[i][j]="X"
def verificar(c):
    for i in range(5):
        V=True
        for j in range(5):
            if c[i][j] != "X":
                V=False
        if V:
            return True
    for j in range(5):
        V=True
        for i in range(5):
            if c[i][j] != "X":
                V=False
        if V:
            return True
    return False
D="sim"
while D=="sim":
    N=int(input("Digite o número de jogadores: "))
    nomes=[]
    cartelas=[]
    for i in range(1,N+1):
        nome=input(f"Nome do jogador {i}: ")
        nomes.append(nome)
        cartelas.append(criar_cartela())
    G=False
    while True:
        n=random.randint(1,75)
        print("\n-------------- Número sorteado:", n,"--------------")
        for i in range(N):
            print("\nCartela de", nomes[i], "\n")
            marcar(cartelas[i], n)
            mostrar(cartelas[i])
            if verificar(cartelas[i]):
                print("BINGO!\nVencedor:", nomes[i])
                D="não"
                G=True
                break
        if G:
            break
