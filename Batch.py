class Batch:

    def __init__(self, batchID, size):
        self.batchID = batchID
        self.size = size
        self.wafers = []

    def setBatchID(self, batchID):
        self.batchID = batchID

    def setSize(self, size):
        self.size = size

    def setWafers(self, wafers):
        for wafer in wafers:
            self.wafers.append(wafer)
    
    def getBatchID(self):
        return self.batchID

    def getSize(self):
        return self.size

    def getWafers(self):
        return self.wafers

