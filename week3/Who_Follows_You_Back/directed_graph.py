class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, nodeA, nodeB):
        if nodeA in self.graph:
            if nodeB not in self.graph[nodeA]:
                self.graph[nodeA].append(nodeB)
        else:
            self.graph[nodeA] = [nodeB]

    def get_neighbours_for_node(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return []
            
    def find_path(self, nodeA, nodeB, path=[]):
        path += nodeA
        if nodeA == nodeB:
            return path
        if nodeA not in self.graph:
            return []

        paths = []
        for node in self.graph[nodeA]:
            if node not in path:
                newpaths = self.find_path(node, nodeB, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def check_if_path_exists(self, nodeA, nodeB):
        path = self.find_path(nodeA, nodeB)
        if nodeA == nodeB:
            return False
        elif path == []:
            return False
        else:
            return True

    def to_string(self):
        result = ''
        for node in self.graph:
            result += '{}: {}\n'.format(node, str(self.graph[node]))
        return result
