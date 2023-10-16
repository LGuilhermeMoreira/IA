# Em uma Random Walk de 100 Steps pra subir em um edifício os steps são decididos da seguinte maneira:

#     Os Steps são decididos no lance de um dado
#     se der 1 ou 2 desce 1 degrau (-1)
#     se der 3, 4 ou 5 sobe 1 degrau (+1)
#     se der 6 lanca o dado novamente e sobe o resultado (+1, +2, +3, +4, +5 ou +6)

# Obs:

#     Cada Random Walk tem uma tem um ponto final
#     Simule 10.000 vezes a caminhada: 10.000 pontos finais
#     Verifique a distribuição dos resultados finais
#     Calcule a probabilidade de se subir 60 ou mais andares no conjunto de caminhadas realizadas

import numpy as np
#import pandas as pd

# starting random

#np.random.seed(123)
def ramdomwalk():
    sum = 0
    
    for i in range(100):
        dice = np.random.randint(1,7)
        if(dice == 2 or dice == 1): sum -= 1
        if(dice == 3 or dice == 4 or dice == 5): sum += 1
        if(dice == 6):
            newdice = np.random.randint(1,7)
            sum += newdice

    return sum

#starting main
if __name__ == '__main__':

    #creating end points
    list = []
    value = 0

    #assigning values
    for i in range(10000):
        list.append(ramdomwalk())
        if(i >= 60): value += 1

    
    result = float(value/len(list))

    print("o resultado é: " + str(result*100) + "%")