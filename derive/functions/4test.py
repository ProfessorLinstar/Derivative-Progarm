from parenthesesFunctions import *
from separateFunctions import *
string="3+2"
pI=ParInfo(string)
print("sep",Separate.sepByAdd(string,pI.parOrder))
