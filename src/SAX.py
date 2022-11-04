"""
Implementación de las funciones relacionadas con el algoritmo de codificación SAX
"""

def PAA ( C : list[float], w:int) -> list[float]:
    ''' Realiza la transformación Piecewise Aggregation Approximation
    Argumentos: 
    `C` serie temporal a transformar
    `w`tamaño de la nueva serie
    '''
    n = len(C)
    w_n = w / n
    n_w = n //w # debe de ser un entero

    bar_C = [
        w_n *sum(
            C[n_w*(i-1) : n_w*i] # no se le suma 1 porque python empieza en 0
        )
        for i in range(1,w+1)
    ]
    return bar_C

# Blanca:  Me he quedado por aquí implementando
def PAA_to_SAX(bar_C, a):
    """
    Realiza paso 2 de discretización
    """
    # Pasos a realizar 
    # 1. Normalización de bar_C
    # 2. Sacar percentiles en función de a
    # 3. Calcular alfabeto(lista de número no de caracteres pa poder utilizar nuestro algoritmos de MI)
    # 4. Asignar a cada bar_C el *caracter/entero* que le corresponda 


### test 

if __name__ == '__main__':
    C = [1,2,1,0, 0, 0 ]
    w =  3
    print(PAA(C,w))

