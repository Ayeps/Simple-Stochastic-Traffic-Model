
import random
from datetime import datetime
import math

#use the instantaneous date as the seed for the 
#pseudorandom number generation
random.seed(datetime.now())

#stochastic model
def calc():
    time_delay = 0
    event = random.random()
    if(0.0<event<0.06):
        time_delay = 0
    elif(0.6<=event<0.21):
        time_delay = 10
    elif(0.21<=event<0.55):
        time_delay = 30
    elif(0.55<=event<0.99):
        time_delay = 45
    else:
        time_delay = 10


    
    #remove the comment sign below if you are to add rain constant!!   
    """rain_event = random.random()
    if(0.0<rain_event < 50):
        time_delay += 15
    """
    return time_delay


if __name__ == "__main__":
    print(calc())