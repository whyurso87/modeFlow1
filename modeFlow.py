from FlowPool import Parallel_All_IntegrationFlow
import TaskPool
from taskflow.patterns import linear_flow

class ModeFlow():
    def __init__(self):
        self.mode1Flow = linear_flow.Flow(self.__class__.__name__)
        self.parallel_All_IntegrationFlow = Parallel_All_IntegrationFlow(self.__class__.__name__, 'frame').buildFlow()
       
    def buildFlow(self): 
        self.mode1Flow.add(
            TaskPool.frameTask(self.__class__.__name__ + '_frameTask',provides = 'frame'),
            TaskPool.yoloTask(self.__class__.__name__+'yoloTask', requires = 'frame', provides = 'frame'),
            TaskPool.wholeTask(self.__class__.__name__+'wholeTask', requires = 'frame', provides = 'frame'),
            self.parallel_All_IntegrationFlow              
        )

        return self.mode1Flow
