from stochmod import calc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

def simulate(realizations,pointOfItrs):
    #this is basically a copy on the monte carlo simulation!
    results = np.zeros(realizations) #store the results of all the runs
    no_occur = {
        'no_45':0,
        'no_30':0,
        'no_10':0,
        'no_0':0,
    }

    for x in range(realizations):
        event = calc()
        results[x] = event
        if (event == 45):
            no_occur['no_45'] += 1
        elif (event == 30):
            no_occur['no_30'] += 1
        elif (event == 10):
            no_occur['no_10'] += 1
        elif (event == 0):
            no_occur['no_0'] += 1 

    #the probabilities of each incidents based on the simulation
    prob_45 = (no_occur['no_45']/len(results))*100
    prob_30 = (no_occur['no_30']/len(results))*100
    prob_10 = (no_occur['no_10']/len(results))*100
    prob_0 = (no_occur['no_0']/len(results))*100

    if pointOfItrs==45 :
        return prob_45
    elif pointOfItrs==30 :
        return prob_30
    elif pointOfItrs==10 :
        return prob_10
    elif pointOfItrs==0 :
        return prob_0

######################################################################
######################################################################



def main():    
    start = int(input('start :'))
    end = int(input('end: '))
    inv = int(input('intervals:'))
    pointOfItrs = int(input(' which a priori probability to track: '))

    #variables to be observed!
    runs = list(np.arange(start,end,inv))
    resultOfRuns = []

    #actual simulation
    for x in runs:
        resultOfRuns.append(simulate(x,pointOfItrs))

    #print(resultOfRuns)
    #print(runs)    
    

    #graphing part!
    style.use('seaborn-whitegrid')
    fig = plt.figure()
    plt.plot(runs,resultOfRuns)
    plt.axhline(y = pointOfItrs, color = 'r', linestyle='-')
    plt.xlabel('no. of simulations')
    plt.ylabel('a posteriori probability')
    plt.show()




if __name__ == '__main__':
    main()
