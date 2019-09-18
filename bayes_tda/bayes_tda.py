# BAYES TDA
#===========
'''
This module contains classes and methods to implement the Bayesian model for persistent homology introduced in

Maroulas, V., Nasrin, F., and Oballe, C. 2018.
Bayesian Inference with Persistent Homology

The model relies heavily on marked Poisson processes and mixed Gaussian assumptions.

author: Chris Oballe
created: 3/21/2019
last modified: 4/12/2019
'''

# imports
import numpy as np
from scipy.stats import multivariate_normal as mvn
import itertools
#---------

class WedgeGaussian:
    '''
    class for gaussian densities restricted to the first quadrant
    '''

    def __init__(self,mu,sigma):
        # mu: mean of gaussian density, given as a 1x2 np.array or a two-element list
        # sigma: magnitude of covariance matrix, given as a numeric

        self.mu = np.array(mu)
        self.sigma = sigma

    def eval(self,x):
        # x: value in R^2 at which to evalaute density, given as a two-element list or 1x2 array 

        x = np.array(x)
        dens =  mvn.pdf(x=x,mean = self.mu ,cov = self.sigma)

        c1 = x[0] >= 0
        c2 = x[1] >= 0

        if c1 and c2:
            return dens
        else:
            return 0


class Prior:
    '''
    class for mixed gaussian priors
    '''

    def __init__(self,weights,mus,sigmas):
        # weights: weights for each component, given as a list of numerics
        # mus: means for each component, given as an np.array where each entry is a two-element list corresponding to a mean
        # sigmas: cov magnitude for each component, given as a list of numeric
        # self.comps: individual gaussian components of the prior, given as a list of WedgeGaussians
        
        self.weights = weights
        self.mus = mus
        self.sigmas = sigmas
        self.comps = [WedgeGaussian(mu = m, sigma = s) for m,s in zip(mus,sigmas)]

    def eval(self,x):
        # x: value in R^2 at which to evaluate density, given as a two-element list or 1x2 array

        x = np.array(x)

        d_vals = list(map(lambda comp: comp.eval(x),self.comps))

        return np.dot(d_vals,self.weights)


class Posterior:
    '''
    class for mixed gaussian posterior
    '''

    def __init__(self,prior,clutter,Dy,sy, alpha = 1):
        # prior: mixed gaussian prior object
        # clutter: mixed gaussian prior object (models noise)
        # Dy: input diagram, given as an np.array where each entry are points in a PD
        # sy: covariance magnitude of stochastic kernel, given as a numeric
        # wscalars: components of w^y, given as a list
        # Qs: Q values from paper, given as a list
        # pmeans: posterior means, given as an np.array
        # psigmas: posterior sigmas, given as a list
        # alpha: alpha parameter from paper, given as a numeric

        self.prior = prior
        self.clutter = clutter
        self.Dy = np.array(Dy)
        self.sy = sy
        self.wscalars = [self.prior.weights[i]*mvn.pdf(x=self.Dy[j],mean = self.prior.mus[i],cov = self.prior.sigmas[i]+self.sy) for i in range(len(self.prior.weights)) for j in range(len(self.Dy))]
        self.pmeans = [(self.prior.sigmas[i]*np.array(Dy[j])+self.sy*np.array(self.prior.mus[i]))/(self.prior.sigmas[i]+self.sy) for i in range(len(self.prior.mus)) for j in range(len(self.Dy))]
        self.psigmas = [(self.prior.sigmas[i]*self.sy)/(self.prior.sigmas[i] + self.sy) for i in range(len(self.prior.sigmas)) for j in range(len(self.Dy))]
        self.Qs = [1-(mvn.cdf([float('inf'),0],mean = self.pmeans[i], cov = self.psigmas[i])+ mvn.cdf([0,float('inf')],mean = self.pmeans[i], cov = self.psigmas[i]))+ mvn.cdf([0,0],mean = self.pmeans[i], cov = self.psigmas[i]) for i in range(len(self.pmeans))]
        self.alpha = alpha
        self.cluts = [self.clutter.eval(y) for y in self.Dy]*len(self.prior.mus)
        self.wQs = list(np.multiply(self.wscalars,self.Qs))
        self.Csums = [sum(self.wQs[i::(len(self.Dy))]) for i in range(0,len(self.Dy))]*len(self.prior.mus) # sum every len(prior.mus) entry
        self.Cs = [w/(c+s) for w,c,s in zip(self.wscalars,self.cluts,self.Csums)]

    def eval(self,x):
        # x: point in wedge at which to evaluate posterior intensity, given as np array
        
        dxv = (1-self.alpha)*self.prior.eval(x)
        dxo = [C*mvn.pdf(x=x,mean = m, cov = s) for C,m,s in zip(self.Cs,self.pmeans,self.psigmas)]
        dxo = self.alpha*sum(dxo)
        return(dxv + dxo)
        