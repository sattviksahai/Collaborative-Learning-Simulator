import torch
from torch.utils.data import DataLoader, Dataset
import numpy as np

class ImageData(Dataset):
    """ dataloader for the worker """
    def __init__(self, path, transform, subset="train"):
        super().__init__()

    def __len__(self):
        """Returns the length of the local dataset"""
    
    def __getitem__(self, index):
        """Returns a datapoint as per the index"""

class base_workerclass:
    """ Class defining a worker node """
    def __init__(self, name, is_malicious_worker, neighbors=[]):
        """ Initialize the worker node """
        self.name=name
        self.optim=None
        self.is_malicious_worker=is_malicious_worker
        self.neighbors=neighbors

    def set_param(self, w):
        """ set model parameters to latest """
        raise Exception('set_param function not defined')

    def get_params(self):
        """ Returns model parameters """
        raise Exception('get_param function not defined')

    def set_optim(self):
        """ set optimizer for model """
        raise Exception('optimizer not defined')

    def client_update(self, global_epoch):
        """ Perform updates on model using worker data """
        raise Exception('client_update function not defined')

    def get_neighbors(self):
        """Returns list of neighboring nodes"""
        return self.neighbors

    def set_neighbor(self, node):
        """Connects the worker with the given node"""
        self.neighbors.append(node)

    def is_malicious(self):
        return self.is_malicious_worker

# class malicious_workerclass:
#     """ Class defining a worker node """
#     def __init__(self):
#         """ Initialize the worker node """
#         self.neighbors=[]

#     def set_param(self, w):
#         """ set model parameters to latest """
        
#     def client_update(self):
#         """ Perform updates on model using worker data """

#     def get_neighbors(self):
#         """Returns list of neighboring nodes"""
#         return self.neighbors

#     def set_neighbor(self, node):
#         """Connects the worker with the given node"""
#         self.neighbors.append(node)