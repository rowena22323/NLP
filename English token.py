#!/usr/bin/env python
# coding: utf-8

# In[5]:


from nltk.corpus import gutenberg
from nltk import regexp_tokenize
import nltk
import matplotlib.pyplot as plt


# In[24]:


files_en=gutenberg.fileids()
doc_en=gutenberg.open('austen-emma.txt').read()
pattern = r'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"'?():-_`]'''
tokens_en=regexp_tokenize(doc_en, pattern)
en = nltk.Text(tokens_en)
print(len(en.tokens)) # returns number of tokens(document length)


# In[50]:


len(set(en.tokens))


# In[55]:


a=dict(en.vocab())
print(a)


# In[43]:


plt.axis([0,50,0,25])
en.plot(50)


# In[57]:


print(en.count('day'))

