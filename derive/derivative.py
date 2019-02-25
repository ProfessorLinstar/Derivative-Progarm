def derive(inputFunction,derVar):
    from functions.callFunctions import Calls
    from functions.separateFunctions import Separate
    from functions.parenthesesFunctions import ParInfo
    from functions.storeFunctions import Store
    commands="*/^NSCTdvt"
    #Separate by +'s outside of largest parentheses
    dvOngoing = True
    deriving = [inputFunction]
    underStat = [True]
    counter=[0]
    #count=Calls.setCounter(deriving)
    #deriving=Store.callStore(deriving,Separate.sepByAdd(deriving,parenthesesOrder),count)
    dvRun=0#run twice for testing
    while dvOngoing:
        #print("\n\nRound",str(dvRun)+"!\n\n")
        dvRun+=1
        #debugging:
            #print("counter:",counter)
            #print("deriving:",deriving,"moved counter:",counter)

        #Order of operations for derivation: check for multiplication / division first 
        #syntax: Separate.sepByAdd(inputSeparate,parenthesesOrder)    
        counter=Calls.setCounter(deriving)
        repeat=True
        #separating via add
        while counter!=[]:
            #print("counter:",counter,"underStat:",underStat,"\n\n")
            if Calls.call(underStat,counter):
                result=Calls.call(deriving,counter)
                repeat=True
                while repeat:
                    repeat=False
                    pI=ParInfo(result)
                    toBeStored=Separate.sepByAdd(result,pI.parOrder)
                    #print("tobeStoredcomplete",toBeStored)
                    i=0
                    #removing derivatives of 0
                    while i<len(toBeStored):
                        #print("\ni:",i,"toBeStored:",toBeStored,"range:",range(len(toBeStored)))
                        if toBeStored[i] not in "+-" and derVar not in toBeStored[i]:
                            #print("deleting:",toBeStored[i])
                            del toBeStored[i]
                            if len(toBeStored)!=0:
                                if i!=0:
                                    #print("deleting plus")
                                    del toBeStored[i-1]
                                elif toBeStored[i]=="+":
                                    del toBeStored[i]
                        else:
                            i+=1
                    #print("toBeStored parentheses check:",toBeStored)
                    #removing extraneous parentheses; ePCR extraneous Parentheses Check Result
                    for i in range(len(toBeStored)):
                        ePCR=toBeStored[i]
                        #print("ePCR",ePCR)
                        if ePCR[0]=="(" and ePCR[-1]==")":
                            pIC=ParInfo(ePCR)
                            #print("parOrder:",pIC.parOrder)
                            if pIC.parOrder[0][0][1]==len(ePCR)-1:
                                toBeStored[i]=ePCR[1:-1]
                                #print("repeating; toBeStored",toBeStored[i])
                                repeat=True
                    if repeat:
                        result="".join(toBeStored)
                        #print("result",result)
                #print("toBeStored final:",toBeStored)
                deriving=Store.callStore(deriving,toBeStored,counter)
                truthList=[]
                for i in toBeStored:
                    if i in "+-":
                        truthList.append(False)
                    else:
                        truthList.append(True)
                underStat=Store.callStore(underStat,truthList,counter)
                #print("derivin,",deriving,"truth,",truthList)
            Calls.moveCounter(deriving,counter)
        #break
        #checking what needs to be derived
        #counter=Calls.setCounter(deriving)
    #    while counter!=[]:
    #        if Calls.call(underStat,counter) and derVar not in Calls.call(deriving,counter):
    #            underStat=Store.callStore(underStat,False,counter)
    #        Calls.moveCounter(deriving,counter)
         
        #separating via operation
        #print("deriving,",deriving,"underStat:",underStat,"counter:",counter)
        
        counter=Calls.setCounter(deriving)
        while counter!=[]:
            if Calls.call(underStat,counter):#index error almost always means inconsistent underStat and deriving
                result=Calls.call(deriving,counter)
                pI=ParInfo(result)
                toBeStored=Separate.sepByOp(result,pI.parOrder)
                found=False
                #print("\nsepbyop tobeStored initial:",toBeStored)
                #/begin groupAif toBeStored[0] not in "+-*/^":#maybe not necessary? and toBeStored not in [["N"]]:
                #if len(toBeStored)>1 or len(toBeStored[0])>1 or derVar in toBeStored[0]:
                for i in commands:
                    bResult=""
                    aResult=""
                    for j in toBeStored:
                        if found:
                            aResult+=j
                            #print("aResult:",aResult)
                        if i==j:
                            found=True
                        elif not found:
                            bResult+=j
                    if found:
                        #print("[bResult,i,aResult]",[bResult,i,aResult])
                        #print("deriving before:",deriving)
                        if i not in "NSCdvt":
                            deriving=Store.callStore(deriving,[bResult,i,aResult],counter)
                            underStat=Store.callStore(underStat,[derVar in bResult,True,derVar in aResult],counter)
                        else:
                            deriving=Store.callStore(deriving,[i,aResult],counter)
                            underStat=Store.callStore(underStat,[True, derVar in aResult],counter)
                        #print("deriving:",deriving)
                        break
                if not found:
                    toBeStored=toBeStored[0].replace(derVar,"")
                    if toBeStored=="":
                        toBeStored="1"
                    elif "e" not in toBeStored and "p" not in toBeStored:
                        toBeStored=str(float(toBeStored))
                    deriving=Store.callStore(deriving,toBeStored,counter)
                    underStat=Store.callStore(underStat,False,counter)
                #/end groupA
            Calls.moveCounter(deriving,counter)
        #break
        
        #actually deriving finally for the love of god
        #print("\ninput understat for derivation:",underStat,"\n")
        counter=Calls.setCounter(deriving)
        while counter!=[]:
            result=Calls.call(deriving,counter)
            if Calls.call(underStat,counter) and result in commands:#index error almost always means inconsistent underStat and deriving
                aCount=counter[:]
                aCount[-1]+=1
                bCount=counter[:]
                bCount[-1]-=1
                aStat=Calls.call(underStat,aCount)
                aResult=Calls.call(deriving,aCount)
                bStat=Calls.call(underStat,bCount)
                bResult=Calls.call(deriving,bCount)
                underStat=Store.callStore(underStat,False,counter)
                #print("\ncounter:",counter,"bCount:",bCount,"aCount:",aCount,"result",result)
                #print("result is ",result)
                if result=="*":
                    if aStat and bStat:
                        del counter[-1]
                        #print("multiplication rule")
                        deriving=Store.callStore(deriving,["((",[aResult],")*"+bResult+"+(",[bResult],")*"+aResult+")"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False,[True],False],counter)
                        #print("deriving after change",deriving,"\n")
                elif result=="/":
                    if aStat and bStat:
                        del counter[-1]
                        #print("division rule")
                        deriving=Store.callStore(deriving,["((",[bResult],")/("+aResult+")-(",[aResult],")*("+bResult+")/("+aResult+")^2)"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False,[True],False],counter)
                    elif aStat:
                        #print("counter before",counter)
                        del counter[-1]
                        #print("Counter after:",counter)
                        deriving=Store.callStore(deriving,["(-(",[aResult],")("+bResult+")/("+aResult+")^2)"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                    #print("deriving after change",deriving,"\n")
                elif result=="^":
                    if aStat and bStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(("+bResult+")^("+aResult+")*(N("+bResult+")(",[aResult],")+("+aResult+")/("+bResult+")",[bResult],"))"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False,[True],False],counter)
                    elif aStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(("+bResult+")^("+aResult+")*N("+bResult+")*(",[aResult],"))"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                    elif bStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(("+aResult+")*("+bResult+")^("+aResult+"-1)*(",[bResult],"))"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                elif result=="N":
                    if aStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(",[aResult],")/"+aResult],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                elif result=="S":
                    if aStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["C"+aResult+"*(",[aResult],")"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                elif result=="C":
                    if aStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(-S"+aResult+")*(",[aResult],")"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                elif result=="d":
                    if aStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(",[aResult],")/\u221a(1-"+aResult+"^2)"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                elif result=="v":
                    if aStat:
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(-(",[aResult],")/\u221a(1-"+aResult+"^2))"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
                elif result=="t":
                    if aStat:
                        del counter[-1]
                        del counter[-1]
                        deriving=Store.callStore(deriving,["(",[aResult],")/(1+"+aResult+"^2)"],counter)
                        underStat=Store.callStore(underStat,[False,[True],False],counter)
            Calls.moveCounter(deriving,counter)
        counter=Calls.setCounter(deriving)
        dvOngoing=False
        while counter!=[]:
            if Calls.call(underStat,counter):
                dvOngoing=True
                break
            Calls.moveCounter(underStat,counter)
        #print("\n\nRound derived:")
        derived=""
        counter=Calls.setCounter(deriving)
        while True:
            try:
                derived+=Calls.movingCall(deriving,counter)
            except TypeError:
                break
        #print(derived)
        #print("\n\nderiving,",deriving)
        #print("\nderive truth list:",underStat)
    #print("\n\n\n\nFinal derived:")
    if derived=="": derived="0"
    return derived










