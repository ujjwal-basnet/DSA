
# basisc hash function 
# note that in real world hash fucntion are more complicated than these  ,
##mod function 
def mod(number , cellnumber ):
    return number  % cellnumber 


list = 24*[None]
mod(400 , 24)
print(mod(400 , 24))

# AsCII Function 
def modASCII(string , cellNumber):
    total = 0 
    for i in string :
        total += ord(i)
    return total % cellNumber

print("\n This is for ModASCII , String " , modASCII('ujjwal' , 28))