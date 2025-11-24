import matplotlib.pyplot as plt
import numpy as np


k = 8.9875517873681764e9

def calcular_forca_coulomb(q1, q2, distancia):
    """
    Calcula a força entre duas cargas usando a Lei de Coulomb
    
    Parâmetros:
    q1, q2: cargas em Coulombs
    distancia: distância entre as cargas em metros
    
    Retorna:
    Força em Newtons
    """
    if distancia == 0:
        return float('inf')  
    
    forca = k * abs(q1 * q2) / (distancia ** 2)
    return forca

def analisar_variacao_distancia(q1, q2, distancia_maxima=1.0, pontos=50):
    """
    Analisa como a força varia com a distância
    
    Parâmetros:
    q1, q2: cargas em Coulombs
    distancia_maxima: distância máxima a ser analisada em metros
    pontos: número de pontos para a análise
    """
    distancias = np.linspace(0.01, distancia_maxima, pontos)  
    forcas = []
    
    for d in distancias:
        forca = calcular_forca_coulomb(q1, q2, d)
        forcas.append(forca)
    
    return distancias, forcas

def plotar_grafico(distancias, forcas, q1, q2):
    """
    Plota o gráfico da força em função da distância
    """
    plt.figure(figsize=(10, 6))
    plt.plot(distancias, forcas, 'b-', linewidth=2)
    plt.title(f'Lei de Coulomb: Força entre q1 = {q1:.2e} C e q2 = {q2:.2e} C', fontsize=14)
    plt.xlabel('Distância (m)', fontsize=12)
    plt.ylabel('Força (N)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def main():
    print("=" * 60)
    print("         LEI DE COULOMB - CALCULADORA DE FORÇA")
    print("=" * 60)

    
    try:
        q1 = float(input("Digite o valor da carga 1 (C): "))
        q2 = float(input("Digite o valor da carga 2 (C): "))
        distancia = float(input("Digite a distância entre as cargas (m): "))
        
        if distancia <= 0:
            print("Erro: A distância deve ser maior que zero!")
            return
        
        
        forca = calcular_forca_coulomb(q1, q2, distancia)
        
        
        if q1 * q2 > 0:
            tipo = "REPULSIVA"
        elif q1 * q2 < 0:
            tipo = "ATRATIVA"
        else:
            tipo = "NULA"
        
        
        print("\n" + "=" * 40)
        print("RESULTADOS:")
        print("=" * 40)
        print(f"Carga 1 (q1): {q1:.2e} C")
        print(f"Carga 2 (q2): {q2:.2e} C")
        print(f"Distância (d): {distancia:.2e} m")
        print(f"Força resultante: {forca:.2e} N")
        print(f"Tipo de força: {tipo}")
        print("=" * 40)
        
        
        analisar = input("\nDeseja analisar como a força varia com a distância? (s/n): ").lower()
        
        if analisar == 's':
            distancia_max = float(input("Digite a distância máxima para análise (m): "))
            distancias, forcas = analisar_variacao_distancia(q1, q2, distancia_max)
            plotar_grafico(distancias, forcas, q1, q2)
            
            print("\nTabela de valores (amostra):")
            print("Distância (m)\tForça (N)")
            print("-" * 30)
            for i in range(0, len(distancias), len(distancias)//5):
                print(f"{distancias[i]:.3e}\t{forcas[i]:.3e}")
    
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()

