import Action as A
import Task as T

class Scheduler:
    def __init__(self, schedulerID, unit, productionline):
        self.schedulerID = schedulerID
        self.unit = unit
        self.actions = []
        self.productionline = productionline

    def getSchedulerID(self):
        return self.schedulerID
    
    def setSchedulerID(self, schedulerID):
        self.schedulerID = schedulerID

    def getUnit(self):
        return self.unit
    
    def setUnit(self, unit):
        self.unit = unit

    def reciveTasks(self, tasks):
        x = 1
        for task in tasks:
            action = A.Action(x, task.getNextBatch(), task, self.productionline)
            self.addAction(action)
    

    def addAction(self, action):
        self.actions.append(action)
        self.actions.sort(key = lambda x: x.getCompletionTime())

    def nextAction(self):
        nextAction = self.actions[0]
        self.actions.remove(nextAction)
        return nextAction





    