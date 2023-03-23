import Task as t


class Unit:

    def __init__(self, unitID):
        self.unitID = unitID
        self.tasks = []
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

    def setAvailable(self):
        self.isAvailable = True

    def setOccupied(self):
        self.isAvailable = False
    
    def getAvailability(self):
        return self.isAvailable

    def whichTaskIsNext(self):
        if self.getAvailability():
            availableTasks = []
            for task in self.getTasks():
                if len(task.getInputBuffer()) != 0:
                    availableTasks.append(task)
            return max(availableTasks, key=lambda x: x.getProcessingTime())

    #preformTimeStep