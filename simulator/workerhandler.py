import torch
import numpy as np
import os
import sys
import random
from collections import OrderedDict
sys.path.insert(0, os.path.dirname(__file__))

import workerclass

class workerhandler:
    """Class defining a handler for all worker nodes"""
    def __init__(self, all_workers):
        """Initialize worker nodes"""
        # self.genuine_workers = [workerclass.workerclass() for w in range(num_genuine_workers)]
        # self.malicious_workers = [workerclass.malicious_workerclass() for w in range(num_malicious_workers)]
        self.all_workers = all_workers
        self.active_status = np.array([True] * len(self.all_workers))
        
    def set_active_workers(self, num_active_workers = None):
        """Select a subgroup of worker nodes which will be involved in the current iteration"""
        assert num_active_workers <= len(self.all_workers), ('number of active workers cannot be more than total number of workers')
        assert num_active_workers >= 0, ('number of active workers cannot be negative')
        if None != num_active_workers:
            passive_indices = random.sample(range(0, len(self.all_workers)), len(self.all_workers)-num_active_workers)
            self.active_status[passive_indices] = False

    def get_active_status(self):
        """Returns active status of all workers"""
        return self.active_status

    def perform_updates(self, global_epoch):
        """Invokes a round of learning on active workers"""
        grads = []
        for worker in self.all_workers:
            print("training on worker: ",worker.name)
            grads.append(worker.client_update(global_epoch))
        gradavg = OrderedDict()
        for layer in grads[0].keys():
            values=[]
            for grad in grads:
                values.append(grad[layer])
            mean_val = torch.sum(torch.stack(values), axis=0)/len(self.all_workers)
            gradavg.update({layer:mean_val})
        return gradavg

    def set_param(self, w):
        """Set model parameters to latest"""
        for worker in self.all_workers:
            worker.set_param(w)

    def get_all_workers(self):
        """Returns a list of all workers"""
        return self.all_workers.copy()
        
    def get_average_weights(self):
        """Returns average weights of all workers"""
        weights = []
        for worker in self.all_workers:
            weights.append(worker.get_params())
        weightsavg = OrderedDict()
        for layer in weights[0].keys():
            values=[]
            for grad in weights:
                values.append(grad[layer])
            mean_val = torch.sum(torch.stack(values), axis=0)/len(self.all_workers)
            weightsavg.update({layer:mean_val})
        return weightsavg
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

if __name__ == "__main__":
    workers = workerhandler([None,None])
    print(workers.get_active_status())
