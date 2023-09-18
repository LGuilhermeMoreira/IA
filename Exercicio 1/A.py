import numpy as np

altura = [1.73, 1.68, 1.71, 1.89, 1.79]
peso = [65.4, 59.2, 63.6, 88.4, 68.7]

l_altura = np.array(altura)
l_peso = np.array(peso)

l_imc = l_peso / (l_altura ** 2)
l_imc = np.array(l_imc)
print("IMC:", l_imc)

l_sobrepeso = []

for imc in l_imc:
    if imc > 23:
        l_sobrepeso.append(imc)

l_sobrepeso = np.array(l_sobrepeso)
print("Sobrepeso:", l_sobrepeso)
