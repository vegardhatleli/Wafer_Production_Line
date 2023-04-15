import ProductionLine as P
import Batch as B
import Task as T

class Action:
    def __init__(self, actionID, batch, task, productionLine):
        self.actionID = actionID
        self.batch = batch
        self.task = task
        self.productionLine = productionLine
        currentTime = self.productionLine.getTime()
        workingTime = (self.batch.getSize() * self.task.getProcessingTime()) + 2.0
        self.completionTime = currentTime + workingTime

    def setBatch(self, batch):
        self.batch = batch
        
    def getBatch(self):
        return self.batch

    def setTask(self, task):
        self.task = task
    
    def getTask(self):
        return self.task

    def setProductionLine(self, productionline):
        self.productionLine = productionline

    def getProductionLine(self):
        return self.productionLine

    def setCompletionTime(self):
        currentTime = self.productionLine.getTime()
        workingTime = (self.batch.getSize() * self.task.getProcessingTime()) + 2.0
        self.completionTime = currentTime + workingTime

    def getCompletionTime(self):
        return self.completionTime




