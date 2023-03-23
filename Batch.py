class Batch:

    def __init__(self, batch_ID, size):
        self.batch_ID = batch_ID
        self.size = size
        self.wafers = []

    def setBatchID(self, batchID):
        self.batch_ID = batchID

    def setSize(self, size):
        self.size = size

    def setWafers(self, wafers):
        self.wafers = wafers
    
    def getBatchID(self):
        return self.batch_ID

    def getSize(self):
        return self.size

    def getWafers(self):
        return self.wafers

