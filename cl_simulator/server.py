import numpy as np
from collections import OrderedDict

class server:
    def __init__(self, lr):
        """Initializes a server"""
        self.neighbors=[]
        self.lr=lr
        self.w=None

    def set_init_weights(self, w):
        self.w=w

    def get_weights(self):
        """broadcasts weights from server"""
        return self.w
        
    # 
    # Args:
    #     weights: list of d-by-1 vectors
    #     losses: list of scalars
    def aggregate(self, grads):
        """Aggregates losses and weights from all workers

        Parameters
        ----------
        grads : list of tensors
            A list of the updated gradients from all workers
        """
        new_weights = OrderedDict()
        for item_w,item_g in zip(self.w.items(), grads.items()):
            new_weights.update({item_w[0]:(item_w[1]-(self.lr*item_g[1]))})
        self.w = new_weights
        return self.w
    
    def get_neighbors(self):
        """Returns list of neighboring nodes"""
        return self.neighbors

    def set_neighbor(self, node):
        """Connects the server with the given node"""
        self.neighbors.append(node)

    # def update_step(self):
        
    # def objective(self, lam):