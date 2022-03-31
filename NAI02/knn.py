import csv
import random
import re
import sys


def calcDistance(train, test, size):
    distance = 0.0

    for i in range(size):
        distance = distance + (float(test[i])-float(train[i]))**2

    return distance


def findClosest(k, distances):
    names = {}

    for i in range(k):
        if distances[i][1] not in names:
            names[distances[i][1]] = 1
        else:
            names[distances[i][1]] += 1

    dict(sorted(names.items(), key=lambda item: item[1], reverse=True))
    print(names)

    return list(names.keys())[0]


def findVectorSize(list):
    size = 0

    for val in list:
        try:
            float(val)
            size += 1
        except:
            pass
    return size

def classifyByVector(trainList, testVector, vectorSize, k):
    for i in range(len(trainList)):
        distances = [ (calcDistance(item, testVector, size=vectorSize), item[vectorSize]) for item in trainList]
        distances.sort(key= lambda tup : tup[0])
        print('\n')
        klas = findClosest(k,distances)
        
    print("Classification: " + klas)

def main():
    if (len(sys.argv) < 4):
        print('Not enough arguments')
        return

    k = int(sys.argv[1])
    trainingSet = []
    testingSet = []
    dim = 0
    accuracy = 0

    with open(sys.argv[2], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for line in reader:
            trainingSet.append(line)

    with open(sys.argv[3], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for line in reader:
            testingSet.append(line)

    for set in trainingSet[0]:
        regex = re.match(r"^\d.\d", set)

        if regex:
            dim = dim + 1

    print('dim: ' + str(dim))

    randomSample = random.sample(testingSet, 10)

    for i in range(len(randomSample)):
        distances = [(calcDistance(item, randomSample[i], size=dim), item[dim])
                     for item in trainingSet]
        distances.sort(key=lambda tup: tup[0])
        print('\n')
        klas = findClosest(k, distances)
        test = randomSample[i][dim]
        print("Classification: " + klas)
        print("Test: " + test)
        if(klas == test):
            accuracy += 1

    print("\nAccuracy: " + str(100*float(accuracy)/float(len(randomSample)))+"%")
    print()

    print(f'Enter vector {dim} dimensional in format "a,b,c,...x"\nType quit to exit')
    while True:
        temp = input()
        if(temp == "quit" or temp == "q"):
            break

        vector = str(temp).split(",")
        
        classifyByVector(trainingSet, vector, dim, k)

if __name__ == '__main__':
    main()
