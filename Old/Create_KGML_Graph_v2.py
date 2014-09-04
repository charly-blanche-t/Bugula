#!/usr/bin/env python
"""
This class create a graph in memory representing KGML from KEGG

"""
__author__ = """ Blanche Temate"""
__date__ = "$Date: 4-29-2014 $"
__credits__ = """"""
__revision__ = "$Revision: 1 $"
#    Copyright (C) 2004 by 
#    TCB
#    All rights reserved.
#    BSD license.


import networkx as nx
import sys
import errno
import os.path
import os




listToBeRemovedNode=[]


def check_KO_group (filename):
    with open(filename, 'r') as f:
        first_line = f.readline()    
    return "ko" in first_line 


def extract_node_name (line):
    #11) ko:K02777 ko:K02778 ko:K02779 ko:K02790 ko:K02791
    words = line.split(')')
    return words[0]


def extract_node_Aliases (line):
    #11) ko:K02777 ko:K02778 ko:K02779 ko:K02790 ko:K02791
    
    line = line.replace("ko","")
    words = line.split(':')
    #words.pop(0)
    
    for ch in words:
        ch = ch.strip()

    words.pop(0)
    #print("              All the aliases of the nodes: " , words)
    
    return words


def check_path_in_node (line):
    #48) path:ko00710
    
    if 'path' in line:
        listToBeRemovedNode.append(extract_node_name(line))



def remove_path_node(graph):

    for i in listToBeRemovedNode:
        graph.remove_node(i)
    listToBeRemovedNode[:] = []
   
    return graph


def create_graph(filename):

    error = 0 # Not dual graph
    
    base=os.path.basename(filename)
    graphName = os.path.splitext(base)[0]
    g = nx.DiGraph(name = graphName)    # Extraxct only name of file from filename
    fg=open(filename)
    print("Is there ko or not: ", check_KO_group (filename))
    
    if check_KO_group (filename):      #Check if we have a green nodes file vs green edges   : Can be done directly from bash script: if file contains "cpd" remove from directory ("C://Qiong//Groups")
        for line in fg:
            line = line.strip()
            if ')' in line:            #To differentiate nodes from edges
                if 'path' in line:
                    #print ("This is a node with path: ", line)
                    check_path_in_node (line)       # To be removed later
                    g.add_node (extract_node_name (line), number = extract_node_name (line), alias = "", color = 'black')   #G.add_node(3,weight=0.4,UTM=('13S',382871,3972649))
                    
                else:
                    #print ( "               Start adding node and aliases")
                    g.add_node (extract_node_name (line), number = extract_node_name (line), alias = extract_node_Aliases (line), color = 'black' )
                    #print ( "Done adding node and aliases")
                    
                                               
            elif '-' in line:
                words=line.split('-')
                g.add_edge (words[0], words[1])
    else:
        print (" Pls consider the dual graph")
        error = 1
    fg.close()

    remove_path_node(g)
    return g, error



