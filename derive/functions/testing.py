from separateFunctions import *
from callFunctions import *
from parenthesesFunctions import *
#inputFunction="((3+2x)+((2+x)+((3x)^3)/2))+2y^x+(3+x^2)^3+y"
#inputFunction="(x^2+e)^(x^(-1+x)+2x)+(x^(x+e)-x^2)"
inputFunction="((())))("
parInfo=ParInfo(inputFunction)
print(inputFunction)
print("inputFunction:",inputFunction)
print("parenthesesOrder:",parInfo.parOrder,"\nparenthesesPlacement:",parInfo.parPlace)
print("\nchecK:",parInfo.parCheck)




#print("\nseparate by addition:",Separate.sepByAdd(inputFunction,parInfo.parOrder),"\nseparatebyOperation:",Separate.sepByOp(inputFunction,parInfo.parOrder))
