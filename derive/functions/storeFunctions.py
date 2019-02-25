class Store:
    def callStore(nestedList, store, inpCounter):
        counter=[0]
        i=nestedList
        inList=[["("],["("]]
        quit=False
        while not quit:
            repeat=True
            while repeat:
                repeat=False
                i=nestedList
                number=0
                while not quit and type(i)==list and counter!=inpCounter:
                    #print("i",i,"number",number,"full counter:",counter)
                    if len(counter)>number:
                        if len(i)>counter[number]:
                            i=i[counter[number]]
                            number+=1
                        else:
                            del counter[-1]
                            if len(counter)>0:
                                counter[-1]+=1
                                inList[0].append(")")
                                inList[1].append(")")
                                repeat=True
                                break
                            else:
                                repeat=False
                                quit=True
                    else:
                        inList[0].append("(")
                        inList[1].append("(")
                        counter.append(0)
            if len(counter)>0:
                #print("\n","i:",i,"\n")
                if counter==inpCounter:
                    inList[0].append(store)
                else:
                    inList[0].append(i)
                inList[1].append(len(counter))
                counter[-1]+=1
        inList[0].append(")")
        inList[1].append(")")
        generate=[]
        gLocate=[]
        gCount=0
        gInCount=0
        maxDepth=0
        for i in inList[1]:
            if type(i)==int:
                maxDepth=max(i,maxDepth)
        #print("inlist:",inList)

        for depth in range(maxDepth,0,-1):
            #print("\n\n\nDepth:",depth)
            gInCount=0
            gCount=0
            inOne=False
            newOne=True
            for checkCounter in range(len(inList[1])):
                #print("CC:",checkCounter,"gLoc:",gLocate,"gen:",generate,"gCount:",gCount,"GIC:",gInCount)
                if gCount<len(gLocate):
                    if inOne and checkCounter>gLocate[gCount][-1]+1:
                        gCount+=1
                        inOne=False
                    elif gLocate[gCount][0]<=checkCounter:
                        inOne=True
                if not newOne and type(inList[0][checkCounter])==str:
                    #for ginnercount; see when element ends
                    parNetSum+=1-2*int(inList[0][checkCounter]=="(")
                    if parNetSum==1:
                        newOne=True
                elif inList[1][checkCounter]==depth+1 and newOne:
                    #if there is an element in front of check, add one to ginnercount
                    newOne=False
                    parNetSum=0 #number of closing parentheses-number of open parentheses
                    gInCount+=1
                elif inList[1][checkCounter]==depth:#if check found an entry
                    if inOne:#if in existing list
                        generate[gCount].insert(gInCount,inList[0][checkCounter])
                        gLocate[gCount].insert(gInCount,checkCounter)
                        gInCount+=1
                    else:#if not in existing list; make new one
                        gInCount=0
                        generate.insert(gCount,[inList[0][checkCounter]])
                        gLocate.insert(gCount,[checkCounter])
                        inOne=True
                        gInCount+=1
            x=0
            #print("\nCombining generate")
            while x<len(gLocate)-1:
                #if there are no ")" between end of one list and start of next, combine lists
                #print("gLoc:",gLocate,"x:",x)
                for j in range(gLocate[x][-1],gLocate[x+1][0]):
                    if type(inList[1][j])==str:
                        break
                    elif j==gLocate[x+1][0]-1:
                        #combine lxsts for locate and gen
                        generate[x].extend(generate[x+1])
                        gLocate[x].extend(gLocate[x+1])
                        del generate[x+1]
                        del gLocate[x+1]
                        x-=1
                x+=1
            for i in range(len(generate)):#nest lists
                generate[i]=[generate[i]]
            #print("new generate:",generate)
            #print("\ninput inList[1]",inList[1])
            x=0
            for i in gLocate:
                x=i[0]-1
                while inList[1][x]==0:
                    x-=1
                #print("x:",x)
                inList[1][x]=0
                x=i[-1]+1
                while inList[1][x]==0:
                    x+=1
                inList[1][x]=0
            #print("output inList[1]:",inList[1])
        generate=generate[0][0]
        nestedList=generate
        return generate

