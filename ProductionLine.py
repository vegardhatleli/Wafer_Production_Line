import Wafer as W
import Batch as B
import Task as T
import Unit as U

class ProductionLine:

    def __init__(self, productionLineID):
        self.productionLineID = productionLineID
        self.units = []
        self.time = 0
        self.outputBuffer = []
        self.storage = []

    def getProductionLineID(self):
        return self.productionLineID

    def setProductionLineID(self, proproductionLineID):
        self.productionLineID = proproductionLineID

    def addUnit(self, unit):
        self.units.append(unit)

    def getUnits(self):
        return self.units

    def removeUnit(self, unit):
        self.units.remove(unit)

    def incrementTime(self):
        self.time += 0.1
        self.time = round(self.time, 1)

    def addOutputBuffer(self, batch):
        self.outputBuffer.append(batch)

    def getOutputBuffer(self):
        return self.outputBuffer

    def getTime(self):
        return self.time

    def getTaskByID(self, taskID):
        for unit in self.getUnits():
            for task in unit.getTasks():
                if task.getTaskID() == taskID:
                    return task
            
    def passBatchToNextTask(self, unit):
        if (unit.getActiveTask() == None):
            return
        completedBatch = unit.getActiveTask().getBatch()
        taskID = unit.getActiveTask().getTaskID()
        if taskID == 'Task9':
            self.addOutputBuffer(completedBatch)
            unit.getActiveTask().setBatch(None)
            unit.setActiveTask(None)
            print(f'{completedBatch.getBatchID()} done')
            return
        self.getTaskByID(f'{taskID[:4]}{int(taskID[4:5])+1}').addToInputBuffer(completedBatch)
        unit.getActiveTask().setBatch(None)
        unit.setActiveTask(None)

    def getStorage(self):
        return self.storage
    
    def setStorage(self, batches):
        self.storage = batches
    
    def getNextBatch(self):
        if len(self.storage) != 0:
            batch = self.storage[0]
            self.storage.remove(batch)
            return batch
        return []

'''
pl = ProductionLine('1')
task1 = T.Task('Task1',1)
task2 = T.Task('Task2',1)
unit = U.Unit('Unit1')
unit.addTask(task1)
unit.addTask(task2)
pl.addUnit(unit)
hei = 'Task1'

print(pl.getTaskByID(f'{hei[:4]}{int(hei[4:5])+1}').getTaskID())

print(f'{hei[:4]}{int(hei[4:5])+1}')
'''
