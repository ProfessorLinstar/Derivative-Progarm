class Separate:
    def sepByAdd(inpSep,parOrder):   
        sep = [""]
        numOfGroups=len(parOrder[1])
        sepCounter = 0
        if len(inpSep)==1:
            return inpSep
        par0List=[]
        for i in range(numOfGroups):
            if parOrder[1][i]==0:
                par0List.append(parOrder[0][i])
        numOfGroups=len(par0List)
        if inpSep[0]=="-":
            sep=["-",""]
            sepCounter+=1
        else:
            sep=[inpSep[0]]
        for i in range(1,len(inpSep)):
            if inpSep[i] in"+-":
                if numOfGroups!=0:
                    for j in range(numOfGroups):
                        if par0List[j][0]<i and i<par0List[j][1]:
                            sep[sepCounter]+=inpSep[i]
                            break
                        elif j==numOfGroups-1:
                            sep.extend([inpSep[i],""])
                            sepCounter+=2
                else:
                    sep.extend([inpSep[i],""])
                    sepCounter+=2
                    
            else:
                sep[sepCounter]+=inpSep[i]
        #print("par0list",par0List)
        #if sepCounter==0:
            #return sep[0]
        #else:
            #return sep
        return sep
    def sepByOp(inpSep, parOrder):
        sep = [""]
        numOfGroups=len(parOrder[1])
        sepCounter = 0
        if len(inpSep)==1:
            return inpSep
        par0List=[]
        for i in range(numOfGroups):
            if parOrder[1][i]==0:
                par0List.append(parOrder[0][i])
        numOfGroups=len(par0List)
        if inpSep[0] in "NCSdvt":
            sep=[inpSep[0],""]
            sepCounter+=1
        else:
            sep=[inpSep[0]]
        for i in range(1,len(inpSep)):
            if inpSep[i] in"/*^NSCdvt":
                if numOfGroups!=0:
                    for j in range(numOfGroups):
                        if par0List[j][0]<i and i<par0List[j][1]:
                            sep[sepCounter]+=inpSep[i]
                            break
                        elif j==numOfGroups-1:
                            sep.extend([inpSep[i],""])
                            sepCounter+=2
                else:
                    sep.extend([inpSep[i],""])
                    sepCounter+=2
                    
            else:
                sep[sepCounter]+=inpSep[i]
        #print("par0list",par0List)
        #if sepCounter==0:
            #return sep[0]
        #else:
            #return sep
        return sep
