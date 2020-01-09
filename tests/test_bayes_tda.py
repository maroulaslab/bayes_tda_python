# BAYES TDA UNIT TESTS
#---------------------
'''
Unit tests for bayes_tda module

author: Chris Oballe
created: 03/21/2019
last modified: 04/12/2019
'''

# imports
import unittest
from bayes_tda import *
#---------------

class TestWedgeGaussian(unittest.TestCase):

    def test_eval_one(self):
        x = [0,0]
        wg = WedgeGaussian(mu = [0,0], sigma = 1)
        self.assertEqual(wg.eval(x),0.15915494309189535)

    def test_eval_two(self):
        x = [-1,2]
        wg = WedgeGaussian(mu = [0,0], sigma = 1)
        self.assertEqual(wg.eval(x), 0)

    def test_eval_three(self):
        x = [1,-2]
        wg = WedgeGaussian(mu = [0,0], sigma = 1)
        self.assertEqual(wg.eval(x), 0)

class TestPrior(unittest.TestCase):
    

    def test_eval_one(self):
        x = [0,0]
        means = np.array([[0,0],[1,1]])
        ss = [1,2]
        ws = [1,5]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        d_pri = pri.eval(x)
        self.assertEqual(d_pri,0.4004858246670301)

    def test_eval_two(self):
        x = [0,-1]
        means = np.array([[0,0],[1,1]])
        ss = [1,2]
        ws = [1,5]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        d_pri = pri.eval(x)
        self.assertEqual(d_pri,0)
        
class TestPosterior(unittest.TestCase):
    
    def test_init_one(self):
        means = np.array([[0,0],[6,6]])
        ss = [1,1]
        ws = [1,1]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
        post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
        self.assertEqual(post.wscalars,[0.0001196398896002352,
                                        0.0001196398896002352,
                                        0.0001196398896002352,
                                        0.0001196398896002352])
    
    def test_init_two(self):
        means = np.array([[0,0],[6,6]])
        ss = [1,1]
        ws = [1,1]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
        post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
        self.assertEqual([list(x) for x in post.pmeans],[[0.5, 2.5],[2.5, 0.5],[3.5, 5.5],[5.5, 3.5]])
    
    def test_init_three(self):
        means = np.array([[0,0],[6,6]])
        ss = [1,1]
        ws = [1,1]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
        post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
        self.assertEqual(post.Qs,[0.760095246283323, 0.760095246283323, 0.9999996284508101, 0.9999996284508101])
        
    
    def test_init_four(self):
        means = np.array([[0,0],[6,6]])
        ss = [1,1]
        ws = [1,1]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
        post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
        self.assertEqual(post.cluts,[0.0, 0.0, 0.0, 0.0])
 
    
    def test_init_five(self):
        means = np.array([[0,0],[6,6]])
        ss = [1,1]
        ws = [1,1]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
        post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
        self.assertEqual(post.Cs,[0.5681511913674839,
                                  0.5681511913674839,
                                  0.5681511913674839,
                                  0.5681511913674839])
    
    def test_init_six(self):
        means = np.array([[0,0],[6,6]])
        ss = [1,1]
        ws = [1,1]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
        post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
        self.assertEqual(post.psigmas,[0.5,0.5,0.5,0.5])
        
        
    def test_eval(self):
        x = [0,0]
        means = np.array([[0,0],[6,6]])
        ss = [1,1]
        ws = [1,1]
        pri  = Prior(weights = ws,mus = means, sigmas = ss)
        noise = Prior(weights = [0], mus = [[30,30]], sigmas = [10])
        post = Posterior(prior = pri,clutter = noise,Dy = [[1,5],[5,1]], sy = 1)
        self.assertEqual(post.eval(x), 0.0005437883664915833)


if __name__ == '__main__':
    unittest.main()
