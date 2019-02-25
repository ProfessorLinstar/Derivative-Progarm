class ParInfo:
    def __init__(self,inputFunction):
        #look for stuff in order of operations
        length=len(inputFunction)
        parenthesesPlacement=[[],[]]#first list = placement of any parenthis; second list = type of parenthis; third list = placement of paired parenthis
        for i in range(length):
            if inputFunction[i] == "(":
                parenthesesPlacement[0].append(i)
                parenthesesPlacement[1].append(1)
            if inputFunction[i]==")":
                parenthesesPlacement[0].append(i)
                parenthesesPlacement[1].append(-1)
        parenthesesOrder=[[],[]]#first list = pairs of parentheses; second list = priority (0=largest parentheses)
        numParentheses=len(parenthesesPlacement[0])
        listy=[[],[]]
        construction=[[],[]]
        for i in range(len(parenthesesPlacement)):
            for j in parenthesesPlacement[i]:
                construction[i].append(j)
        self.parPlace=construction
        #print("parenthesesPlacement:",parenthesesPlacement)
        check=True
        i=0
        while i != numParentheses:
            if parenthesesPlacement[1][i]==1:
                listy[0].append(parenthesesPlacement[0][i])
                if len(listy[0])==1:
                    firstBound=i
                    check=False
            elif parenthesesPlacement[1][i]==-1:
                listy[1].append(parenthesesPlacement[0][i])
            if len(listy[0])==len(listy[1]) and len(listy[0])!=0:
                parenthesesOrder[1].append(0)
                parenthesesOrder[0].append([listy[0][0],listy[1][-1]])
                for j in parenthesesOrder[0]:
                    if j[0]<listy[0][0] and listy[1][-1]<j[1]:
                        parenthesesOrder[1][-1]+=1
                parenthesesPlacement[1][firstBound]=0
                parenthesesPlacement[1][i]=0
                i=firstBound
                listy=[[],[]]
                check=True
            i+=1
        self.parOrder=parenthesesOrder
        if sum(self.parPlace[1])!=0:
            check=False
        self.parCheck=check
        #print("parenthesesPlacement:",parenthesesPlacement)
        #print("construction:",construction)
