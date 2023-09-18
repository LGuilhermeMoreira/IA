import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

#Series

# words = pd.Series(['macaco','bola','prato'],index=['animal:', 'objeto:','objeto:'])

# print(words)

# print('===============================================')

# print(words[0])

# print('===============================================')

# for i in words:
#     print(words)

# print('===============================================')


#Dataframes

# relatorio = pd.DataFrame(
#     {
#         'Professores' : ['Atilio, Marcos, Enyo'],
#         'Cadeiras' : ['PAA, IA, APS'],
#         'A.I' : ['Graphs, ML, Software Eng.']
#     }
# )

# print(relatorio['A.I'])

#Exercism

csv = pd.read_csv('brics.csv')

print(csv)