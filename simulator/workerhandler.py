import torch
import numpy as np
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import workerclass

class workerhandler:
    """Class defining a handler for all worker nodes"""
    def __init__(self, all_workers):
        """Initialize worker nodes"""
        # self.genuine_workers = [workerclass.workerclass() for w in range(num_genuine_workers)]
        # self.malicious_workers = [workerclass.malicious_workerclass() for w in range(num_malicious_workers)]
        self.all_workers = all_workers
        
    def set_active_workers(self, num_active_workers):
        """Select a subgroup of worker nodes which will be involved in the current iteration"""

    def perform_updates(self):
        """Invokes a round of learning on active workers"""

    def set_param(self, w):
        """Set model parameters to latest"""

    def get_all_workers(self):
        """Returns a list of all workers"""
        return self.all_workers.copy()
        
    # def loss(self, temp_w):
    #     """Compute local loss"""
    #     yx = numpy.multiply(self.y_batch, self.x_batch) # s-by-d
    #     yxw = numpy.dot(yx, temp_w) # s-by-1
    #     vec1 = numpy.exp(-yxw) # s-by-1
    #     vec2 = numpy.log(1+vec1) # s-by-1
    #     return numpy.sum(vec2)
        
    # def gradient(self, y, x, temp_w):
    #     """Compute local gradient"""
    #     yx = numpy.multiply(y, x) # s-by-d
    #     yxw = numpy.dot(yx, temp_w) # s-by-1
    #     vec1 = numpy.exp(yxw) # s-by-1
    #     vec2 = numpy.divide(yx, 1+vec1) # s-by-d
    #     g = -numpy.sum(vec2, axis=0).reshape(self.d, 1) # d-by-1
    #     return g
    
    # def agd(self, g, temp_w):
    #     self.v *= self.beta
    #     self.v += g
    #     temp_w -= self.alpha*self.v
    #     return temp_w
        
    # def objective(self, lam, loss, temp_w):
    #     reg = lam/2 * numpy.sum(temp_w*temp_w)
    #     self.obj = loss/self.s + reg
    #     return self.obj
        
    # def client_update(self):
    #     obj_vals=[]
    #     temp_w = self.w
    #     for i in range(self.q):
    #         # evaluate objective function
    #         local_loss =self.loss(temp_w)
    #         obj_vals.append(self.objective(self.lam, local_loss, temp_w))
    #         for j in range(self.y_batch.shape[0]):
    #             g = self.gradient(self.y_batch[j,:], self.x_batch[j,:], temp_w)
    #             temp_w = self.agd(g, temp_w)
    #     return self.w - temp_w, obj_vals