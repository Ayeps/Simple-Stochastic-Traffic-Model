from stochmod import calc
import numpy as np

realizations = int(input('how many simulation runs: '))

results = np.zeros(realizations) #store the results of all the runs

no_occur = {
    'no_45':0,
    'no_30':0,
    'no_10':0,
    'no_0':0,
    #add the dict elements below by removing the comments (if rain element is added!)
    #'no_15':0,'no_25':0,'no_60':0,

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
    #add more if options (if rain element is added!)
    """
    elif (event == 15):
        no_occur['no_15'] += 1
    elif (event == 25):
        no_occur['no_25'] += 1
    elif (event == 60):
        no_occur['no_60'] += 1
    """    
    print(event)

#the probabilities of each incidents based on the simulation
prob_45 = (no_occur['no_45']/len(results))*100
prob_30 = (no_occur['no_30']/len(results))*100
prob_10 = (no_occur['no_10']/len(results))*100
prob_0 = (no_occur['no_0']/len(results))*100
#prob_15 = (no_occur['no_15']/len(results))*100
#prob_25 = (no_occur['no_25']/len(results))*100
#prob_60 = (no_occur['no_60']/len(results))*100




print(results)
print('----------------------------------------------------------------')
print('The number of occurences of a 45-minute delay: ',no_occur['no_45'])
print('The number of occurences of a 30-minute delay: ',no_occur['no_30'])
print('The number of occurences of a 10-minute delay: ',no_occur['no_10'])
print('The number of occurences of no delays: ',no_occur['no_0'])
#print('The number of occurences of 15-minute delay: ',no_occur['no_15'])
#print('The number of occurences of 25-minute delay: ',no_occur['no_25'])
#print('The number of occurences of 60-minute delay: ',no_occur['no_60'])

print('----------------------------------------------------------------')
print('a posteriori probability of a 45-minute delay',prob_45, ' per cent')
print('a posteriori probability of a 30-minute delay',prob_30, ' per cent')
print('a posteriori probability of a 10-minute delay',prob_10, ' per cent')
print('a posteriori probability of no delays',prob_0, ' per cent')
#print('a posteriori probability of a 15-minute delay',prob_15, ' per cent')
#print('a posteriori probability of a 25-minute delay',prob_25, ' per cent')
#print('a posteriori probability of a 60-minute delay',prob_60, ' per cent')
