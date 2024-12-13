import random
from matplotlib import pyplot

def crossover(parent1, parent2):
    #1-point crossover
    #if Pc combination is high enough, crossover
    if parent1[3]*parent2[3] >= random.uniform(0, 1):
        #exchange tails
        tempY = parent1[1];
        parent1[1] = parent2[1]
        parent2[1] = tempY

    return parent1, parent2

def z(p):

    x = (int(p[0], 2) -1)/1000 - 5
    y = (int(p[1], 2) -1)/1000 - 5
    zscore = (4-2.1*pow(x,2)+pow(x,4)/3.0)*pow(x,2)+x*y+(-4+4*pow(y,2))*pow(y,2)

    return zscore

def mutation(p):
    #probability of bit flip is average of 1/population and 1/chromosomelength
    Pm = 1/5
    flip = 0
    for i in range(2):
        for c in p[i]:
            flip = random.uniform(0, 1)
            if flip <= Pm:
                if c == '0':
                    c == '1';
                elif c == '1':
                    c == '0'
    return p

def takeZ(elem):
    return elem[2]

def takeF(elem):
    return elem[3]

def fitness(p, ztotal):
    Pc = 1 - p[2]/(2*ztotal)
    return Pc


def SGA():
    generations = 2000000
    population = 10

    #[x, y, z, Pc]
    p0 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p1 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p2 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p3 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p4 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p5 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p6 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p7 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p8 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    p9 = ['{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), '{0:14b}'.format(int((random.uniform(-5, 5)+5)*1000+1)), 1, 1]
    parents = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]
    best = p0
    Zavg = []
    Favg = []
    bests = []
    for j in range(generations):
        sumF = 0
        sumZ = 0
        for i in range(population):
            i_next = i+1
            if i_next > 9:
                i_next = 0;
            parents[i], parents[i_next] = crossover(parents[i], parents[i_next])
        #apply mutations and get z value for each child
        for k in range(population):
            parents[k] = mutation(parents[k])
            parents[k][2] = z(parents[k])
            sumZ += parents[k][2]
        Zavg.append(sumZ/10)
        parents.sort(key = takeZ)
        #fitness and assign Pcs
        for m in range(population):
            x = (int(parents[m][0], 2) -1)/1000 - 5
            y = (int(parents[m][1], 2) -1)/1000 - 5
            if (x<-5 or x>5) or (y<-5 or y>5):
                parents[m][3] = 0
                m += 1
                continue
            parents[m][3] = fitness(parents[m], sumZ)
            sumF += parents[m][3]
        Favg.append(sumF/10)
        parents.sort(key = takeF, reverse = True)
        #update best solution
        bests.append(parents[0][2])
        if parents[0][2] < best[2]:
            best = parents[0]
            

    return best, bests, Zavg

def main():
    solution, bestFitness, FitnessAvg = SGA()
    x = (int(solution[0], 2) -1)/1000 - 5
    y = (int(solution[1], 2) -1)/1000 - 5
    z = solution[2]
    print("x:", x, "y:", y, "z:", z)

    
    pyplot.figure(1)

    pyplot.plot(bestFitness)
    pyplot.xlabel("Generation")
    pyplot.ylabel('Best Individual Fitness')

    pyplot.figure(2)
    pyplot.plot(FitnessAvg)
    pyplot.xlabel("Generation")
    pyplot.ylabel('Average Population Fitness')

    pyplot.show()

if __name__ == "__main__":
    main()