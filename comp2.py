
# coding: utf-8

# # Comp 2
# 
# Peter Vanya
# 
# Jarná škola FX, marec 2016
# 
# ## Program na dnes
# 
# * Matematické operácie, vektory a matice. Hľadanie vlastných čísel. 
# * Prvé zoznámenie sa s knižnicami `numpy` a `matplotlib`

# In[8]:

# najskor nacitame kniznice
# toto je vseobecne zauzivana konvencia, nemente ju!
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# ## Vektory

# In[9]:

a = np.array([1,2,3])
print(a)
type(a)

b = np.array([2,3,4])
print(a + b)    # spravne scitanie!


# In[4]:

np.dot(a, b)    # skalarny sucin


# In[5]:

np.cross(a, b)  # vektorovy sucin


# In[7]:

np.outer(a, b)  # outer product (jak sa to povie po slovensky?), premyslite si


# ## Matice

# In[107]:

A = np.array([[0,1], [1,0]])
print(A)
type(A)


# In[23]:

AA = np.matrix(A)   # premena na iny datovy typ
type(AA)


# In[108]:

B = np.array([[1, 0], [0, -1]])
print(B)


# In[28]:

C = np.dot(A, B)
print(C)
# pozor!
print(A*B)


# In[30]:

# Vlastnosti matic
print(len(A))
print(A.shape)


# In[7]:

# uzitocne vektory/matice, konvencia z Matlabu
N = 3
print(np.ones(N), "\n")      # konstantny vektor
print(np.ones((N, N)), "\n") # 
print(np.eye(N), "\n")       # identita
print(np.zeros((N, N)))      # nulova matica NxN


# ## Generovanie (pseudo)náhodných čísel

# In[92]:

# cisla sa menie, pokial nefixneme seed!
np.random.seed(10)

N = 5
a = np.random.rand(N)   # v intervale [0,1]
A = np.random.rand(N, N)
print(a, "\n")
print(A)


# In[94]:

a = np.random.randn(N)      # gaussovske cisla
print(a)

mu, sigma = 1.0, 2.0
a = np.random.randn(200)*sigma + mu
plt.hist(a)
plt.show()


# In[65]:

a = np.random.randint(10, size=10)   # cele cisla, pozor na size!
print(a)


# ## Vlastné čísla

# In[95]:

from numpy.linalg import eig


# In[106]:

N = 20
A = np.random.rand(N, N)
vals, vecs = eig(A)
print(vals.real)


# ## Pozn
# 
# Okrem toho existujú funkcie na vlastné čísla symetrických alebo hermitovských matíc `eigs` a `eigh`.
# 
# ## Problem
# TO FILL

# ## Matematické funkcie

# In[3]:

import math
print(math.__dict__.keys())


# In[4]:

math.pi


# In[5]:

math.cos


# ## Grafy

# In[18]:

import matplotlib
matplotlib.rcParams.update({'font.size': 16})

x = np.linspace(0, 2*math.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("$x$")
plt.ylabel("$\sin(x)$")
plt.xlim([0, 2*math.pi])
plt.show()


# ## Pár slov k štylistike
# Python má svoje štylistické štandardy PEP 8, ktoré odporúčam dodržiavať. Podľa miery dodržiavania sa určuje "krása" (a čitateľnost) kódu.
# 
# * odsadzovanie for cyklov a funkcií o štyri medzery
# * za čiarkou nasleduje medzera
# * medzi "=" je medzera, (napr. `a = 2`), ale nie vo funkcii (napr. `def (a, b=5)`)
# * názvy funkcií malými písmenami, slová oddeľujeme podtržníkom (napr. `calc_evals(A)`), názvy objektov veľkými písmenami (pre expertov)

# In[ ]:



