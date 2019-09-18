import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sale = pd.read_csv('sale.csv')
X = np.array(sale.iloc[:, 1:4])
Y = np.array(sale.iloc[:, -1])
a = X.max()
b = X.min()
X = (X-b)/(a-b)
ay = Y.max()
by = Y.min()
Y = (Y-by)/(ay-by)

n = len(Y)


def y(w1, w2, w3, x):
    return w1*x[0]+w2*x[1]+w3*x[2]


def MSE(w1, w2, w3):
    ans = 0
    for i in range(n):
        ans += (Y[i]-(w1*X[i][0]+w2*X[i][1]+w3*X[i][2]))**2
    return ans/2/n


def fw1(w1, w2, w3):
    ans = 0
    for i in range(n):
        ans += X[i][0]*(Y[i]-y(w1, w2, w3, X[i]))
    return 2*ans/(-n)


def fw2(w1, w2, w3):
    ans = 0
    for i in range(n):
        ans += X[i][1]*(Y[i]-y(w1, w2, w3, X[i]))
    return 2*ans/(-n)


def fw3(w1, w2, w3):
    ans = 0
    for i in range(n):
        ans += X[i][2]*(Y[i]-y(w1, w2, w3, X[i]))
    return 2*ans/(-n)


LR = 0.001
epochs = 3005
w1 = 10
w2 = 10
w3 = 10
mse = []
for i in range(epochs):
    #print(w1)
    #print(w2)
    #print(w3)
    #print(MSE(w1,w2,w3))
    #print('===============')
    t1, t2, t3 = w1, w2, w3
    w1 -= LR*fw1(t1, t2, t3)
    w2 -= LR*fw2(t1, t2, t3)
    w3 -= LR*fw3(t1, t2, t3)
    mse.append(MSE(w1, w2, w3))

plt.plot(range(epochs), mse, c='green')
plt.title('Error rate')
plt.ylabel('MSE')
plt.xlabel('Iterations')

plt.show()
