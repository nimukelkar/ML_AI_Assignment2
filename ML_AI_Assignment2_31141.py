import numpy as np
from numpy import genfromtxt
from scipy.stats import kurtosis,skew
from matplotlib import pyplot as plt
import math

def calmean(A):
    return(np.mean(A))

def calmoment(A,n):
    sum=0
    av=calmean(A)
    len = np.size(A)
    for i in range(len):
        sum+=(A[i]-av)**n
    return sum/len
def calskewness(A):
    mu2=calmoment(A,2)
    mu3=calmoment(A,3)
    g=mu3/pow(mu2,1.5)
    print("Population skweness is",g)
    n=A.size
    G=math.sqrt(n*(n-1)*g/(n-2))
    print("Sample skewness is",G)
    return
def calkurt(A):
    mu4=calmoment(A,4)
    mu2=calmoment(A,2)
    kurt=mu4/pow(mu2,2)
    kurtexc=kurt-3
    print("Population degree of kurtosis is",kurt)
    print("Population excess of kurtosis is",kurtexc)
    n=A.size
    g2=((n+1)*kurtexc+6)*(n-1)/((n-2)*(n-3))
    print("Sample kurtosis is",g2)
    return

B=genfromtxt('height.csv',delimiter=',',skip_header=1)



print("Using user defined functions")
print('*************************')
calskewness(B)
calkurt(B)
print("\n")
print("Using inbuilt functions")
print("******************")
print("Excess of kurtosis is",kurtosis(B))
print("Skewness is",(skew(B)))

print("*********************")


pos=100
scale=5
size=100000
values=np.random.normal(pos,scale,size)
plt.hist(values,100)
plt.show()

