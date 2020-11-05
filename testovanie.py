#!/usr/bin/env python
# coding: utf-8

# In[1]:


3+4


# In[2]:


3+6


# In[3]:


solve(x^3 - 1 == 0, x)


# In[4]:


k = GF(5);
for a in k:
    print(2*a)


# In[5]:


factor(2021)


# In[6]:


factor(x^2-4)


# In[7]:


factor(x^4+4y^4)


# In[11]:


EllipticCurve(GF(101),[2,3])


# In[14]:


11+2


# In[16]:


EllipticCurve(GF(101),[2,7])


# In[19]:


EllipticCurve(GF(101),[2,7]);
E.abelian_group()


# In[1]:


E = EllipticCurve(GF(101),[2,7])
E


# In[2]:


E.plot()


# In[3]:


EE = EllipticCurve([-10,10])
EE


# In[4]:


EE.plot()


# In[5]:


E.order()


# In[6]:


E.cardinality()


# In[7]:


E.order() == E.cardinality()


# In[8]:


E.points()


# In[9]:


EE.order()


# In[10]:


EE.cardinality()


# In[11]:


EE.points()


# In[12]:


P = E.random_point()
P


# In[13]:


P.order()


# In[18]:


Q = E.random_point()
Q;
Q.order()


# In[20]:


R = E.random_point()
R


# In[21]:


R.order()


# In[23]:


Fq = GF(11^2);
Fq


# In[24]:


Fq.gen()


# In[5]:


2+4


# In[8]:


E = EllipticCurve(GF(101),[2,7])
E


# In[9]:


E.j_invariant()


# In[14]:


F = EllipticCurve_from_j(GF(101)(18))
F


# In[21]:


E.is_quadratic_twist(F)


# In[16]:


F.j_invariant()


# In[28]:


phi = EllipticCurveIsogeny(E, E((82,68)) )
phi


# In[29]:


phi.degree()


# In[30]:


phi.kernel_polynomial()


# In[31]:


phi.rational_maps()


# In[48]:


S = E.random_point()
S.order()


# In[49]:


S


# In[52]:


iso = EllipticCurveIsogeny(E, E((69,0)) )
iso


# In[53]:


iso.degree()


# In[54]:


iso.rational_maps()


# In[59]:


iso.kernel_polynomial()


# In[ ]:





# In[ ]:




