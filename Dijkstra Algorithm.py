#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###-----------------------------Dijkstra Algorithm--------------------------------------------------------###

#----Date- 29/11/22
#----Author- ELangeshwaran
#----Last modified- 3/12/22 
#----Aim - to find the shortest path from the source to all the vertex


# In[ ]:


def AdjacentRetriever(arr,pos):                #to find the adjacent edges(INPUT: Graph,arrat of positions)
    
    [i,j] = pos                                #current Shortest path tree set (SPTs) position & size of input graph
    n = len(arr)
    m = len(arr[0])
    
    adjacents = []
    adjacentLOC = []
    
    def isValidPos(i, j, n, m):                                      #finding adjacent of the current SPTs
        if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
            return 0
        return 1
    
    for l in range(n):
        if (isValidPos(i-l, j, n, m)):
            if arr[i-l,j] !=0: # & np.logical_not(np.array_equal([i-l,j],pos)):
                adjacents.append(arr[i-l,j])
                adjacentLOC.append([i-l,j])
    for l in range(n):
        if (isValidPos(i+l, j, n, m)):
            if arr[i+l,j] !=0: # & np.logical_not(np.array_equal([i+l,j],pos)):
                adjacents.append(arr[i+l,j])
                adjacentLOC.append([i+l,j])
    for l in range(m):
        if (isValidPos(i, j-l, n, m)):
            if arr[i,j-l] !=0: # & np.logical_not(np.array_equal([i,j-l],pos)):
                adjacents.append(arr[i,j-l])
                adjacentLOC.append([i,j-l])
    for l in range(m):           
        if (isValidPos(i, j+l, n, m)):
            if arr[i,j+l] !=0: # & np.logical_not(np.array_equal([i,j+l],pos)):
                adjacents.append(arr[i,j+l])
                adjacentLOC.append([i,j+l])
                
    for o in range(n):           
        for l in range(m):           
            if (isValidPos(i+o, j+l, n, m)):
                if arr[i+o,j+l] !=0: # & np.logical_not(np.array_equal([i,j+l],pos)):
                    adjacents.append(arr[i+o,j+l])
                    adjacentLOC.append([i+o,j+l])
    for o in range(n):           
        for l in range(m):           
            if (isValidPos(i-o, j-l, n, m)):
                if arr[i-o,j-l] !=0: # & np.logical_not(np.array_equal([i,j+l],pos)):
                    adjacents.append(arr[i-o,j-l])
                    adjacentLOC.append([i-o,j-l])
    for o in range(n):           
        for l in range(m):           
            if (isValidPos(i-o, j+l, n, m)):
                if arr[i-o,j+l] !=0: # & np.logical_not(np.array_equal([i,j+l],pos)):
                    adjacents.append(arr[i-o,j+l])
                    adjacentLOC.append([i-o,j+l])
    for o in range(n):           
        for l in range(m):           
            if (isValidPos(i+o, j-l, n, m)):
                if arr[i+o,j-l] !=0: # & np.logical_not(np.array_equal([i,j+l],pos)):
                    adjacents.append(arr[i+o,j-l])
                    adjacentLOC.append([i+o,j-l])
                
                
    return adjacents,adjacentLOC


# In[ ]:


def EucledianDistance(arr,pointA, pointB):
   # LOCpointA = np.where(A == pointA)
    #LOCpointB = np.where(A == pointB)
    distance = math.dist(pointA,pointB)
    #print(distance)
    return distance


# In[ ]:


import numpy as np
import math
from collections import Counter

A = np.array([[1,0,7,0,2],                       #Graph
     [3,0,4,0,0],
     [0,6,0,0,0],
     [8,0,0,0,5]])
print(A)

elements = np.count_nonzero(A)                  #counting no. of edges
print(elements)

#print()


# In[ ]:


SourcePoint = np.where(A==1)                   #init source point
SourceScore = 0                                #Source score

unusableLOC = []                               #used edges

ScoreSet = []                                  #Score Set
ScoreSet.append(SourceScore)                   #Source score setup in Score Set

Edges = []
Edges.append(A[tuple(SourcePoint)])

unusableLOC.append(SourcePoint)


# In[ ]:



p=0
while p<=elements:    #((len(A)*len(A[0]))-1):   #while loop to perform operations until all the elements of graph are done with shortest path score
    [Adj,AdjLOC] = AdjacentRetriever(A, SourcePoint)


    for x in unusableLOC: 
        for y in AdjLOC: 
            if np.array_equal(tuple(x),tuple(y)): 
                for n in Adj: 
                    counti = Adj.count(n)
                    if n == A[tuple(y)] : 
                        Adj.remove(n) 
                        AdjLOC.remove(y)     
    

    Distance=[] 
    for Pos in AdjLOC:                            #for loop to find shortest distance of all adjacents 
        dist = EucledianDistance(A,SourcePoint,Pos) 
        Distance.append(dist)

#print(Distance)

    ShortestPathScore = min(Distance)

#print(ShortestPathScore)

    SourceScore = ShortestPathScore +SourceScore  #distance as score
    ScoreSet.append(SourceScore)

    SourcePoint = AdjLOC[Distance.index(min(Distance))]

    Edges.append(A[tuple(SourcePoint)])
    
    unusableLOC.append(SourcePoint) 
    np.array(unusableLOC)
    p =p+1
    #print(Edges) 
    #print(ScoreSet)


# In[ ]:


Results = np.column_stack((Edges,ScoreSet))
print(Results)


# In[ ]:





# In[ ]:




