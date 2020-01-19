import numpy as np

class server:
    def __init__(self):
    	"""Initializes a server"""
    	self.neighbors=[]

    def get_weights(self):
        """broadcasts weights from server"""
        
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
    
    def get_neighbors(self):
        """Returns list of neighboring nodes"""
        return self.neighbors

    def set_neighbor(self, node):
        """Connects the server with the given node"""
        self.neighbors.append(node)

    # def update_step(self):
        
    # def objective(self, lam):