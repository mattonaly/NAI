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

    for i in range(len(testingSet)):
        distances = [(calcDistance(item, testingSet[i], size=dim), item[dim])
                     for item in trainingSet]
        distances.sort(key=lambda tup: tup[0])
        print('\n')
        klas = findClosest(k, distances)
        test = random.sample(testingSet, 1)[0][dim]
        print("Classification: " + klas)
        print("Test: " + test)
        if(klas == test):
            accuracy += 1

    print("\nAccuracy: " + str(100*float(accuracy)/float(len(testingSet)))+"%")


if __name__ == '__main__':
    main()
