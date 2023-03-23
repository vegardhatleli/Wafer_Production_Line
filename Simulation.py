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

def createProductionLine():
    wafers = createListOfWafers(50)
    batch1 = B.Batch('Batch1', 50)
    batch1.setWafers(wafers)

    task1 = T.Task('Task1', 2.5)
    task2 = T.Task('Task2', 5.5)
    task3 = T.Task('Task3', 3.2)
    task4 = T.Task('Task4', 5.0)
    task5 = T.Task('Task5', 2.8)
    task6 = T.Task('Task6', 2.5)
    task7 = T.Task('Task7', 3.0)
    task8 = T.Task('Task8', 3.9)
    task9 = T.Task('Task9', 2.3)
    unit1 = U.Unit('Unit1')
    unit2 = U.Unit('Unit2')
    unit3 = U.Unit('Unit2')
    
    unit1.addTask(task1)
    unit1.addTask(task3)
    unit1.addTask(task6)
    unit1.addTask(task9)

    unit2.addTask(task2)
    unit2.addTask(task5)
    unit2.addTask(task7)

    unit3.addTask(task4)
    unit3.addTask(task8)

    productionLine = PL.ProductionLine()
    productionLine.addUnit(unit1)
    productionLine.addUnit(unit2)
    productionLine.addUnit(unit3)

    return productionLine

def simulation():
    productionLine = createProductionLine()



    while productionLine.getOutputBuffer() < 1000:
        productionLine.incrementTime()


    pass


simulation()