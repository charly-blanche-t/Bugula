
from array import *


def create_new_entry_statDict (graphName, statDict, outputDict):

    value = outputDict[graphName]

    nber_green_cc = []
    nber_nodes_largest_cc =  []
    nber_edges_largest_cc =  []
    nber_edges_induced_graph =  []

    
    nber_green_cc.append(value[0])
    nber_nodes_largest_cc.append(value[1])
    nber_edges_largest_cc.append(value[2])
    nber_edges_induced_graph.append(value[3])


    list_of_arrays = []
    list_of_arrays.append(nber_green_cc)
    list_of_arrays.append(nber_nodes_largest_cc)
    list_of_arrays.append(nber_edges_largest_cc)
    list_of_arrays.append(nber_edges_induced_graph)

    statDict[graphName]= list_of_arrays
    

    return  statDict



def update_statDict (graphName,  statDict, outputDict):

    from_outputDict = outputDict[graphName]             #This is a list

    statDict[graphName][0].append(from_outputDict[0])   # This is an array statDict[graphName][0]
    statDict[graphName][1].append(from_outputDict[1])
    statDict[graphName][2].append(from_outputDict[2])
    statDict[graphName][3].append(from_outputDict[3])

    return  statDict


def writeDict(statDict, stat_filename, sep, graphName):
    with open(stat_filename, "a") as f:
        i = graphName
                
        f.write("%s" % "nberCC")
        f.write(",")
        for item in statDict[i][0]:
          f.write("%s" % item)
          f.write(",")
        f.write("\n")
        
        f.write("%s" % "highestNberNodesInCC")
        f.write(",")
        for item in statDict[i][1]:
          f.write("%s" % item)
          f.write(",")
        f.write("\n")
            
        f.write("%s" % "highestNberEdgesInCCs")
        f.write(",")
        for item in statDict[i][2]:
          f.write("%s" % item)
          f.write(",")
        f.write("\n")
        
        f.write("%s" % "nberEdgesInducedGraph")
        f.write(",")
        for item in statDict[i][3]:
          f.write("%s" % item)
          f.write(",")
        f.write("\n")

        f.write("\n") # To separate runs


            
