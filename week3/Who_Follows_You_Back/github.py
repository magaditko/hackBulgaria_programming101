import requests
import json

from directed_graph import Graph
from node import Requester


class Github:

    def __init__(self, username, depth):
        self.graph = Graph()
        self.request = Requester()
        self.depth = depth
        self.username = username

    def _get_following(self, username):
        
        print(self.request.following(username))


g = Github('shosh', 2)
print(g._get_following('shosh'))
