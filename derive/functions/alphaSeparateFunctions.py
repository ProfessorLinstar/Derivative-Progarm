class Separate:
    def sepByAdd(inputSeparate,parenthesesOrder):   
        separatedByAddition = [[""],[]]
        numOfGroups=len(parenthesesOrder[1])
        separatedCounter = 0
        for i in range(len(inputSeparate)):
            if inputSeparate[i] in"+-":
                for j in range(numOfGroups):
                    if parenthesesOrder[1][j]==0:
                        if parenthesesOrder[0][j][0]<i and i<parenthesesOrder[0][j][1]:
                            separatedByAddition[0][separatedCounter]+=inputSeparate[i]
                            break
                        elif j==numOfGroups-1:
                            separatedByAddition[0].append("")
                            separatedCounter+=1
                            separatedByAddition[1].append(inputSeparate[i])
            else:
                separatedByAddition[0][separatedCounter]+=inputSeparate[i]
        return separatedByAddition
    def sepByOp(inputSBP, parenthesesOrder):
        separatedByOperation = [[""],[]]
        numOfGroups=len(parenthesesOrder[1])
        separatedCounter = 0
        for i in range(len(inputSBP)):
            if inputSBP[i] in"*/^":
                for j in range(numOfGroups):
                    if parenthesesOrder[1][j]==0:
                        if parenthesesOrder[0][j][0]<i and i<parenthesesOrder[0][j][1]:
                            separatedByOperation[0][separatedCounter]+=inputSBP[i]
                            break
                        elif j==numOfGroups-1:
                            separatedByOperation[0].append("")
                            separatedCounter+=1
                            separatedByOperation[1].append(inputSBP[i])
            else:
                separatedByOperation[0][separatedCounter]+=inputSBP[i]
        return separatedByOperation
