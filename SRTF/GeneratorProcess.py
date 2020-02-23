import ProcessInfo as process
import random

class GeneratorProcess(object):
    def __init__(self):
        self.array=None
        self.count=None;
    def Test (self):
        process1=process.ProcessInfo(1,0,7)
        process2=process.ProcessInfo(2,1,5)
        process3=process.ProcessInfo(3,2,3)
        process4=process.ProcessInfo(4,3,1)
        process5=process.ProcessInfo(5,4,2)
        process6=process.ProcessInfo(6,5,1)
        self.array=[process1,process2,process3,process4,process5,process6]
        return self.array
    def AnyCombination(self,count,num_process,num_arrival,num_burst):
        pid=set()
        arrival=set()
        i=0
        self.count=count;
        self.array=[];
        while True:
            if (self.count==i):
                if 0 not in arrival:
                     self.array.append(process.ProcessInfo(num_process+1,0,random.randint(1,num_burst)))
                return self.array
            p_g=random.randint(0,num_process)
            a_g=random.randint(0,num_arrival)
            b_g=random.randint(1,num_burst)
            if p_g not in pid:
                pid.add(p_g)
                arrival.add(a_g)
                self.array.append(process.ProcessInfo(p_g,a_g,b_g))
                i+=1
            else:
                continue

    """description of class"""


