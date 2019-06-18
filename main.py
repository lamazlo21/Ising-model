import numpy as np
import random as rand
import math
import matplotlib.pyplot

class Ising:



    def setLattice(self,size):
        return np.random.choice([-1, 1], size=(size, size))

    def metropolis(self, size, lattice, temp):
        time = 0
        avgArray = []
        for i in range(10000):
            for j in range(size*size):
                row = rand.randint(0,size-1)
                column = rand.randint(0,size-1)
                spin = lattice[row][column]

                if row-1 >=0:
                    bottom = lattice[row-1][column]
                else:
                    bottom = 0
                if row+1 <=9:
                   top = lattice[row+1][column]
                else:
                   top = 0
                if column-1 >=0:
                    left = lattice[row][column-1]
                else:
                    left = 0
                if column+1 <=9:
                    right = lattice[row][column+1]
                else:
                    right = 0

                deltaE = 2*spin*(top+bottom+left+right)
                if(deltaE < 0 ):
                    lattice[row][column] = lattice[row][column] * (-1)
                else:
                    p = math.exp((-1*deltaE)/(temp))
                    r = np.random.uniform(0,1)
                    if r<p:
                        lattice[row][column] = lattice[row][column] * (-1)


            sum = 0
            for j in range(size):
                for k in range(size):
                    sum = sum + lattice[j][k]


            m = (1/(size*size))*sum
            avgArray.append((m,time))
            time = time+1

        return avgArray



    def avgMagnetization(self, size):
        results = []
        i = 2.6
        while i<=3.5:
            sum = 0
            count = 0
            for j in range(5):
                fileName = 'Mag' + str(size) + 'L' + str(i).replace('.', '') + str(j) + '.txt'
                tempArray = self.readAvgFromFile(self, fileName)
                for k in range(100, len(tempArray), 1000):
                    sum = sum + abs(tempArray[k][0])
                    count = count + 1
            results.append(((sum/count), i))
            i = round(i + 0.1,3)
        return results

    def avgSpinToFile(self, array, fileName):
        file = open(fileName,"a+")
        for i in range(len(array)):
            file.write(str(array[i][0])+" "+str(array[i][1])+'\n')
        file.close()

    def readAvgFromFile(self, fileName):
        file = open(fileName, 'r')
        tempArray = []
        while True:
            line = file.readline()
            if line == "":
                break
            tempArray.append((float(line.split(' ')[0]),int(line.split(' ')[1])))
        file.close()
        return tempArray

ising = Ising
size = 40
temperature = 2.8
#code that compute avrage magnetization
for j in range(19):
    for i in range(5):
        fileName = 'Mag'+str(size)+'L'+str(temperature).replace('.','')+str(i)+'.txt'
        lattice = ising.setLattice(ising,size)
        avgSpinArray = ising.metropolis(ising, size, lattice, temperature)
        ising.avgSpinToFile(ising,avgSpinArray,fileName)
    temperature = round(temperature + 0.1,3)
#avgMagnetization = []
#ising.readAvgFromFile(ising,avgMagnetization,'Mag10L170.txt')
#ising.avgMagnetization(ising, x,y, avg,tempA)
#matplotlib.pyplot.scatter(y,x, label='a')
#matplotlib.pyplot.xlabel('t[MCS]')
#matplotlib.pyplot.ylabel('m')
#matplotlib.pyplot.title('Magnetyzacja L =' +str(size)+', T = '+str(temperature))
#matplotlib.pyplot.show()
#print(ising.avgMagnetization(ising, size))

#print(avg)
