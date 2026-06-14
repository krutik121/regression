import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')

print("Setup successful!")

x_train = np.array([1.0,2.0,3.0,4.0,5.0])
y_train = np.array([300.0,500.0,700.0,900.0,1100.0])

def compute_cost(x,y, w, b):
    m = x.shape[0]
    cost = 0.0

    for i in range(m):
        f_wb_i = w * x[i] + b
        cost = cost + (f_wb_i - y[i]) ** 2

    cost = cost / (2 * m)

    return cost

plt.plot(x_train, y_train, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Training data')
plt.show()

# x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
# y_train = np.array([250, 300, 480,  430,   630, 730,])

plt.close('all')
fig, ax, dyn_items = plt_stationary(x_train, y_train)
plt.show()