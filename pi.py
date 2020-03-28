import numpy as np
import sys
import matplotlib.pyplot as plt

def calculation(tries):
    try:
        impo = open("pi-file.txt", "r")
        ins = int(impo.readline()[4:])
        tot = int(impo.readline()[4:])
        impo.close()
    except FileNotFoundError:
        print("Starting from new file")
        ins = 0
        tot = 0

    print("Starting with numbers: " + str(ins) + " and " + str(tot))

    # Creating arrays 
    psx = np.zeros(tries)
    psy = np.zeros(tries)

    # Filling arrays with random float-values
    for i in range(tries):
        psx[i] = np.random.random()
        psy[i] = np.random.random()

        # Checks if point is within circle
        if np.hypot(psx[i],psy[i]) <= 1:
            ins += 1
        tot += 1


        pi = (ins / tot) * 4
        sys.stdout.write("\rDoing %i" % i + " of " + str(tries))
        sys.stdout.flush()

        log = open("pi-log.txt", "a")
        log.write(str(pi) + "\n")
        log.close()

    impo = open("pi-file.txt", "w")
    impo.write("ins=" + str(ins) + "\n")
    impo.write("tot=" + str(tot))
    impo.close()


def plotPi():
    try:
        logImp = open("pi-log.txt", "r")

        line = []

        i_arr = []
        i=0
        while line != None:
            try:
                line.append(float(logImp.readline()[:-2]))
                i_arr.append(i)
            except ValueError:
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
    except FileNotFoundError:
        print("No file found.s")

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
    try:
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

    except FileNotFoundError:
        print("File not found.")

def last():
    try:
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

    except FileNotFoundError:
        print("File not found.")


while True:

    print("\nChoose one of the processes: Calculation(c), Plot(p), Reset(r), Log-Average(a), Last(l), Quit(q)")
    inp = input("->").lower()

    if inp == "c":
        print("How many tries?")
        tries = int(input("->"))

        calculation(tries)

    elif inp == "p":
        plotPi()

    elif inp == "r":
        resetPi()

    elif inp == "a":
        average()

    elif inp == "l":
        last()

    elif inp == "q":
        exit()

    else:
        print("Something is wrong please try again.")
