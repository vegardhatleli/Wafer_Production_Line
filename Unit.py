import Task as t


class Unit:

    def __init__(self, unitID):
        self.unitID = unitID
        self.tasks = []
        self.activeTask = None
        self.downCounter = 0
        self.isAvailable = True

    def getUnitID(self):
        return self.unitID

    def setUnitID(self, unitID):
        self.unitID = unitID

    def addTask(self, task):
        self.tasks.append(task)

    def getTasks(self):
        return self.tasks

    def setDownCounter(self, count):
        self.downCounter = count
    
    def getDownCounter(self):
        return self.downCounter

    def decrementDownCounter(self):
        self.downCounter -= 0.1
        self.downCounter = round(self.downCounter, 1)

    def setAvailable(self):
        self.isAvailable = True

    def setOccupied(self):
        self.isAvailable = False
    
    def getAvailability(self):
        return self.isAvailable

    def getActiveTask(self):
        return self.activeTask

    def setActiveTask(self, task):
        self.activeTask = task

    def isThereAvailableBatches(self):
        for task in self.getTasks():
            if len(task.getInputBuffer()) > 0:
                return True
            else:
                return False

    
    def runNextTask(self, task, time):
        task.setBatch(task.getNextBatch())
        self.setActiveTask(task)
        self.setDownCounter(float(task.getProcessingTime()) * float(task.getBatch().getSize()) + 2.0)
        self.setOccupied()
        print(f'Task started: {self.getUnitID()} | {task.getTaskID()} | {task.getBatch().getBatchID()} | {time}')