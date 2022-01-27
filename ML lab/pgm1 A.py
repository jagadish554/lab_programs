# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 13:52:24 2021

@author: HP
"""

def aStarAlgo(start_node,stop_node):
    open_set=set(start_node)
    closed_set=set()
    g={}
    parents={}
    g[start_node]=0
    parents[start_node]=start_node
    while len(open_set)>0:
        n=None
        for v in open_set:
            if n==None or g[v] + heuristic(v)< g[n] + heuristic(n):
                n=v
        if n==stop_node or Graph_nodes[n]==None:
            pass
            else:
            for(m,weight) in get_neighbor(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n==None:
            print("path does noot exist!")
            return None
        if n==stop_node:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start_node)
            path.reverse()
            print("path found: {}".format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print("path does not exist!")
    return None

def get_neighbor(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
def heuristic(n):
    h_dist={ 'S' :7,
             'A' :6,
             'B' :2,
             'C' :1,
             'G' :0
            }
    return h_dist[n]
Graph_nodes = {'S':[('A',1),('B',4)],
               'A':[('B',2),('C',5),('G',12)],
               'B':[('C',2)],
               'C':[('G',3)]
               }
aStarAlgo('S','G')