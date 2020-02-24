import SRTF as srtf
import GeneratorProcess as gp
import GanttDiogramm as GD
from prettytable import PrettyTable

if __name__ == "__main__":
    #list_proc=gp.GeneratorProcess().Test()
    list_proc=gp.GeneratorProcess().AnyCombination(10)
    n_proc=len(list_proc) #число процессов
    PID_ID=[x.PID for x in list_proc]
    table_info=PrettyTable()
    table_info.field_names = ["PID", "Arrival Time", "Burst Time"]
    for x in list_proc:
         table_info.add_row([x.PID, x.ArrivalTime, x.BurstTime])
    print(table_info)
    queue_srtf=srtf.SRTF(list_proc).GetSequenceProcesses()
    GD.GanttDiogramm().DrawProcess(queue_srtf,n_proc,PID_ID)
   
