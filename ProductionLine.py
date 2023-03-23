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





