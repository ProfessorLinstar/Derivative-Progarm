from math import log,sin,cos,asin,acos,atan,e,pi
from derivative import *
from functions.parenthesesFunctions import *
def convert(inp,into): 
    for i in range(len(into[0])):
        inp=inp.replace(into[0][i],into[1][i])
    return inp
def insMult(inp):
    counter=0
    b=" "
    for i in inp:
        #print("inputfunction on iteration:",inp,"i:",i,"counter:",counter)
        a=i
        #print("a:",a,"b:",b)
        if (a=="(" and b ==")") or (a in "ep\u03c0xyz(" and b in "1234567890ep\u03c0xyz") or (a in "1234567890ep\u03c0xyz" and b in "ep\u03c0xyz)"):
            inp=inp[:counter]+"*"+inp[counter:]
            #print("inscounter:",counter)
            counter+=1
        b=i
        counter+=1
    return inp
print("Input function here. Use up to three variables in this order: x, y, and z in the form: \nType help for list of operations.\n")
badInput = True
#convert to single letter for derivation and then replace again for display
#skipthis nonsense
if False:#test this stuff sometime
    while badInput:
        badInput=False
        inpFunc = input("f= ")
        if inpFunc=="help":
            print("here's some help for you.")
            badInput=True
        else:
            try:
                float(eval(insMult(convert(inpFunc,[["^","x","y","z"," ","ln"],["**","(0)","(0)","(0)","","log"]]))))
            except KeyboardInterrupt:
                Raise
            except ZeroDivisionError:
                pass
            except ValueError:
                pass
            except Exception as x:
                badInput=True
                print("Error:",x)
    print("derivation variable:")
    while True:
        derVar = input()
        if derVar not in ["x","y","z"]:
            print("bad input")
        else:
            break
    print("Calculate at a point?(y/n)")
    yn=input()
    while len(yn)!=1 or yn not in "ynYN":
        yn=input("(y/n):")
    if yn in "yY":
        print("Input",derVar,"value:")
        varList,atAPoint=[],[]
        for i in "xyz":
            if i in inpFunc:
                varList.append(i)
                atAPoint.append(0)
        counter=0
        print("varList and atAPoint::",varList,atAPoint)
        while counter<len(varList):
            try:
                atAPoint[counter]=str(float(eval("("+input((varList)[counter]+":")+")")))
                counter+=1
            except KeyboardInterrupt:
                raise
            except:
                print("Bad Input. Try again.")
        print("atAPoint:",atAPoint,"varList:",varList)
    #exit()
else:
    #inpFunc="x^S(x)"
    #inpFunc="ln(x^2+2x)"
    #inpFunc="e+e*x+(C((x^2+ez))^2)^S(S((x^(yz+C(x+y))+2x)))+(x^(xy/z+e)-x^2)"
    inpFunc="(C((x)))^S(x^(yz+C(x+y)))"
    #inpFunc="x^S(x^2+2x)"
    #inpFunc="e^(-x+3)"
    #inpFunc="((e+1)+1)+((2^3)+3x)+((((x^x)*x)))+((e^x)*x+1)+(x+(3/x^2))+(2+x)"
    #inpFunc="3x+(x^x)*x+(e^x)*x+(x+(3/x^2))+(2+x)"
    #inpFunc="(x^2+e)^(x^(-1+x)+2x)+x"
    #inpFunc="(x^2+e)*(x)"
    #inpFunc="(x^x)*x"
    #inpFunc="N(x)"
    #inpFunc="x*x*x*x*x*x"
    #inpFunc="-x*x"
    #inpFunc="(1)(2)(3)N(x)x(y)z(x)+x(3)"
    #inpFunc="S(N(3x))"
    #inpFunc="S(3)"
    derVar="x"
    atAPoint=["1","3","10"]
    varList=["x","y","z"]
    yn="y"


oriFunc=convert(inpFunc,[["log","N","S","C","T","d","v","t","p","pi","**"],["log","ln","sin","cos","tan","asin","acos","atan","\u03c0","\u30c0","^"]])

#function friendly
inpFunc=convert(inpFunc,[["ln","log","sin","cos","tan","asin","acos","atan","pi","**"],"NNSCTdvtp^"])
inpFunc=insMult(inpFunc)

#/begin derivation
derived=derive(inpFunc,derVar)
#/end derivation


#presentation friendly
derived=convert(derived,["NSCTdvtp",["ln","sin","cos","tan","asin","acos","atan","\u03c0"]])




print("\ninput:",oriFunc)
print("\nfinal derived:",derived)
if yn in "yY":
    derivedPY=insMult(derived)
    derivedPY=convert(derivedPY,[["ln","^","\u03c0","e","\u221a"]+varList,["log","**","(pi)","(e)","sqrt"]+atAPoint])
    print("At "+str(varList),"=",str(atAPoint),"df/dx="+str(eval(derivedPY)))
    derivedCC=convert(derivedPY,[["**"],["^"]])
    print("\r\n\r\nCalculator friendly version:",derivedCC)
    print("\r\nPython friendly version:",derivedPY)


file=open("outputDerived.txt","w")
file.write("--Results of derivation--\r\n\r\noriFunc:"+oriFunc+"\r\nderived:"+derived)
if yn in "yY":
    file.write("\r\nAt "+str(varList)+"="+str(atAPoint)+" df/dx="+str(eval(derivedPY)))
    file.write("\r\n\r\nPython friendly version: "+derivedPY)
    file.write("\r\nCalculator friendly version: "+derivedCC)
file.close()
