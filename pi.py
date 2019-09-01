import random
import math
import sys
import matplotlib.pyplot as plt

def calculation(tries):
    impo = open("pi-file.txt", "r")
    ins = impo.readline()
    tot = impo.readline()
    impo.close()

    insNum = ""
    totNum = ""

    for i in range(4,len(ins)):
        insNum = insNum + str(ins[i])

    for i in range(4,len(tot)):
        totNum = totNum + str(tot[i])

    ins = int(insNum)
    tot = int(totNum)

    print("Starting with numbers: " + str(ins) + " and " + str(tot))

    for x in range(0, int(tries)):
        for i in range(0, 200000):
            posX = random.randint(0, 10000)/10000
            posY = random.randint(0, 10000)/10000
            
            if math.hypot(posX, posY) < 1:
                ins = ins + 1
            tot = tot + 1

            

        pi = ins / tot * 4
        sys.stdout.write("\rDoing %x" % x + " of " + hex(int(tries)))
        sys.stdout.flush()

        log = open("pi-log.txt", "a")
        log.write(str(pi) + "\n")
        log.close()

        impo = open("pi-file.txt", "w")
        impo.write("ins=" + str(ins) + "\n")
        impo.write("tot=" + str(tot))
        impo.close()


def plotPi():
    logImp = open("pi-log.txt", "r")

    line = []

    i_arr = []
    i=0
    while line != None:
        try:
            line.append(float(logImp.readline()[:-2]))
            i_arr.append(i)
        except ValueError:
            print("Exception")
            break
        
        i = i + 1

    plt.plot(i_arr, line)

    pi = []
    co_pi = []
    for i in range(0,len(i_arr)):
        pi.append(3.1415926)
        co_pi.append(i)

    plt.plot(co_pi,pi)
    plt.axis([0,len(line),max(line),min(line)])


    logImp.close()
    plt.show()

def resetPi():
    impo = open("pi-file.txt", "w")
    impo.write("ins=0\n")
    impo.write("tot=0")
    impo.close()

    log = open("pi-log.txt", "w")
    log.write("")
    log.close()

    print("Data has been deleted")


def average():
    log = open("pi-log.txt", "r")
    
    line = []

    while line != None:
        try:
            line.append(float(log.readline()[:-2]))
        except ValueError:
            print("End of Average")
            break

    log.close()

    lineLen = len(line)
    lineTot = 0
    for i in range(0,lineLen):
        lineTot = lineTot + line[i]

    lineAverage = lineTot/lineLen

    print(lineAverage)

def last():
    log = open("pi-log.txt", "r")
    
    line = 0

    while line != None:
        try:
            line = float(log.readline()[:-2])
        except ValueError:
            print("End of Last")
            break

    log.close()
    print(line)


while True:

    print("\nChoose one of the processes: Calculation(c), Plot(p), Reset(r), Log-Average(a), Last(l)")
    inp = input("->").lower()

    if inp == "c":
        print("How many tries?")
        tries = input("->")

        calculation(tries)

    elif inp == "p":
        plotPi()

    elif inp == "r":
        resetPi()

    elif inp == "a":
        average()

    elif inp == "l":
        last()

    else:
        print("Something is wrong please try again.")
