from itertools import permutations
import sys
import matplotlib.pyplot as plt
import Wafer as W
import Batch as B
import Task as T
import Unit as U
import ProductionLine as PL
import math

## SETUP FUNCTIONS
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

def createProductionLine(numberOfBatches, numberOfWafers, rest):
    if rest == 0:
        batches = createListOfBatches(numberOfBatches,numberOfWafers)

    if rest <= 50 and rest != 0:
        batches = createListOfBatches(numberOfBatches,numberOfWafers)
        wafers = createListOfWafers(rest)
        restBatch = B.Batch(f'Batch{numberOfBatches+1}', rest)
        restBatch.setWafers(wafers)
        batches.append(restBatch)

    if rest > 50:
        batches = createListOfBatches(numberOfBatches,numberOfWafers)
        wafers1 = createListOfWafers(math.ceil(rest/2))
        wafers2 = createListOfWafers(math.floor(rest/2))
        restBatch1 = B.Batch(f'Batch{numberOfBatches+1}', math.ceil(rest/2))
        restBatch2 = B.Batch(f'Batch{numberOfBatches+1}', math.floor(rest/2))
        restBatch1.setWafers(wafers1)
        restBatch2.setWafers(wafers2)
        batches.append(restBatch1)
        batches.append(restBatch2)

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

## SIMULATIONS
def simulation(inputInterval, numberOfBatches, numberOfWafers, rest):
    f = open("output.out", "w")
    sys.stdout = f
    productionLine = createProductionLine(numberOfBatches, numberOfWafers, rest)
    while_parameter = len(productionLine.getStorage())
    while len(productionLine.getOutputBuffer()) < while_parameter:
        if (productionLine.getTime() % inputInterval == 0 and len(productionLine.getStorage()) > 0):
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
    print(productionLine.getTime())
    f.close()
    return productionLine.getTime(), productionLine.getBatchData()

def simulationWithHeuristic(inputInterval, orderUnit1, orderUnit2, orderUnit3):
    f = open("Task6/FinishedTimeWithDifferentHeuristic.txt", "a")
    productionLine = createProductionLine(20,50,0)
    while len(productionLine.getOutputBuffer()) < 20:
        if (productionLine.getTime() % inputInterval == 0 and len(productionLine.getStorage()) > 0):
            productionLine.getUnits()[0].getTasks()[0].addToInputBuffer(productionLine.getNextBatch())
        productionLine.incrementTime()
        for unit in productionLine.getUnits():
            if unit.getDownCounter() > 0:
                unit.decrementDownCounter()

            if (unit.getDownCounter() == 0):
                productionLine.passBatchToNextTask(unit)
                unit.setAvailable()

            if (unit.getAvailability()):
                task = productionLine.findNextTaskGiverOrder(unit,orderUnit1, orderUnit2, orderUnit3)
                if task != None:
                    unit.runNextTask(task, productionLine.getTime())

    f.write('{:<15} {:<15} {:<15} {:<15}\n'.format(f'{str(orderUnit1)} |' , f'{str(orderUnit2)} |', f'{str(orderUnit3)} |', f'{str(productionLine.getTime())}'))
    f.close()
    return

## OPTIMIZE FUNTIONS
def optimizeBatchSize():
    totalTimes = []
    numberOfWafersInBatch = []
    all_batches = createAllPossibleBatches()
    for batch in all_batches:
        time, data = simulation(1, batch[0], batch[1], batch[2])
        numberOfWafersInBatch.append(batch[1])
        totalTimes.append(time)
    return numberOfWafersInBatch, totalTimes

def optimizeTimeBetweenBatches():
    graphData = []
    totalTimes = []
    intervals = [653.5, 500, 400, 300, 200, 100, 50, 25, 15, 10, 5, 2]
    for interval in intervals:
        time, data = simulation(interval, 20, 50, 0)
        totalTimes.append(time)
        graphData.append(data)

    return intervals, totalTimes, graphData

## CREATE PLOTS
def createBatchFinishedTable(intervals, totalTimes):
    f = open("Task7/NumberOfWafersPerBatch.txt", "w")
    f.write('{:<25} {:<15}\n'.format('NumberOfWafersPerBatch', 'Total time used'))
    for i in range(len(intervals)):
        f.write("{:<25} {:<15}\n".format(f'{str(intervals[i])}', f'{str(totalTimes[i])}'))
    f.close()

def createBarChart(xData, yDsta):
    numberOfWafers = xData
    totalTime = yDsta
    for i in range(len(xData)):
        plt.bar(numberOfWafers[i], totalTime[i], width=0.6)

    plt.xlabel('Number of wafers in each batch')
    plt.ylabel('Total time')
    plt.title('Chart of finished time for each batch')

    plt.savefig('Task7/NumberOfWafersPerBatchBarChart') 

def createBatchFinishedGraph(graphData):
    batches = []
    for i in range(len(graphData[0])):
        batches.append(f'{i + 1}')
    
    for element in graphData:
        plt.plot(batches, element)

    plt.xlabel('Batch')
    plt.ylabel('Time')
    plt.title('Chart of finished time for each batch')

    plt.savefig('Task5/ReduceIntervalBetweenBatches')

def createHeuristicTable():
    f = open("Task6/FinishedTimeWithDifferentHeuristic.txt", "w")
    f.write('{:<37} {:<29} {:<24} {:<15} \n'.format('Unit1 Heuristic ', 'Unit2 Heuristic ', 'Unit3 Heuristic ', 'Total time used'))
    f.write('\n')
    f.close()
    unit1 = list(permutations(['Task1','Task3','Task6','Task9']))
    unit2 = list(permutations(['Task2','Task5','Task7']))
    unit3 = list(permutations(['Task4','Task8']))

    for order1 in unit1:
        for order2 in unit2:
            for order3 in unit3:
                simulationWithHeuristic(2, order1, order2, order3)
    
    return

## SUPPORTFINCTIONS
#Retruns all possible permutations of batchsizes
def createAllPossibleBatches():
    allPossibleBatches = []
    for i in range(20,51):
        numberOfWafers = i
        numberOfBatches = 1000 // i
        rest = 1000 % i
        if (rest != 0 and rest + numberOfWafers >= 50):
            rest = numberOfWafers + rest
            numberOfBatches -= 1
        if (rest != 0 and rest + numberOfWafers < 50):
            rest = numberOfWafers + rest
        allPossibleBatches.append([numberOfBatches,numberOfWafers,rest])
        #print(f'Batches: {numberOfBatches}, wafers: {numberOfWafers} rest: {rest}')
    return allPossibleBatches


## MAIN
#The simulation with out fastest total time
#For result look in the output.out
simulation(1,26,36,64)


