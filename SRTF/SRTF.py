import ProcessInfo as process
import Plot as pl

class SRTF(object):
   def __init__(self, array):
        self.array=array
   def __InCPU(self,num_process,time):
       print("<Executed by CPU: P{}>\n<TIME: {}>".format(num_process,time))
   
   def __NextProcess(self,applicants,key=False):
       min=1000;
       num_process=-1;
        #поиск процесса с самым коротким Burst Time
       for x in applicants:
           if key:
               if x.PlaceQueue is not None:
                   if x.PlaceQueue<=min:
                       min=x.PlaceQueue
                       num_process=x.PID
               else: pass
           else:
               if x.BurstTime<=min:
                   min_time=x.BurstTime
                   num_process=x.PID
       return num_process 
   
   def __GetIndex(self,mass,PID_executed):
       return next((i for i, item in enumerate(mass) if item.PID == PID_executed),None)
   
   def GetSequenceProcesses(self):
       list_pos_srtf=[] #последовательность исполнения процессов
       time_CPU=0;
       sl=2
       applicants=[x for x in self.array if x.ArrivalTime==0] #поиск всех процессов с Arrival Time=0
       #поиск процессов с мин Burst Time при Arrival Time=0
       PID_executed=self.__NextProcess(applicants);
       prev=PID_executed#индекс предпоследнего
       print('Start process is: P',PID_executed);
       while True:
           if self.array:
               el_srtf=pl.Plot()
               el_srtf.pos='P'+str(PID_executed)
               el_srtf.start_time=time_CPU
               self.__InCPU(PID_executed,time_CPU)
               time_CPU+=1;
               el_srtf.end_time=time_CPU
               list_pos_srtf.append(el_srtf)

               print('TIME UPD:{}\n\----------------/'.format(time_CPU))
               #находим процесс (индекс) который только что исполнялся
               PID_executed_index=self.__GetIndex(self.array,PID_executed)
               #уменьшаем Burst Time
               self.array[PID_executed_index].BurstTime-=1
               if self.array[PID_executed_index].BurstTime==0:
                   print("<COMPLATED: P{}>\n<TIME: {}> \n/-----------------------/".format(self.array[PID_executed_index].PID,time_CPU))
                   self.array.pop(PID_executed_index);
                   self.__UpdateQueue(self.array[:sl],PID_executed_index-1,time_CPU,len(self.array),True,prev)
                   PID_executed=self.__NextProcess(self.array[:sl],key=True);
                   prev=PID_executed
                   sl+=1
               else:
                    #обновление очереди
                   #процесс который был завершен
                    self.__UpdateQueue(self.array[:sl],PID_executed_index,time_CPU,len(self.array),prev,False)
                    PID_executed=self.__NextProcess(self.array[:sl],key=True);
                    prev=PID_executed
                    sl+=1
           else:
                return list_pos_srtf 
   
   def __UpdateQueue(self,listProcess,PID_ind,timeCPU,n,prev_PID,delete=False):
       swapPID=-10000
       curUpPID=-10000
       flag_boostburst=False 
       flag_swap=False # флаг того,что произошел свайп пар процессов
       #поиск процессов с одинаковым Burst Time
       for x in listProcess:
           if x.PlaceQueue is None:
               pass
           else: 
               x.PlaceQueue-=1
               curUpPID=x.PID 
           if x.ArrivalTime==timeCPU:
               #устанавливаем приоритет исполнения НОВОГО процесса по Arrival Time
               x.PlaceQueue=1
               curUpPID=x.PID #номер процесса по Arrival Time
               break
       if delete==False:
           listProcess[PID_ind].PlaceQueue=100
       
       #ситуация когда актуальный процесс имеет меньший Burst чем предыдущий
       curIndex=self.__GetIndex(listProcess,curUpPID)
       swapIndex=self.__GetIndex(listProcess,prev_PID)
       if curIndex is not None:
           if swapIndex is not None:
            if listProcess[curIndex].BurstTime<=listProcess[swapIndex].BurstTime:
                listProcess[curIndex].PlaceQueue=0
                #listProcess[swapIndex].PlaceQueue=2
                flag_boostburst=True;


       for x in range(0,len(listProcess)):
           for y in range(x+1,len(listProcess)):
               if (listProcess[x].BurstTime==listProcess[y].BurstTime):#одинаков Burst Time
                   if (listProcess[x].PID<listProcess[y].PID):
                       listProcess[x].PlaceQueue, listProcess[y].PlaceQueue = listProcess[y].PlaceQueue, listProcess[x].PlaceQueue #swap местами в очереди
                       swapPID=listProcess[x].PID
       curIndex=self.__GetIndex(listProcess,curUpPID)
       swapIndex=self.__GetIndex(listProcess,swapPID)
       
       if curIndex is not None:
           if swapIndex is not None:
            if listProcess[curIndex].BurstTime==listProcess[swapIndex].BurstTime:
                if (listProcess[curIndex].PID>listProcess[swapIndex].PID):
                    for x in listProcess: 
                        if (x.PID==swapIndex):
                            continue
                        if x.PlaceQueue is None:
                            pass
                        else:
                            x.PlaceQueue+=1
                    listProcess[swapIndex].PlaceQueue=0
                    listProcess[curIndex].PlaceQueue=1





