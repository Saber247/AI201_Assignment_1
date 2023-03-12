#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                print(curr, end=' ')
                for neighbor in self.adj_list[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
    
    def dfs(self, start):
        visited = set()
        self.dfs_recursive(start, visited)
    
    def dfs_recursive(self, curr, visited):
        if curr not in visited:
            visited.add(curr)
            print(curr, end=' ')
            for neighbor in self.adj_list[curr]:
                self.dfs_recursive(neighbor, visited)
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex)
            for neighbor in self.adj_list[vertex]:
                print(neighbor)
            print()


# In[20]:


graph = Graph()

# add edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 3)

#graph.print_graph()
graph.dfs(4)
print()
graph.bfs(4)


# In[ ]:




