
import networkx as nx
import functools
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction
#from random import shuffle
from random import choice


def nCk(n,k): 
  return int(functools.reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def nber_permutation_test(G,H):
  nber_edges = len(G.nodes())
  nber_green_edges = len(H.nodes())
  nber_permutation = nCk(nber_edges,nber_green_edges)
  
  return nber_permutation


def swap_vertices(G):
  
  for i in range (100):
    all_nodes = G.nodes()
    success = False

    while not success:
      vertex_a = choice(all_nodes)
      vertex_b = choice(all_nodes)
   
      if G.node[vertex_a]['color'] != G.node[vertex_b]['color']:
        success = True
        color_a = G.node[vertex_a]['color']
        G.node[vertex_a]['color']= G.node[vertex_b]['color']
        G.node[vertex_b]['color'] = color_a

  return G



def swap_edges(G):

  for i in range (100000):
    all_edges = G.edges()
    success = False

    while not success:
      edge_a = choice(all_edges)
      #print("edge_a ", edge_a )
      #print("edge_a ", edge_a," vertex 1", G[edge_a[0]], " and vertex 2 ", G[edge_a[1]] )
      edge_b = choice(all_edges)
      #print("edge_b ", edge_b," vertex 1", G[edge_b[0]], " and vertex 2 ", G[edge_b[1]] )
      #print("edge_b ", edge_b)    

      success = False
   
      if check_connectivity(G, edge_a[0], edge_a[1] , edge_b[0], edge_b[1]):
        success = True
        G.remove_edge(edge_a[0], edge_a[1])
        G.remove_edge(edge_b[0], edge_b[1])
        G.add_edge(edge_a[0], edge_b[1])
        G.add_edge(edge_b[0], edge_a[1])
  ##      print ("One success in swapping edges !!!")
  ##      print("After from ", edge_a[0],  " head vertex 1", G[edge_a[0]])
  ##      print ("After from ", edge_b[0], " head vertex 2 ", G[edge_b[0]] )

  return G




def check_connectivity_old(G, a0, a1, b0, b1):  #a0-->a1 and b0-->b1
  connectivity = False

  if ((a0 != b0) and (a0 != b1) and (a1 != b0) and (a1 != b1)): #no a0==b0 or a0==b1 0r a1==b0 or a1==b1
    if (a0 not in G[a1]) and (b0 not in G[b1]) :    #no a1 -->a0 or b1 -->bo
      if (a0 not in G[b0]) and (a0 not in G[b1]) and (b0 not in G[a0]) and (b0 not in G[a1]):     #no bo-->a0 or b1-->a0 or a0-->b0 or a1 -->b0
        if (a1 not in G[b0]) and (a1 not in G[b1]) and (b1 not in G[a0]) and (b1 not in G[a1]):   #no bo-->a1 or b1-->a1 or a0-->b1 and a1--> b1
          connectivity = True
  return connectivity




def check_connectivity(G, a0, a1, b0, b1):  #a0-->a1 and b0-->b1
  connectivity = False

  if ((a0 != b0) and (a0 != b1) and (a1 != b0) and (a1 != b1)): #no a0==b0 or a0==b1 0r a1==b0 or a1==b1
    if (b1 not in G[a0]) and (a1 not in G[b0]) :    #no a1 -->a0 or b1 -->bo
      connectivity = True
  return connectivity






##
##def random_node(l):
##  shuffle(l)
##  #print("1. initial", l)
##  shuffle(l)
##  #print("2. initial", l)
##  shuffle(l)
##  #print("3. initial", l)
##  shuffle(l)  
##  return l[0]
##
##
##def random_edge(l):
##  shuffle(l)
##  shuffle(l)
##  shuffle(l)
##  shuffle(l) 
##  return l[0]
