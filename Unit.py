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

    
    def runNextTask(self):
        availableTasks = []
        for task in self.getTasks():
            if len(task.getInputBuffer()) > 0:
                availableTasks.append(task)
        if len(availableTasks) == 0:
            #rint('Ingen mulige batches å hente')
            return
        nextTask = max(availableTasks, key=lambda x: x.getProcessingTime())
        nextTask.setBatch(nextTask.getNextBatch())
        self.setActiveTask(nextTask)
        self.setDownCounter(float(nextTask.getProcessingTime()) * float(nextTask.getBatch().getSize()) + 2.0)
        self.setOccupied()

    #preformTimeStep