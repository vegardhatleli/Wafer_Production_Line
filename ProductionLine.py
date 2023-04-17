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
        self.batchData = []

    def getProductionLineID(self):
        return self.productionLineID

    def addBatchData(self, time):
        self.batchData.append(time)

    def getBatchData(self):
        return self.batchData

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
        #print(f'Task finished: {unit.getUnitID()} | {taskID} | {completedBatch.getBatchID()} | {self.getTime()}')
        if taskID == 'Task9':
            self.addOutputBuffer(completedBatch)
            unit.getActiveTask().setBatch(None)
            unit.setActiveTask(None)
            #print(f'{completedBatch.getBatchID()} done')
            self.addBatchData(self.getTime())
            return
        unit.getActiveTask().getNextTask().addToInputBuffer(completedBatch)
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

    def findNextTask(self, unit):
        pendingTasks = []
        for task in unit.getTasks():
            if len(task.getInputBuffer()) > 0:
                pendingTasks.append(task)
        if len(pendingTasks) == 0:
            return
        pendingTasks.sort(key = lambda x: x.getProcessingTime() * x.getInputBuffer()[0].getSize() + 2.0)
        for task in pendingTasks:
            if task.taskID == 'Task9':
                return task
            nextTask = task.getNextTask()
            if (nextTask.inputBufferAvalible(task.getInputBuffer()[0].getSize())):
                return task
            
        return

    def findNextTaskGiverOrder(self, unit, orderUnit1, orderUnit2, orderUnit3):
        neworder1 = {orderUnit1[0] : 1, orderUnit1[1] : 2, orderUnit1[2] : 3, orderUnit1[3] : 4}
        neworder2 = {orderUnit2[0] : 1, orderUnit2[1] : 2, orderUnit2[2] : 3}
        neworder3 = {orderUnit3[0] : 1, orderUnit3[1] : 2}
        if (unit.getUnitID() == 'Unit1'):
            tasks = sorted(unit.getTasks(), key = lambda x: neworder1[x.getTaskID()])
        if (unit.getUnitID() == 'Unit2'):
            tasks = sorted(unit.getTasks(), key = lambda x: neworder2[x.getTaskID()])
        if (unit.getUnitID() == 'Unit3'):
            tasks = sorted(unit.getTasks(), key = lambda x: neworder3[x.getTaskID()])

        pendingTasks = []
        for task in tasks:
            if len(task.getInputBuffer()) > 0:
                pendingTasks.append(task)
        if len(pendingTasks) == 0:
            return

        for task in pendingTasks:
            if task.taskID == 'Task9':
                return task
            nextTask = task.getNextTask()
            if (nextTask.inputBufferAvalible(task.getInputBuffer()[0].getSize())):
                return task
