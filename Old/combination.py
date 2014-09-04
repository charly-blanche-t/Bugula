

import functools
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction
from random import shuffle


def nCk(n,k): 
  return int(functools.reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def nber_permutation_test(G,H):
  nber_edges = len(G.nodes())
  nber_green_edges = len(H.nodes())
  nber_permutation = nCk(nber_edges,nber_green_edges)
  
  return nber_permutation


def swap_vertices(G):
  all_nodes = G.nodes()
  success = False

  while not success:
    vertex_a = random_node(all_nodes)
    vertex_b = random_node(all_nodes)
 
    if G.node[vertex_a]['color'] != G.node[vertex_b]['color']:
      success = True
      color_a = G.node[vertex_a]['color']
      G.node[vertex_a]['color']= G.node[vertex_b]['color']
      G.node[vertex_b]['color'] = color_a

  return G



def random_node(l):
  shuffle(l)
  return l[0]
