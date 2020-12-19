import random


step = 0.001
accurancy = 1e-6

y = 10
x = a1 = 5
w1, w2 = random.uniform(0, 3), random.uniform(0, 3)
a2 = w1 * a1
a3 = w2 * a2


while abs(a3 - y) > accurancy:
    print(w1, w2, w1 * w2)
    w2 = w2 - step * 2 * (a3 - y) * a2
    w1 = w1 - step * 2 * (a3 - y) * w2 * a1
    
    a2 = w1 * a1
    a3 = w2 * a2
