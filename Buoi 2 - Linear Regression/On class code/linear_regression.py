#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

def test_y(x):
    return 4*x+5+random.uniform(0.1,0.2)

X = list(range(-50,50,2))
Y = [test_y(i) for i in X]


# In[10]:


# y=w1*x+w2

def y(w1, w2, x):
    return w1*x+w2

y(1,2,3)


# In[33]:


def MSE(w1, w2):
    ans = 0
    for x_i, y_i in zip(X,Y):
        ans += (y_i - y(w1,w2,x_i))**2
    return (2/len(X))*ans


# In[30]:


def gradient_w1(w1, w2):
    ans = 0
    for x_i, y_i in zip(X,Y):
        ans += x_i*(y_i - y(w1,w2,x_i))
    return (-2/len(X))*ans


# In[31]:


def gradient_w2(w1, w2):
    ans = 0
    for x_i, y_i in zip(X,Y):
        ans += (y_i - y(w1,w2,x_i))
    return (-2/len(X))*ans


# In[39]:


epochs = 696
w1 = 9
w2 = 6
LR = 0.001

print('Epoch: 0')
print('MSE:', MSE(w1, w2))
print('w1 = {} || w2 = {}'.format(w1, w2))
print('==========================')

for i in range(epochs):
    temp = w1
    w1 -=  LR*gradient_w1(w1, w2)
    w2 -=  LR*gradient_w2(temp, w2)
    print('Epoch:', i+1)
    print('MSE:', MSE(w1, w2))
    print('w1 = {} || w2 = {}'.format(w1, w2))
    print('==========================')

