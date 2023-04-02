from time import *
start = time()
from pyamaze import *
from random import *
from operator import *

popsize=400
colomn=30
rows=20
m = maze(rows,colomn)
# m.CreateMaze(loadMaze="maze--2023-04-02--16-24-59.csv")
m.CreateMaze(saveMaze=True, loopPercent=100)
aa = agent(m, footprints=True, shape='arrow')
# m.run()
sweight = 1
tweight = 2
whweight = 3
minstep=[1]
maxstep=[1]
minturn=[1]
maxturn=[1]
minwronghouses=[1]
maxwronghouses=[1]

def popfiller():
    b=[]
    for i in range(popsize): 
        a=[(randint(1,rows),i) for i in range(1,colomn)]
        a.pop(0)
        a.insert(0,(1,1))
        t=(rows,colomn)
        a.append(t)
        a.reverse()
        c = randint(0,1)
        a.insert(0,c)
        b.append(a)
    return b

def chatgptmadethisforme(a):
    step=[]
    turn=[]
    wronghouse=[]
    
    s=[]
    minstep[0]=99999
    maxstep[0]=0
    minturn[0]=99999
    maxturn[0]=0
    minwronghouses[0]=9999
    maxwronghouses[0]=0
    
    for i in range(popsize):
        z=[]
        steps = 0
        turns = 0
        wronghouses=0
        if a[i][0] == 1:
            
            a[i].pop(0)

            for j in range(colomn-1):


                if a[i][j][0] < a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1])]["S"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1])]["W"] == 0:
                                wronghouses+=1

                            # print(steps)
                        # print(x,a[i][j][1])
                        w=(x,a[i][j][1])
                        z.append(w)

                if a[i][j][0] > a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]-1,-1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1])]["N"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1])]["W"] == 0:
                                wronghouses+=1
                        #     # print(steps)
                        # print(x,a[i][j][1])
                        w=(x,a[i][j][1])
                        z.append(w)

                if a[i][j][0] == a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if m.maze_map[(x,a[i][j][1])]["W"] == 0:
                                wronghouses+=1
                            # print(steps)
                        # print(x,a[i][j][1])
                        w=(x,a[i][j][1])
                        z.append(w)

                if a[i][j][0] != a[i][j+1][0]:
                    turns+=1
            

            if minstep[0] > steps:
                minstep[0] = steps
            if maxstep[0] < steps:
                maxstep[0] = steps
            if minturn[0] > turns:
                minturn[0] = turns
            if maxturn[0] < turns:
                maxturn[0] = turns
            if minwronghouses[0] > wronghouses:
                minwronghouses[0] = wronghouses
            if maxwronghouses[0] < wronghouses:
                maxwronghouses[0] = wronghouses





            w=(1,1)
            z.append(w)
            s.append(list(z))
            a[i].insert(0,1)
            a[i].insert(0,turns)
            a[i].insert(0,steps)
            a[i].insert(0,wronghouses)


            continue

            

            


            # print("Steps:",steps)
            # print("turns",turns)
            # print("wronghouses:", wronghouses)

        
        if a[i][0] == 0:
            

            steps = 0
            turns = 0
            wronghouses=0
            a[i].pop(0)
            for j in range(colomn-1):



                if a[i][j][0] < a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1]-1)]["S"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1]-1)]["W"] == 0:
                                wronghouses+=1

                            # print(steps)
                        # print(x,a[i][j][1]-1)
                        w=(x,a[i][j][1]-1)
                        z.append(w)

                if a[i][j][0] > a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]-1,-1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1]-1)]["N"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1]-1)]["W"] == 0:
                                wronghouses+=1
                        #     # print(steps)
                        # print(x,a[i][j][1]-1)
                        w=(x,a[i][j][1]-1)
                        z.append(w)

                if a[i][j][0] == a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if m.maze_map[(x,a[i][j][1]-1)]["W"] == 0:
                                wronghouses+=1
                            # print(steps)
                        # print(x,a[i][j][1]-1)
                        w=(x,a[i][j][1]-1)
                        z.append(w)

                if a[i][j][0] != a[i][j+1][0]:
                    turns+=1



            wronghouses -=1





            if m.maze_map[(a[i][0])]["W"] == 0:
                wronghouses+=1







            if minstep[0] > steps:
                minstep[0] = steps
            if maxstep[0] < steps:
                maxstep[0] = steps
            if minturn[0] > turns:
                minturn[0] = turns
            if maxturn[0] < turns:
                maxturn[0] = turns
            if minwronghouses[0] > wronghouses:
                minwronghouses[0] = wronghouses
            if maxwronghouses[0] < wronghouses:
                maxwronghouses[0] = wronghouses

        
            
            w=(rows,colomn)
            z.insert(0,w)
            s.append(list(z))
            a[i].insert(0,0)
            a[i].insert(0,turns)
            a[i].insert(0,steps)
            a[i].insert(0,wronghouses)

            # print("Steps:",steps)
            # print("turns",turns)
            # print("wronghouses:", wronghouses)
        
    # print(s)
    # print("\n")
    # print("\n")
    return s


    
    
def fitnesschecker69(a):
    
    for i in range(popsize):
        if maxturn[0]==minturn[0]:
            maxturn[0]+=1
        if maxstep[0]==minstep[0]:
            maxstep[0]+=1
        if maxwronghouses[0]==minwronghouses[0]:
            maxwronghouses[0]+=1
        sfit = 1 - ((a[i][1]-minstep[0])/ (maxstep[0]-minstep[0]))
        tfit = 1 - ((a[i][2]-minturn[0])/ (maxturn[0]-minturn[0]))
        whfit = 1 - ((a[i][0]-minwronghouses[0])/ (maxwronghouses[0]-minwronghouses[0]))

        fit= (100 * whweight * whfit) * ((sweight * sfit) + (tweight * tfit)) / (sweight + tweight)

        a[i].insert(0,fit)
    
    
    
    
    
    
    
    
    
    
    
    
    # a= sorted(a,key=itemgetter(2))

    # print("\n")
    # print("\n")
    # print("\n")
    # print("\n")
    # print(a)

    # a= sorted(a,key=itemgetter(1))
    # print("\n")
    # print("\n")
    # print("\n")
    # print("\n")
    # print(a)

    a= sorted(a,reverse=True,key=itemgetter(0))

    # print("\n")
    # print("\n")
    # print("\n")
    # print("\n")
    # print(a)
    for i in range(popsize):
        a[i].pop(0)
        a[i].pop(0)
        a[i].pop(0)
        a[i].pop(0)
        


    # print("\n")
    # print("\n")
    # print("\n")
    # print("\n")
    # print(a)


def listadder(a):
    g=[]
    for i in range(popsize):
        g.append(a[i][0])
        a[i].pop(0)
    return a,g

def listrefurbisher(a,g):
    for i in range(popsize):
        a[i].insert(0,g[i])
    return a
    
def crosscross(a):
    a, g = listadder(a)
    for i in range(int(popsize/2)):
        a[int(popsize/2) + i] = a[i][0:int(colomn/2)] + a[i+1][int(colomn/2):colomn]
    a = listrefurbisher(a,g)
    # for i in range(int(popsize/2), popsize):
    #     a[i].pop(0)
    #     c=randint(0,1)
    #     a[i].insert(0,c)


def mutate(a):
    a, g = listadder(a)
    for i in range(popsize):
        x=randint(1,colomn-2)
        a[i][x] = (randint(1,rows-1),colomn-x)
    a = listrefurbisher(a,g)
    # print("\n")
    # print("\n")
    # print("\n")
    # print("\n")
    # print(a)

def printthemfer(a):
    for i in range(popsize):
        print(a[i])
    print("\n")
    print("\n")
    print("\n")


























def ultimateanswer(a):
    step=[]
    turn=[]
    wronghouse=[]
    
    s=[]
    minstep[0]=99999
    maxstep[0]=0
    minturn[0]=99999
    maxturn[0]=0
    minwronghouses[0]=9999
    maxwronghouses[0]=0
    
    for i in range(1):
        a[i].pop(0)
        a[i].pop(0)
        a[i].pop(0)

        z=[]
        steps = 0
        turns = 0
        wronghouses=0
        if a[i][0] == 1:
            
            a[i].pop(0)

            for j in range(colomn-1):


                if a[i][j][0] < a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1])]["S"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1])]["W"] == 0:
                                wronghouses+=1

                            # print(steps)
                        # print(x,a[i][j][1])
                        w=(x,a[i][j][1])
                        z.append(w)

                if a[i][j][0] > a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]-1,-1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1])]["N"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1])]["W"] == 0:
                                wronghouses+=1
                        #     # print(steps)
                        # print(x,a[i][j][1])
                        w=(x,a[i][j][1])
                        z.append(w)

                if a[i][j][0] == a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if m.maze_map[(x,a[i][j][1])]["W"] == 0:
                                wronghouses+=1
                            # print(steps)
                        # print(x,a[i][j][1])
                        w=(x,a[i][j][1])
                        z.append(w)

                if a[i][j][0] != a[i][j+1][0]:
                    turns+=1
            

            if minstep[0] > steps:
                minstep[0] = steps
            if maxstep[0] < steps:
                maxstep[0] = steps
            if minturn[0] > turns:
                minturn[0] = turns
            if maxturn[0] < turns:
                maxturn[0] = turns
            if minwronghouses[0] > wronghouses:
                minwronghouses[0] = wronghouses
            if maxwronghouses[0] < wronghouses:
                maxwronghouses[0] = wronghouses





            w=(1,1)
            z.append(w)
            s.append(list(z))
            a[i].insert(0,1)
            a[i].insert(0,turns)
            a[i].insert(0,steps)
            a[i].insert(0,wronghouses)


            continue

            

            


            # print("Steps:",steps)
            # print("turns",turns)
            # print("wronghouses:", wronghouses)

        
        if a[i][0] == 0:
            

            steps = 0
            turns = 0
            wronghouses=0
            a[i].pop(0)
            for j in range(colomn-1):



                if a[i][j][0] < a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1]-1)]["S"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1]-1)]["W"] == 0:
                                wronghouses+=1

                            # print(steps)
                        # print(x,a[i][j][1]-1)
                        w=(x,a[i][j][1]-1)
                        z.append(w)

                if a[i][j][0] > a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]-1,-1):
                        steps+=1
                        if x != a[i][j+1][0]:
                            if m.maze_map[(x,a[i][j][1]-1)]["N"] == 0:
                                wronghouses+=1
                        else:
                            if m.maze_map[(x,a[i][j][1]-1)]["W"] == 0:
                                wronghouses+=1
                        #     # print(steps)
                        # print(x,a[i][j][1]-1)
                        w=(x,a[i][j][1]-1)
                        z.append(w)

                if a[i][j][0] == a[i][j+1][0]:
                    for x in range(a[i][j][0],a[i][j+1][0]+1):
                        steps+=1
                        if m.maze_map[(x,a[i][j][1]-1)]["W"] == 0:
                                wronghouses+=1
                            # print(steps)
                        # print(x,a[i][j][1]-1)
                        w=(x,a[i][j][1]-1)
                        z.append(w)

                if a[i][j][0] != a[i][j+1][0]:
                    turns+=1



            wronghouses -=1

            # if m.maze_map[(a[i][-1])]["W"] == 0:
            #     wronghouses+=1



            if minstep[0] > steps:
                minstep[0] = steps
            if maxstep[0] < steps:
                maxstep[0] = steps
            if minturn[0] > turns:
                minturn[0] = turns
            if maxturn[0] < turns:
                maxturn[0] = turns
            if minwronghouses[0] > wronghouses:
                minwronghouses[0] = wronghouses
            if maxwronghouses[0] < wronghouses:
                maxwronghouses[0] = wronghouses

        
            
            w=(rows,colomn)
            z.insert(0,w)
            s.append(list(z))
            a[i].insert(0,0)
            a[i].insert(0,turns)
            a[i].insert(0,steps)
            a[i].insert(0,wronghouses)

            # print("Steps:",steps)
            # print("turns",turns)
            # print("wronghouses:", wronghouses)
        
    # print(s)
    # print("\n")
    # print("\n")
    return s




































fin = popfiller()
# print(fin)
# print(fin[0])
# w=paths(fin)
# # q=w[0]
# # print(q)
# # print("\n")
# # q=w[1]
# # print(q)
# # print("\n")
# # h=w[5]
# # print(h)
# # print("\n")
# # print("\n")
# # print("\n")
# # # print(w)
# # # m.tracePath({aa:})
# # print("\n")
# # print("\n")
# # print("\n")
# # print(fin[0])
# # print("\n")
# # print("\n")
# # print("\n")
# # print(fin, sep="\n")
# # print("\n")
# # print("\n")
# # print("\n")
# print("\n")
# fitnesschecker69(fin)
# print("\n")
# print("\n")
# print("\n")
# print("\n")


# printthemfer(fin)
# # print(fin[0])
# # print(fin[1])
# # print(fin[2])
# # print(fin[3])
# # print(fin[4])
# # print(fin[5])
# # print(fin[6])
# # print(fin[7])
# # print(fin[8])
# # print(fin[9])

# print("\n")
# print("\n")
# print("\n")
# print("\n")
# crosscross(fin)
# printthemfer(fin)
    
# # print(fin[0])
# # print(fin[1])
# # print(fin[2])
# # print(fin[3])
# # print(fin[4])
# # print(fin[5])
# # print(fin[6])
# # print(fin[7])
# # print(fin[8])
# # print(fin[9])
# mutate(fin)
# printthemfer(fin)








count=0
# count+=1
# print(count)
dope = False
hegs=True
herg=0

while dope == False:
    print("\n")
    count=0
    print("New Generation of party people")
    fin = popfiller()
    while count < 10000:
        w = chatgptmadethisforme(fin)
        fin = sorted(fin,key=itemgetter(0))
        if fin[0][0]==0:
            dope=True
            break
        print(fin[0][0])
        
        fitnesschecker69(fin)
        crosscross(fin)

        mutate(fin)
        count+=1
        # print(count)
        # printthemfer(fin)

printthemfer(fin)

# w = chatgptmadethisforme(fin)

fin = sorted(fin,key=itemgetter(0))


r = ultimateanswer(fin)
print(r[0])
print("\n")

print(w[0])
m.tracePath({aa:r[0]})

end = time()
print((end-start) * 10**3, 'ms')
print(count)

# printthemfer(fin)
print(w[0])
m.run()