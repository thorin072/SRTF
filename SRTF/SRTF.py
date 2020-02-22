import ProcessInfo as process

#process1=process.ProcessInfo(1,0,7)
#process2=process.ProcessInfo(2,1,5)
#process3=process.ProcessInfo(3,2,3)
#process4=process.ProcessInfo(4,3,1)
#process5=process.ProcessInfo(5,4,2)
#process6=process.ProcessInfo(6,5,1)


#listProcess=[process1,process2,process3,process4,process5,process6]

process1=process.ProcessInfo(1,0,8)
process2=process.ProcessInfo(2,1,2)
process3=process.ProcessInfo(3,4,3)
listProcess=[process1,process2,process3]

def InCPU(num_process,time):
    print("<Executed by CPU: P{}>\n<TIME: {}>".format(num_process,time))

def NextProcess(applicants,key=False):
    min=1000;
    num_process=-1;
    #поиск процесса с самым коротким Burst Time
    for x in applicants:
        if key:
            if x.PlaceQueue<=min:
                min=x.PlaceQueue
                num_process=x.PID
        else:
            if x.BurstTime<=min:
                min_time=x.BurstTime
                num_process=x.PID
    return num_process

def GetIndex(applicants,PID_executed):
    return next((i for i, item in enumerate(applicants) if item.PID == PID_executed),None)

def UpdateQueue(listProcess,PID_ind,timeCPU,n,delete=False):
    
    swapPID=-10000
    curUpPID=-10000
    #поиск процессов с одинаковым Burst Time
    for x in listProcess:
        x.PlaceQueue-=1
        if x.ArrivalTime==timeCPU:
            #устанавливаем приоритет исполнения НОВОГО процесса по Arrival Time
            x.PlaceQueue=1
            curUpPID=x.PID #номер процесса по Arrival Time
            break
    if delete==False:
        listProcess[PID_ind].PlaceQueue=n
    
    flag_swap=False # флаг того,что произошел свайп пар процессов
    for x in range(0,len(listProcess)):
         for y in range(x+1,len(listProcess)):
            if (listProcess[x].BurstTime==listProcess[y].BurstTime):#одинаков Burst Time
                if (listProcess[x].PID<listProcess[y].PID):
                    listProcess[x].PlaceQueue, listProcess[y].PlaceQueue = listProcess[y].PlaceQueue, listProcess[x].PlaceQueue #swap местами в очереди
                    swapPID=listProcess[x].PID
    
    curIndex=GetIndex(listProcess,curUpPID)
    swapIndex=GetIndex(listProcess,swapPID)

    if curIndex is not None:
        if swapIndex is not None:
            d=0
            if listProcess[curIndex].BurstTime==listProcess[swapIndex].BurstTime:
                if (listProcess[curIndex].PID>listProcess[swapIndex].PID):
                    
                    for x in listProcess: 
                        if (x.PID==swapIndex):
                            continue
                        x.PlaceQueue+=1
                    listProcess[swapIndex].PlaceQueue=1
                    listProcess[curIndex].PlaceQueue=2


              
           

              

def GetGantt(listProcess):
    time_CPU=0;
    sl=2
    prev=-1;#индекс предпоследнего
    applicants=[x for x in listProcess if x.ArrivalTime==0] #поиск всех процессов с Arrival Time=0
    #поиск процессов с мин Burst Time при Arrival Time=0
    PID_executed=NextProcess(applicants);
    print('Start process is: P',PID_executed);
   
    while True:
        if listProcess:
            InCPU(PID_executed,time_CPU)
            time_CPU+=1;
            print('TIME UPD:{}\n\----------------/'.format(time_CPU))
            #находим процесс (индекс) который только что исполнялся
            PID_executed_index=GetIndex( listProcess,PID_executed)
            #уменьшаем Burst Time
            listProcess[PID_executed_index].BurstTime-=1
            if listProcess[PID_executed_index].BurstTime==0:
                print("<COMPLATED: P{}>\n<TIME: {}> \n/-----------------------/".format(listProcess[PID_executed_index].PID,time_CPU))
                listProcess.pop(PID_executed_index);
                UpdateQueue(listProcess[:sl],PID_executed_index-1,time_CPU,len(listProcess),True)
                PID_executed=NextProcess(listProcess[:sl],key=True);
                sl+=1
            else:
                #обновление очереди
                UpdateQueue(listProcess[:sl],PID_executed_index,time_CPU,len(listProcess),False)
                PID_executed=NextProcess(listProcess[:sl],key=True);
                sl+=1
        else:
            return 0


GetGantt(listProcess);