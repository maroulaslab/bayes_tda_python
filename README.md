# bayes_tda

This module contains classes to implement a marked Poisson process model for Bayesian inference with persistence diagrams. The model relies on mixed Gaussian assumptions. For a full description of the model, please refer to [https://arxiv.org/abs/1901.02034](https://arxiv.org/abs/1901.02034).


# Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bayes_tda.

```bash
pip install bayes_tda
```
# Classes

| Class name| Description |Methods |
|--|--|--|
| WedgeGaussian |Gaussian density restricted to upper half of $\mathbb{R}^2$.| eval|
|Prior| Mixed Gaussian prior intensity.| eval
|Posterior|Mixed Gaussian posterior intensity.| eval



# Usage
```python
from bayes_tda import *
import matplotlib.pyplot as plt
import numpy as np

x = [0,0] # a point in birth-persistence coordinates
wg = WedgeGaussian(mu = [0,0], sigma = 1) # Gaussian densities restricted to the upper half plane
d = wg.eval(x) # evaluates the Gaussian density at x

means = np.array([[0,0],[6,6]])
ss = [1,1]
ws = [1,1]

pri  = Prior(weights = ws,mus = means, sigmas = ss)
d_pri = pri.eval(x)

b = np.linspace(0,10,50)
p = np.linspace(0,10,50)

B,P = np.meshgrid(b,p)

Z = list()
for ind in range(len(P)):
    l = list()
    for i in range(len(P)):
        l.append(pri.eval([B[ind][i],P[ind][i]]))
    Z.append(l)
        
plt.style.use('seaborn-white')
plt.contourf(B,P,Z, 20, cmap = 'twilight')
plt.colorbar()
plt.show()

noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
peval = post.eval(x)

Z = list()
for ind in range(len(P)):
    l = list()
    for i in range(len(P)):
        l.append(post.eval([B[ind][i],P[ind][i]]))
    Z.append(l)
        
plt.style.use('seaborn-white')
plt.contourf(B,P,Z, 20, cmap = 'twilight')
plt.colorbar()
plt.show()
```
## Reporting Bugs
Report any bugs by opening an issue at [https://github.com/coballejr/bayes_tda/](https://github.com/coballejr/bayes_tda/).


## License
[MIT](https://choosealicense.com/licenses/mit/)