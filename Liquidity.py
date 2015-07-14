import numpy as np
import matplotlib.pyplot as plt
count = 1000 # 1000 timestamps
p0 = 10 # initial price
v0 = 10000 # volume of the megaorder that i place

# market without my participation
parray=[] # price array
varray=[] # volume array
parray.append(p0)
varray.append(v0*np.random.rand())
for i in range(1,count):
	dp=np.random.choice([-0.01,0,0.01])
	parray.append(parray[i-1]+dp) # price changes in a random walk fashion
	varray.append(100*np.random.rand()) # volume at each time can't be higher than what I place
plt.plot(parray,'b',label='original market')


# market with my participation
#dt = 10 # I am able to trade every 10 counts
nparray = parray # the market price trend after I place the order
nparray.append(parray[0])
rV = varray[0] #initial realised traded volume
cost = nparray[0] * varray[0] # initial cost
i = 1
while rV <= v0: #rV<=v0
	if parray[i-1]>parray[i]: # if the price decreases
		nparray[i] = parray[i-1] + np.random.choice([0,0.01]) # how should my order affect the price to increase?
	cost += parray[i] * varray[i]
	rV += varray[i]
	i+=1
print i
print cost-p0*v0
for j in range(i,count):
	dp=np.random.choice([-0.01,0,0.01])
	nparray[j]=nparray[j-1]+dp

plt.plot(nparray,'r',label='with my participation')
plt.axvline(x=i, color='g',label='at time %s, trading cost is %s' %(i,cost))
plt.ylim([min(min(nparray),min(parray))-0.3,max(max(nparray),max(parray))+0.3])
plt.legend(loc='upper center',bbox_to_anchor=(0.5, 1.05))
plt.show()