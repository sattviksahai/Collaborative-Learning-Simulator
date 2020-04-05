import networkx as nx
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import server
import workerhandler
import workerclass

class topology_manager:
	def __init__(self):
		self.g = nx.Graph()
		self.color_map = []
	
	def connect(self, node1, node2):
		"""connects 2 nodes in a network"""
		node1.set_neighbor(node2)
		node2.set_neighbor(node1)

	def connect_star(self, server, client_list):
		"""connects a server and a list of clients in a star topology"""
		self.color_map.append('green')
		for i, (client) in enumerate(client_list):
			self.connect(server, client)
			self.g.add_edge(0,i+1)
			self.color_map.append('blue')

	def plot_topology(self):
		return nx.draw(self.g, node_color=self.color_map, with_labels = True)