import plotly.graph_objs as go
import plotly.figure_factory as ff
import random
class GanttDiogramm(object):
    def __init__(self):
        pass
    def DrawProcess(self,array,n):
        df=[]
        color_d=dict()
        for i in range(1,n+1):
            r = random.randint(0,255)
            g=random.randint(0,155)
            b=random.randint(0,255)
            color_d.update({'P'+str(i):'rgb({},{},{})'.format(r,g,b)})
        for x in array:
            el=dict(Task=x.pos, Start=str(x.start_time), Finish=str(x.end_time),Resource=x.pos)
            df.append(el)
        fig = ff.create_gantt(df,colors=color_d, index_col='Resource', title='GANTT Process',show_colorbar=True, bar_width=0.5, showgrid_x=True, showgrid_y=True, group_tasks=True)
        
        fig['layout']['xaxis'].update({'type': None})

        fig.show()
    """description of class"""


