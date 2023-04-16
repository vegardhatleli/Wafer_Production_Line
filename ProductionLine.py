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
        print(f'Task finished: {unit.getUnitID()} | {taskID} | {completedBatch.getBatchID()} | {self.getTime()}')
        if taskID == 'Task9':
            self.addOutputBuffer(completedBatch)
            unit.getActiveTask().setBatch(None)
            unit.setActiveTask(None)
            print(f'{completedBatch.getBatchID()} done')
            return
        unit.getActiveTask().getNextTask().addToInputBuffer(completedBatch)
        #self.getTaskByID(f'{taskID[:4]}{int(taskID[4:5])+1}').addToInputBuffer(completedBatch)
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
            #nextTask = self.getTaskByID(f'{task.taskID[:4]}{int(task.taskID[4:5])+1}')
            nextTask = task.getNextTask()
            if (nextTask.inputBufferAvalible(task.getInputBuffer()[0].getSize())):
                #print(f'{nextTask.getTaskID()} ## {nextTask.getSizeOfInputBuffer()}')
                return task
            
        #print('All output buffers full, needs to wait')
        return