from itertools import product
from matplotlib import pyplot as plt 
import math

def Binomial(string,checkParam,probability, repeat):
    gender = [''.join(i) for i in product(string, repeat=repeat)]
    

    gendernuum = product([probability,1-probability], repeat=repeat)
    genderNumList = []
    for i in list(gendernuum):
        genderNumList.append(math.prod(i))
        
        
    ge={}

    for i,j in zip(list(gender), genderNumList):
        occur = i.count(checkParam)
        try:
            if(ge[occur]):
                ge[occur] += j
        except:
            ge.update(
                {
                    occur:j
                }
            )
            
    plt.bar(ge.keys(),ge.values())
    plt.show()
    return [list(gender),ge]

[a,c] = Binomial('GB', checkParam="B",probability=0.4,repeat=20)

print(c)