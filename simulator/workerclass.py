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

class workerclass:
    """ Class defining a worker node """
    def __init__(self):
        """ Initialize the worker node """
        self.neighbors=[]

    def set_param(self, w):
        """ set model parameters to latest """
        
    def client_update(self):
        """ Perform updates on model using worker data """

    def get_neighbors(self):
        """Returns list of neighboring nodes"""
        return self.neighbors

    def set_neighbor(self, node):
        """Connects the worker with the given node"""
        self.neighbors.append(node)

class malicious_workerclass:
    """ Class defining a worker node """
    def __init__(self):
        """ Initialize the worker node """
        self.neighbors=[]

    def set_param(self, w):
        """ set model parameters to latest """
        
    def client_update(self):
        """ Perform updates on model using worker data """

    def get_neighbors(self):
        """Returns list of neighboring nodes"""
        return self.neighbors

    def set_neighbor(self, node):
        """Connects the worker with the given node"""
        self.neighbors.append(node)