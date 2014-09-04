
#!/usr/bin/env python
"""
This class compute statistics from aor the induced green graph
"""
__author__ = """ Blanche Temate"""
__date__ = "$Date: 8-15-2014 $"
__credits__ = """"""
__revision__ = "$Revision: 1 $"
#    Copyright (C) 2014 by 
#    TCB
#    All rights reserved.
#    BSD license.


import networkx as nx
import sys




##          1.       Nber of green nodes + a set of names of all green nodes
##          2.       Nber of green connected components (cc)
##          3.       Largest green cc
##          4.       Nber of edges in largest green cc
##          5.       Nber of edges in induced green subgraph

def create_stats (graphName, H):

    #print
    ##print ("Start: stats / p-value !!!!")
   
    statDict = {}


    ##          1.       Nber of green nodes + a set of names of all green nodes
    nberGN = len(H.nodes())
    #print ("(create_stats) Nber of green nodes: ", nberGN )


    ##          2.       Nber of connected components (cc)
    #print
    listCC = sorted(nx.weakly_connected_components(H), key = len, reverse=True)
    #listCC = sorted(nx.connected_components(H), key = len, reverse=True)
    ##print(listCC)
    nbrCC = len(listCC)
    ##print ("(create_stats) 1. Nber of connected components: ", nbrCC)

    
    ##          3.       Largest cc
    #print 
    largestCC = listCC[0] # Same  as largestCC = max(listCC)
    #print("(create_stats) Largest cc: ", largestCC)
    ##print("(create_stats) 2. Nber of node in Largest cc: ", len(largestCC))

 
    
    ##          4.       Nber of edges in largest cc
    #print
    #nberEdgesLargestCC = len (H.edges(largestCC))
    nberEdgesLargestCC = 0
    for i in listCC:
        if nberEdgesLargestCC < len (H.edges(i)):
            nberEdgesLargestCC = len (H.edges(i))
            
            
    ##print ("(create_stats) 3. Highest nber of edges among all cc :" , nberEdgesLargestCC)


    ##          5.       Nber of edges in induced green subgraph
    #print    
    nbrEdgesGreen = len(H.edges())
    ##print ("(create_stats) 4. Nber of edges in induced green subgraph :" , nbrEdgesGreen)


    # Save everything in stat dict: key: graph name, value: 1,2,3 and 4 stats
    #print
    ##print ("end: Stats !!!!")


    # value shd be an array
    
    value= []
    #value.append(nberGN)
    value.append(nbrCC)
    value.append(len(largestCC))        #nber nodes in largest cc
    value.append(nberEdgesLargestCC)    # change to highest nber edges in a cc
    value.append(nbrEdgesGreen)

    statDict[graphName]= value
    #nberGreenDict to contain name of graph + nber of green node. Also can directly come from the global Map
        
    return statDict


