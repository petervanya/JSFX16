
# coding: utf-8

# # Comp 3
# 
# Peter Vanya
# 
# Jarná škola FX, marec 2016
# 
# ## Program na dnes
# Práca so súbormi, tlačenie a načítanie dát

# ## Za pomoci numpy
# 
# Najjednoduchší spôsob za pomoci dvoch príkazov: `np.loadtxt` a `np.savetxt`.

# In[14]:

# najjednoduchsi sposob
import numpy as np
import os

a = np.arange(10)
print(a)
fname = "subor.out"
np.savetxt(fname, a)   # vektor ulozeny v subor.out
os.listdir(".")        # je tam, ale pozor na formatovanie


# In[12]:

# opatovne nacitanie
b = np.loadtxt(fname)
print(b)    # premena z int na float


# ## Štandardný Python

# In[26]:

veta = "toto je veta"
fname = "veta.out"

# spravny sposob
with open(fname, "w") as f:
    f.write(veta)
        
# alebo na jeden riadok
open(fname, "w").write(veta + " " + veta)


# In[33]:

# nacitanie
veta = open(fname, "r").read()
print(veta)
print(len(veta))    # dlzka


# ## Operácie so stringom [Adv 1]
# Python má perfektné možnosti manipulácie stringov, stojí za to sa ich naučiť (napr. ak raz budete chcieť scrapovať internet alebo "čítať" emaily)

# In[32]:

print(veta.split())              # rozdel podla medzier
print(veta.split("t"))           # rozdel podla znaku t
print("_".join(veta.split()))    # spoj naspat podla zelaneho znaku


# In[48]:

# realny text
fname = "eminem.out"
lyric = open(fname, "r").read()
print(len(lyric))                   # pocet znakov
print(len(lyric.split()))           # pocet slov

print(lyric[:500])


# In[55]:

# inak
lyric = open(fname, "r").readlines()
print(len(lyric))   # pocet riadkov
print(lyric[:50])


# In[52]:

# najdime nejake slovo
word = "fuck"
[line for line in lyric if word in line]


# ***
# ## Úloha
# 
# Načítajte *Lose yourself* a nájdite počet prázdnych riadkov.
# ***

# ## Reálne dáta
# 
# Zoberme si xyz súbor `dump.xyz`.
# * Prvy riadok: počet atómov
# * Druhý riadok: komentár
# * Zvyšné riadky: typ atómu a súradnice

# In[62]:

fname = "dump.xyz"
A = open(fname).readlines()
print(A[:2])
print(A[2:])


# In[68]:

B = A[2:]
B = [[float(i) for i in line.split()] for line in B]
B


# ## Regulárne výrazy [Adv 2]
# *"Pokiaľ nevieš regulárne výrazy, nie si chlap!"* Tomáš Srnka, CTO Websupportu
# 
# Obrovská téma na samostatný predmet, ale načnime aspoň pár podstatných.
# 
# Hľadanie vzorov (pattern matching) v text, napr. veľkých písmen, čísel, znakov na začiatku riadkov etc.

# In[ ]:



