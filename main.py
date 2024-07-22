import math

def calcular_vetor_normal(pontoA, pontoB, pontoC):
    # Calculando os vetores AB e AC
    AB = [pontoB[i] - pontoA[i] for i in range(3)]
    AC = [pontoC[i] - pontoA[i] for i in range(3)]
    
    # Calculando o produto vetorial de AB e AC manualmente
    vetor_normal = [
        AB[1] * AC[2] - AB[2] * AC[1],
        AB[2] * AC[0] - AB[0] * AC[2],
        AB[0] * AC[1] - AB[1] * AC[0]
    ]
    
    return vetor_normal

def normalizar_vetor(vetor):
    # Calculando o módulo do vetor
    modulo = math.sqrt(sum([coord ** 2 for coord in vetor]))
    # Normalizando o vetor para obter o versor
    versor = [coord / modulo for coord in vetor]
    versor_oposto = [-coord / modulo for coord in vetor]
    return versor, versor_oposto

def ler_ponto():
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))
    z = float(input("Digite a coordenada z: "))
    return [x, y, z]

def main():
    print("Digite as coordenadas do ponto A:")
    pontoA = ler_ponto()
    
    print("Digite as coordenadas do ponto B:")
    pontoB = ler_ponto()
    
    print("Digite as coordenadas do ponto C:")
    pontoC = ler_ponto()
    
    vetor_normal = calcular_vetor_normal(pontoA, pontoB, pontoC)
    versor, versor_oposto = normalizar_vetor(vetor_normal)
    
    print("O vetor normal ao plano definido pelos pontos é:", vetor_normal)
    print("Os versores (vetores unitários) correspondentes são:")
    print("Versor 1:", versor)
    print("Versor 2:", versor_oposto)

if __name__ == "__main__":
    main()
