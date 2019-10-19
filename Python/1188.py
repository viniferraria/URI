def create_matrix():
    matrix = [[ float(input()) for column in range(12)] for row in range(12)]
    return matrix

def inferior_area(matrix):
    inferior_matrix = [ matrix[12 - each][each: 12 - each] for each in range(1,6)]
    qtd = 0
    soma = 0
    for i in range(6):
        qtd += len(inferior_matrix[i])
        soma = sum(inferior_matrix[i])
    return qtd, soma

def main():
    option = input()
    matriz = create_matrix()
    qtd, soma = inferior_area(matriz)
    if option.upper() == "S":
        print(soma)
    else:
        media = soma/qtd
        print(media)
