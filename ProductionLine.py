import Wafer as W
import Batch as B
import Task as T
import Unit as U

class ProductionLine:

    def __init__(self, productionLineID):
        self.productionLineID = productionLineID
        self.units = []
        self.time = 0
        self.outputBuffer = 0

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

    def addOutputBuffer(self, batch):
        self.outputBuffer += batch.getSize()

    def getOutputBuffer(self):
        return self.outputBuffer

    def getTime(self):
        return self.time

    def getTaskByID(self, taskID):
        for unit in self.getUnits():
            for task in unit:
                if task.getTaskID() == taskID:
                    return task
            
    def passBatchToNextTask(self, unit):
        completedBatch = unit.getActiveTask().getBatch()
        taskID = unit.getActiveTask().getTaskID()
        if taskID == 'Task9':
            return print('FERDIG')
        self.getTaskByID(f'{taskID[:4]}{int(taskID[4:5])+1}').addToInputBuffer(completedBatch)
        #receivingTask = self.getTaskByID(f'{taskID[:4]}{int(taskID[4:5])+1}')
        #receivingTask.addToInputBuffer(completedBatch)
        unit.getActiveTask.setBatch(None)
        unit.setActiveTask(None)


