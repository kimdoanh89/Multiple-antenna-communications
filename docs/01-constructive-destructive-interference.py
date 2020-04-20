import scipy.integrate as integrate
import scipy.stats as stats
import numpy as np
from numpy import sqrt, pi, sin, radians
import matplotlib.pyplot as plt

# Constructive-destructive-interference
t = np.arange(0, 1+0.01, 0.01)
y1 = sqrt(2)*sin(2*pi*t)
energy1 = integrate.quad(lambda t: (sqrt(2)*sin(2*pi*t))**2, 0, 1)
theta_degree = np.arange(-180, 180+10, 10)
theta = radians(theta_degree)
energy2 = [integrate.quad(lambda t: (1/sqrt(2)*(sqrt(2)*sin(2*pi*t) + sqrt(2)*sin(2*pi*t - theta_point)))**2, 0, 1)
           for theta_point in theta]
energy2_first = [energy2_tuple[0] for energy2_tuple in energy2]

plt.plot(theta_degree, energy1[0]*np.ones(theta_degree.size), 'k--',
         theta_degree, energy2_first, 'b')
plt.legend(('One signal', 'Two signals'))
plt.xlabel('Phase difference (degrees)')
plt.ylabel('Energy')
plt.xlim([-180, 180])
plt.ylim([0, 2])

# Channel capacity
# Gaussian distribution
mu = 0
variance = 1
sigma = sqrt(variance)
x = np.linspace(mu-5*sigma, mu+5*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.xlabel('x')
plt.ylabel('Probability density function')
plt.xlim([-5, 5])
plt.ylim([0, 0.4])
# Complex gaussian distribution
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sigma2 = sigma/sqrt(2)
x_r = np.linspace(-5, 5, 100)
x_i = np.linspace(-5, 5, 100)
x_r, x_i = np.meshgrid(x_r, x_i)
ax.plot_surface(x_r, x_i, stats.norm.pdf(x_r, mu, sigma2) * stats.norm.pdf(x_i, mu, sigma2), color='r', cmap=plt.cm.Spectral)
ax.set_xlabel('Real part')
ax.set_xlim(-5, 5)
ax.set_ylabel('Imaginary part')
ax.set_ylim(-5, 5)
ax.set_zlabel('Probability density function')
ax.set_zlim(0, 0.3)
# Capacity behaviours
B = np.linspace(0, 100, 100)
plt.plot(SNR, np.log2(1+5*10**6*B))

