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
            
    expected_value = repeat * probability
    
    print("-------------------------------------------------------------")
    print(f"In {repeat} days we get {expected_value} days for {probability*100}% desire output")
    print("-------------------------------------------------------------")
    print(f"your average number of successes is {expected_value} in {repeat} trials if you repeat the trials many times.")
    print("-------------------------------------------------------------")
            
    plt.bar(ge.keys(),ge.values())
    plt.show()
    return [list(gender),ge, expected_value]
