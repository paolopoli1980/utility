import random

ngames=50000
point=0
for i in range(ngames):

    doors=[0,0,0]
    door=random.randint(0,2)
    #print (door)

    doors[door]=1

    choice=random.randint(0,2)
    
    if doors[choice]==1:
        point+=1
        

print(point/ngames)
point=0
for i in range(ngames):

    doors=[0,0,0]
    door=random.randint(0,2)
    #print (door)

    doors[door]=1

    choice=random.randint(0,2)
    memchoice=choice
    for j in range(3):
        #print(j)
        if doors[j]==0 and j!=choice:
            memj=j
            
    #print (doors)
    while choice==memj or choice==memchoice:        
        choice=random.randint(0,2)
            
    if doors[choice]==1:
        point+=1
        

print(point/ngames)
