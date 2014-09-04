import copy
import operator
from array import *


def create_new_entry_statDict (graphName, statDict, outputDict):

    value = outputDict[graphName]

    nber_green_cc = []
    nber_OneNode_cc = []
    nber_nodes_largest_cc =  []
    nber_edges_largest_cc =  []
    nber_edges_induced_graph =  []
    graph_density =  []
    
    nber_green_cc.append(value[0])
    nber_OneNode_cc.append(value[1])
    nber_nodes_largest_cc.append(value[2])
    nber_edges_largest_cc.append(value[3])
    nber_edges_induced_graph.append(value[4])
    graph_density.append(value[5])


    list_of_arrays = []
    list_of_arrays.append(nber_green_cc)
    list_of_arrays.append(nber_OneNode_cc)
    list_of_arrays.append(nber_nodes_largest_cc)
    list_of_arrays.append(nber_edges_largest_cc)
    list_of_arrays.append(nber_edges_induced_graph)
    list_of_arrays.append(graph_density)    

    statDict[graphName]= list_of_arrays
    

    return  statDict



def update_statDict (graphName,  statDict, outputDict):

    from_outputDict = outputDict[graphName]             #This is a list

    statDict[graphName][0].append(from_outputDict[0])   # This is an array statDict[graphName][0]
    statDict[graphName][1].append(from_outputDict[1])
    statDict[graphName][2].append(from_outputDict[2])
    statDict[graphName][3].append(from_outputDict[3])
    statDict[graphName][4].append(from_outputDict[4])
    statDict[graphName][5].append(from_outputDict[5])

    return  statDict


def p_value (statDict):

    three_p_value = {}

    for graphName in statDict.keys():

        density_list = statDict[graphName][5]             #This is a list
        reference = density_list.pop(0)
        copy_density_list = copy.copy(density_list)

        indexes = sorted(range(len(copy_density_list)), key = lambda k: copy_density_list[k])
        #indexes1 = sorted(enumerate(copy_density_list), key=operator.itemgetter(1))
        #print ("indexes1: ", indexes1 )        # keep track of initial position
        print ("indexes: ", indexes )

        position05 = 1
        position3 = 1    
        position5 = 1
        
        sorted_dlist = sorted(copy_density_list)
        print ("sorted_dlist: ", sorted_dlist )
        l_dlist = len(sorted_dlist)
        i=1
        print ("sorted_dlist[l_dlist-i]: ", sorted_dlist[l_dlist-i] )
        while (reference <= sorted_dlist[l_dlist-i] and i< l_dlist):
            if i/float(l_dlist)<=0.005:
                position05 = position05 +1
                position3 = position3 +1
                position5 = position5 +1

            if i/float(l_dlist)<=0.03:
                position3 = position3 +1
                position5 = position5 +1
                
            if i/float(l_dlist)<=0.05:
                position5 = position5 +1        
                    
            i=i+1
        print ("i out: ", i )

        print ("reference: ", reference)
        print ("position05: ", position05)
        print ("position3: ", position3)
        print ("position5: ", position5)
        value= []
        value.append(position05)
        value.append(position3)
        value.append(position5)    

        three_p_value[graphName]= value

    return  three_p_value



def writeDensity_vertices(three_p_value_Dict):
    
    stat_filename = "Vertices/" + "Graph_density_vertices.csv"

    with open(stat_filename, "w") as f:

        f.write("%s" % "Pathway")
        f.write(",")
        
        f.write("%s" % "0.005_P_value")
        f.write(",")

        f.write("%s" % "0.03_P_value")
        f.write(",")

        f.write("%s" % "0.05_P_value")
        f.write("\n")

        for i in three_p_value_Dict.keys():
            graphName = i

            f.write("%s" % graphName)
            f.write(",")            

            #for j in range (len (three_p_value_Dict[i])):
            f.write("%s" % three_p_value_Dict[i][0])
            f.write(",")
            f.write("%s" % three_p_value_Dict[i][1])
            f.write(",")
            f.write("%s" % three_p_value_Dict[i][2])
            f.write("\n") 
              



def writeDensity_edges(three_p_value_Dict):
    
    stat_filename = "Edges/" + "Graph_density_edges.csv"

    with open(stat_filename, "w") as f:

        f.write("%s" % "Pathway")
        f.write(",")
        
        f.write("%s" % "0.005_P_value")
        f.write(",")

        f.write("%s" % "0.03_P_value")
        f.write(",")

        f.write("%s" % "0.05_P_value")
        f.write("\n")

        for i in three_p_value_Dict.keys():

            f.write("%s" % i)
            f.write(",")            

            for j in range (len (three_p_value_Dict[i])):
                f.write("%s" % three_p_value_Dict[i][j])
                f.write(",")
                f.write("%s" % three_p_value_Dict[i][j])
                f.write(",")
                f.write("%s" % three_p_value_Dict[i][j])
                f.write("\n") 







def writeDict_vertices(statDict, sep):

    for i in statDict.keys():
        stat_filename = "Vertices/" + i + "_swap_vertices.csv"

        with open(stat_filename, "w") as f:

            f.write("%s" % "nberCC")
            f.write(",")
            
            f.write("%s" % "nberOneNodeCC")
            f.write(",")

            f.write("%s" % "highestNberNodesInCC")
            f.write(",")

            f.write("%s" % "highestNberEdgesInCCs")
            f.write(",")
            
            f.write("%s" % "nberEdgesInducedGraph")
            f.write(",")
            
            f.write("%s" % "density")
            f.write("\n")            

            for j in range (len (statDict[i][1])):
                f.write("%s" % statDict[i][0][j])
                f.write(",")
                f.write("%s" % statDict[i][1][j])
                f.write(",")
                f.write("%s" % statDict[i][2][j])
                f.write(",")
                f.write("%s" % statDict[i][3][j])
                f.write(",")                
                f.write("%s" % statDict[i][4][j])
                f.write(",")
                f.write("%s" % statDict[i][5][j])
                f.write("\n")               





def writeDict_edges(statDict, sep):
    
    for i in statDict.keys():
        stat_filename = "Edges/" + i + "_swap_edges.csv"

        with open(stat_filename, "w") as f:

            f.write("%s" % "nberCC")
            f.write(",")
            
            f.write("%s" % "nberOneNodeCC")
            f.write(",")

            f.write("%s" % "highestNberNodesInCC")
            f.write(",")

            f.write("%s" % "highestNberEdgesInCCs")
            f.write(",")
            
            f.write("%s" % "nberEdgesInducedGraph")
            f.write("\n")
            
            f.write("%s" % "density")
            f.write("\n")            

            for j in range (len (statDict[i][1])):
                f.write("%s" % statDict[i][0][j])
                f.write(",")
                f.write("%s" % statDict[i][1][j])
                f.write(",")
                f.write("%s" % statDict[i][2][j])
                f.write(",")
                f.write("%s" % statDict[i][3][j])
                f.write(",")                
                f.write("%s" % statDict[i][4][j])
                f.write(",")
                f.write("%s" % statDict[i][5][j])
                f.write("\n")               

                

            

##    >>> myList = [1, 2, 3, 100, 5]
##    >>> [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
##    [0, 1, 2, 4, 3]
##    x = numpy.argsort(a) function or x = numpy.ndarray.argsort(a)
##
##    from operator import itemgetter
##    sorted(enumerate(a), key=itemgetter(1))
##
##    lst = [2,3,1,4,5]
##    import operator
##    sorted(enumerate(lst), key=operator.itemgetter(1))
##    [(2, 1), (0, 2), (1, 3), (3, 4), (4, 5)]


            
