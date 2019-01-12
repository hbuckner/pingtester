from pythonping import ping
import matplotlib.pyplot as plt
import numpy as np
import time
import sys

arg1=str(sys.argv[1])
arg2=int(sys.argv[2])

#PingServer:
#Input: (str,int)
#Description: takes in address to ping and amount of time to ping in min and Determines if ping spikes are occuring or not, outputs a graph to see ping
def PingServer(address, timemin):

    responselist = ping(address, count=timemin*60)
    ms=[]

    for x in responselist._responses:
        time.sleep(1)
        ms.append(x.time_elapsed_ms)
    if responselist.rtt_max_ms <70:
        print("You're good to play!")
    else:
        print("Ping is too high to play")

    plt.plot(ms)
    plt.show()

PingServer(arg1,arg2)
#104.160.131.3
