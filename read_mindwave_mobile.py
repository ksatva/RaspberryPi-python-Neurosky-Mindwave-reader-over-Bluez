import numpy as np


import time 
import bluetooth 
from MindwaveDataPoints import RawDataPoint 
from MindwaveDataPointReader import MindwaveDataPointReader


if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    
    count=0;
    rawdata=[];
    #while(True):
    while(count<=100):
        
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        #if (not dataPoint.__class__ is RawDataPoint):
         #   print dataPoint
      
        if (dataPoint.__class__ is RawDataPoint):
            
	    rawdata.append(dataPoint.rawValue)
            #print dataPoint
       	    count+=1    # set to limit the duration of recording in "while(true)"
 
    print rawdata
    #rawdata_=rawdata[:,2,:]
    #print "\n\n\n"
     #print rawdata_

    x=rawdata
    x1,x2,x3,x4,x5=np.split(x,[20,40,60,80])
    print "\n"
    print x1
    print "\n"
    print x2 
    print x3
    print x4 
    print x5
    
