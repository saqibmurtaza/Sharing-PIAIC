#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[148]:


x=np.array([5,2,9,4])
y=np.array([10,9,4,3])
z=np.array([2.5,9.7,1.2,2.4])
num=np.array([-1.6,-2.9,-3.0,-8.9])
angles=np.array([90,180,270,360])
set=np.array([2,2,2,3,4,3,9,9,8,7,7])


# In[22]:


sqrt=np.sqrt(x)
power=np.power(x,3)
mean=np.mean(x)
exp=np.exp(x)
log=np.log(x)
log2=np.log2(x)
log10=np.log10(x)
a=np.reciprocal(x)
b=np.isreal(x)
c=np.square(x)


# In[26]:


sqrt,power,mean,exp,log,log2,log10,a,b,c


# In[27]:


x,y,z


# In[54]:


absolute=np.absolute(num)
d=np.maximum(x,y)
f=np.minimum(x,y)


# In[55]:


absolute,d,f


# In[108]:


sinit=np.sin(angles)
sinit


# In[57]:


np.cos(angles)


# In[58]:


np.tan(angles)


# In[171]:


sumit=np.sum(x)
add=np.add(x,y)
mul=np.multiply(x,y)
division=np.divide(x,y)
diff=np.subtract(x,y)
tru=np.trunc(z)
fixit=np.fix(num)
roundnum=np.around(sinit,2)
flornum=np.floor(sinit)
ceil=np.ceil(num)
modit=np.mod(x,y)
divnmod=np.divmod(x,y)
cumsum=np.cumsum(x)


# In[172]:


sumit,add,mul,division,diff,tru,fixit,roundnum,flornum,ceil,modit,divnmod,cumsum


# In[138]:


num1=20
num2=30
lcm=np.lcm(num1,num2)
gcd=np.gcd(num1,num2)
lcm,gcd


# In[136]:


lcmit=np.lcm.reduce(x)
gcdit=np.gcd.reduce(x)


# In[137]:


lcmit,gcdit


# In[145]:


d2r=np.deg2rad(angles)
r2d=np.rad2deg(d2r)


# In[146]:


d2r,r2d


# In[161]:


u=np.unique(set)
union=np.union1d(set,u)
intersection=np.intersect1d(set,x)


# In[158]:


u,union,intersection


# In[176]:


dif=np.diff(x)
diff=np.diff(x,n=2)
where=np.where(u>5,"ok","nok")


# In[177]:


dif,diff,where


# In[183]:


matrix1=np.random.randn(2,3)
matrix2=np.random.randn(3,2)


# In[184]:


matrix1,matrix2


# In[192]:


dot=matrix1.dot(matrix2)
tp=matrix1.transpose()
plus=matrix1+matrix1
minus=matrix2-matrix2


# In[195]:


dot,tp,plus,minus,matrix1.trace()


# In[197]:


base=2
perp=3
np.hypot(base,perp)


# In[198]:


np.arcsin(1)


# In[199]:


np.arccos(1)


# In[200]:


np.arctan(1)


# In[ ]:




