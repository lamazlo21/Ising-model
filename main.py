import numpy as np
import random as rand
import math
import matplotlib.pyplot

class Ising:



    def setLattice(self,size):
        return np.random.choice([-1, 1], size=(size, size))

    def metropolis(self, size, lattice, x, y, temp):
        time = 0
        for i in range(10000):
            for j in range(1000):
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
                    p = math.exp(-1*deltaE/1*temp)
                    r = np.random.uniform(0,1)

                    if r<p:
                        lattice[row][column] = lattice[row][column] * (-1)

            sum = 0;

            for j in range(size):
                for k in range(size):
                    sum = sum + lattice[j][k]


            m = (1/(size*size))*sum
            x.append(m)
            y.append(time)
            time = time+1











ising = Ising
x = []
y = []
lattice = ising.setLattice(ising,100)
ising.metropolis(ising, 100, lattice, x, y, 3.5)
#print(x)
#print(y)
matplotlib.pyplot.scatter(y,x, label='a')
matplotlib.pyplot.xlabel('t[MCS]')
matplotlib.pyplot.ylabel('m')
matplotlib.pyplot.show()