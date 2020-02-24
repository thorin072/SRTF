import ProcessInfo as process
import random

class GeneratorProcess(object):
    def __init__(self):
        self.array=None
        self.count=None;
    def Test (self):
        #process1=process.ProcessInfo(1,0,7)
        #process2=process.ProcessInfo(2,1,5)
        #process3=process.ProcessInfo(3,2,3)
        #process4=process.ProcessInfo(4,3,1)
        #process5=process.ProcessInfo(5,4,2)
        #process6=process.ProcessInfo(6,5,1)
        #self.array=[process1,process2,process3,process4,process5,process6]

        
        process1=process.ProcessInfo(1,0,8)
        process2=process.ProcessInfo(2,1,2)
        process3=process.ProcessInfo(3,4,3)
        self.array=[process1,process2,process3]
        return self.array
    def AnyCombination(self,count):
        pid=set()
        arrival=set()
        i=0
        self.count=count;
        self.array=[];
        num_process=count
        num_arrival=count+10
        num_burst=count+20
        while True:
            if (self.count==i):
                if 0 not in arrival:
                     self.array.append(process.ProcessInfo(num_process+1,0,random.randint(1,num_burst)))
                return sorted(self.array, key=lambda el: el.ArrivalTime)
            p_g=random.randint(1,num_process)
            a_g=random.randint(0,num_arrival)
            b_g=random.randint(1,num_burst)
            if p_g not in pid:
                if a_g not in arrival:
                    pid.add(p_g)
                    arrival.add(a_g)
                    self.array.append(process.ProcessInfo(p_g,a_g,b_g))
                    i+=1
            else:
                continue

    """description of class"""


