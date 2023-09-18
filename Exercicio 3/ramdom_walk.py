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