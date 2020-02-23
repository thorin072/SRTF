import SRTF as srtf
import GeneratorProcess as gp
import GanttDiogramm as GD

if __name__ == "__main__":
    list_proc=gp.GeneratorProcess().Test()
    #list_proc=gp.GeneratorProcess().AnyCombination(n,n,10,10)
    n_proc=len(list_proc) #число процессов
    queue_srtf=srtf.SRTF(list_proc).GetSequenceProcesses()
    GD.GanttDiogramm().DrawProcess(queue_srtf,n_proc)
   
