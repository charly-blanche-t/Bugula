#!/usr/bin/env python
"""
This class create a green graph in memory representing KGML from KEGG
after analysis.

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

from Create_KGML_Graph_v2 import *
from combination import *
from significance import *


def printDict(dictGreen):
    for key, value in dictGreen.items():
        print (key,value)
        print


def printGraph(G):
    print(G.nodes())
    #List of all nodes without and with data
    print(G.nodes(data=True))
    # Similarly     # G.node # this is a dictionary of node attributes
    print(G.edges())



    
def createGreenMap ( SetofKoNames):
    # Step 1: Read the entire "green" file into a hashmap and keep it in memory
    # Create dictionary
    
    greens = {}

    fd = open(SetofKoNames)
    #ko00061 : K09458,K00645,K00059,K01961,K11262,K00665,

    for line in iter(fd):
        #print (line)
        words = line.split()
        green_nodes=[]
        green_nodes.extend(words[2].split(','))
        green_nodes.pop() 
        greens[words[0]]= green_nodes
        
    fd.close()

    return greens




def create_green_graph(g, mapDict):

    print ("Test dictionary")  # Good working
    #printDict(mapDict)
    
    print ("1- name of the graph: ", g.name)
    graphName = (g.name).strip()
    words=[]
    if graphName in mapDict:           # test if the name of the group is a key in dict consisting of name of graph + green nodes
                                    # to make sure the "group" of that graph is effectively in the list of all map/k0/graph from the kegg website
        words = mapDict[graphName]     # words contains all the green nodes of this graph
        print ("2- name of the graph: ", graphName)
    #else:
    #    error = 3
    #   test the error in main and move to next graph 

    for n in  g.nodes():
##        print ("Print this node: ", n)
##        print ("Print this node's aliases: ", g.node[n]['alias'])
##        print ("Print the name/number of node (2): ", g.node[n]['number'])

        for alias1 in g.node[n]['alias']:
            
            if alias1 in words:
                g.node[n]['color'] = 'green'
                print ("Successful: node ", n , " is green")
                break
            else:
                g.node[n]['color'] = 'black'

    return g



def create_induced_green_graph (green, mapDict):

    graphName = (green.name).strip()
    words=[]
    error = 0
    
    if graphName in mapDict:  
        G = green.to_undirected(reciprocal=False)
        node_ss = [node for node, ndata in G.nodes(data=True) if ndata['color'] == 'green']
        H = G.subgraph(node_ss)
        #printGraph(H)
        print ("(reate_induced_green_graph): finished")
        print
    else:
        error = 2

    return H, error





##          1.       Nber of green nodes + a set of names of all green nodes
##          2.       Nber of green connected components (cc)
##          3.       Largest green cc
##          4.       Nber of edges in largest green cc
##          5.       Nber of edges in induced green subgraph

def create_stats (graphName, H):

    print
    print ("Start: stats / p-value !!!!")
    print

   
    statDict = {}


    ##          1.       Nber of green nodes + a set of names of all green nodes
    nberGN = len(H.nodes())
    print ("(create_stats) Nber of green nodes: ", nberGN )


    ##          2.       Nber of connected components (cc)
    print
    listCC = sorted(nx.connected_components(H), key = len, reverse=True)
    print(listCC)
    nbrCC = len(listCC)
    print ("(create_stats) 1. Nber of connected components: ", nbrCC)

    
    ##          3.       Largest cc
    print 
    largestCC = listCC[0] # Same  as largestCC = max(listCC)
    #print("(create_stats) Largest cc: ", largestCC)
    print("(create_stats) 2. Nber of node in Largest cc: ", len(largestCC))

    
    ##          4.       Nber of edges in largest cc
    print
    nberEdgesLargestCC = len (H.edges(largestCC))
    print ("(create_stats) 3. Nber of edges in largest cc :" , nberEdgesLargestCC)


    ##          5.       Nber of edges in induced green subgraph
    print    
    nbrEdgesGreen = len(H.edges())
    print ("(create_stats) 4. Nber of edges in induced green subgraph :" , nbrEdgesGreen)


    # Save everything in stat dict: key: graph name, value: 1,2,3 and 4 stats
    print
    print ("end: Stats !!!!")


    # value shd be an array
    
    value= []
    #value.append(nberGN)
    value.append(nbrCC)
    value.append(len(largestCC))
    value.append(nberEdgesLargestCC)
    value.append(nbrEdgesGreen)

    statDict[graphName]= value
    #nberGreenDict to contain name of graph + nber of green node. Also can directly come from the global Map
        
    return statDict





def main():
##    SetofKoNames ="C://Users//ytematetiagueu1//Dropbox//Projects//Bugula_Retina//Eclipse_Output//SetofKoNames1.txt"
##    dirname = "C://Qiong//Groups" # Contains all the network graph as text files

    SetofKoNames ="C://Users//temateb//Qiong//SetofKoNames1.txt"
    dirname = "C://Users//temateb//Qiong//Groups" # Contains all the network graph as text files


##    SetofKoNames ="C://Qiong//SetofKoNames1.txt"
##    dirname = "C://Qiong//Groups" # Contains all the network graph as text files


    greensDict = createGreenMap (SetofKoNames)
    graphList=[]
    statDict = {}
        
    for file in os.listdir(dirname):
        #print(file)
        filename=dirname+"//"+file

        print( "\nThe graph from", filename , ":")
        graph, error = create_graph(filename)  # From Create_KGML_Graph_v1 import *

        if error != 1:
            print 
            print ("Print from the graph list of nodes with path: ", listToBeRemovedNode)
            graphList.append(graph)

            print 
            print ("Start creating " , graph.name, "associated green and induced green graph ")
            green =  create_green_graph(graph, greensDict)      # graph (name=X) and greensDict(X:list of nodes)
            onlyGreen, error1 = create_induced_green_graph (green, greensDict)
            print ("End creating " , graph.name, "associated green and induced green graph ")

            if error1 != 2:
                print 
                outputDict = create_stats (graph.name,onlyGreen) # this should just be a list
                statDict = create_new_entry_statDict (graph.name, statDict, outputDict)
                #greenGraphList.append(green)

                nber_permutation = nber_permutation_test(green, onlyGreen)
                print
                print ("Nber nodes in entire graph: ", len(green.nodes()) )
                print ("Nber nodes in entire graph: ", len(green.nodes()) )
                print ("Nber of combinations of green/white: ", nber_permutation)
                print
                
                
                for i in range(5):
                    green_swapped = swap_vertices (green)
                    onlyGreen, error1 = create_induced_green_graph (green_swapped, greensDict)
                    outputDict = create_stats (graph.name,onlyGreen)
                    statDict = update_statDict (graph.name, statDict, outputDict)

                    #All_Results in outputDict
                    # output_Dict  key= graph_name: value: actual outputDict, permutation results, and add the nber_permutation times results

                print
                print ("Print entire dictionnary and save to file")
                
                stat_filename = graph.name + ".csv"
                printDict (statDict)
                writeDict(statDict, stat_filename, ",")
                print
                print

                    
            else:
                print (" Cannot find map or wrong KO name")

                
            
            #printGraph(graphList[0])

        #sys.exit(1)
    
main()





