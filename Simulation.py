import sys
import Wafer as W
import Batch as B
import Task as T
import Unit as U
import ProductionLine as PL

def createListOfWafers(numberOfWafers):
    listOfWafers = []
    for i in range(numberOfWafers):
        listOfWafers.append(W.Wafer(f'Wafer{i}'))
    return listOfWafers

def createListOfBatches(NumberofBatches, NumberOfWafers):
    batches = []
    for i in range(NumberofBatches):
        wafers = createListOfWafers(NumberOfWafers)
        batch = B.Batch(f'Batch{i+1}', NumberOfWafers)
        batch.setWafers(wafers)
        batches.append(batch)
    return batches

def createProductionLine():
    batches = createListOfBatches(20,50)
    wafers = createListOfWafers(50)
    batch1 = B.Batch('Batch1', 50)
    batch1.setWafers(wafers)

    task1 = T.Task('Task1', 0.5)
    task2 = T.Task('Task2', 3.5)
    task3 = T.Task('Task3', 1.2)
    task4 = T.Task('Task4', 3.0)
    task5 = T.Task('Task5', 0.8)
    task6 = T.Task('Task6', 0.5)
    task7 = T.Task('Task7', 1.0)
    task8 = T.Task('Task8', 1.9)
    task9 = T.Task('Task9', 0.3)

    task1.setNextTask(task2)
    task2.setNextTask(task3)
    task3.setNextTask(task4)
    task4.setNextTask(task5)
    task5.setNextTask(task6)
    task6.setNextTask(task7)
    task7.setNextTask(task8)
    task8.setNextTask(task9)

    unit1 = U.Unit('Unit1')
    unit2 = U.Unit('Unit2')
    unit3 = U.Unit('Unit3')
    unit1.addTask(task1)
    unit1.addTask(task3)
    unit1.addTask(task6)
    unit1.addTask(task9)

    unit2.addTask(task2)
    unit2.addTask(task5)
    unit2.addTask(task7)

    unit3.addTask(task4)
    unit3.addTask(task8)

    productionLine = PL.ProductionLine('Wafer Production')
    productionLine.addUnit(unit1)
    productionLine.addUnit(unit2)
    productionLine.addUnit(unit3)
    productionLine.setStorage(batches)

    return productionLine

def simulation():
    f = open("output.out", "w")
    sys.stdout = f
    productionLine = createProductionLine()
    while len(productionLine.getOutputBuffer()) < 20:
        if (productionLine.getTime() % 1 == 0 and len(productionLine.getStorage()) > 0):
            productionLine.getUnits()[0].getTasks()[0].addToInputBuffer(productionLine.getNextBatch())
        productionLine.incrementTime()
        for unit in productionLine.getUnits():
            if unit.getDownCounter() > 0:
                unit.decrementDownCounter()

            if (unit.getDownCounter() == 0):
                productionLine.passBatchToNextTask(unit)
                unit.setAvailable()

            if (unit.getAvailability()):
                task = productionLine.findNextTask(unit)
                if task != None:
                    unit.runNextTask(task, productionLine.getTime())
    return productionLine.getTime()


print(simulation())