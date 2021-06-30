# Dijkstra_Python
This is a program for finding the closest destinations from the source by applying Dijkstra's algorithm with an Adjacency List on an undirected graph.  

For an Adjacency List we use a Dictionary where the keys are the vertices of the graph and the value of each key is a list containing tuples of length=2. The first element of a tuple is the name of the connected vertex and the next element is the edge weight between the key vertex and the tuple vertex. For example:

Adjacency_List={1:[(2,6), (3,2)], 2:[(1,6), (3,4)], 3:[(1,2), (2,4)]}

So in this Adjacency_List, when the key is 1, our first vertex under consideration or the source vertex is: 1
The value of this key is the adjacency list of vertex 1 i.e. [(2,6),(3,2)]
In this adjacency list, all the connected vertices and their edge weights are grouped together in a tuple. We considered a tuple so that the connected details cannot be changed but more elements can be added/appended in the list for each key vertex.
Now, in our first tuple in this list is (2,6). Hence we can say vertex 1 and 2 are connected with an edge of weight = 6.
Thereofore it can be generalized as:

Adjacency_list={ Key_vertex : [ (adjacent_node, edge_weight), (adjacent_node, edge_weight), .....],
                  Key_vertex2: [ (adjacent_node, edge_weight), (adjacent_node, edge_weight), .....],
                  .
                  .
                  .}


Required Data Structures:

i) processed_dictioanry = {} where all the unprocessed elements/key vertices will have their value kept as 'False' if they are unvisited; and 'True' if visited (initialize as 'False' for every vertex)

ii) parent_dictionary = {} where the vertices are keys and their parents/connected vertices are the values (initialize as -1 for every vertex)

iii) label_dictionary={} where all the key vertices (except the source vertex which has value = 0) have the value which is the cost from the source to that vertex. Every time we find a lesser cost, we update that value (initialize as 'infinity'/9999 for every vertex)

Required Algorithm for Single Source Shortest Path:

i) mark all the vertices as unvisited initially

ii) marks all vertices with 'infinity' label initially except the source node which is 0

iii) Repeat the following for (V-1) times #v is the number of vertices and v-1 because we consider all the vertices except the source
              a) pick the minimum value node which is unprocessed
              b) mark this node as processed
              c) Update all adjacent vertices cost as:
                        if label[u] + weight(u->v) < label[v]
                                update label[v] = label[u] + weight(u->v)
                        else
                                skip/continue
                                
                         
In our program we have made a graph of the City of Kolkata. So the vertices are the pincodes of each locality and the edge weights of adjacent vertices are the distance of the roads betweeen those two localities. Hence we find out the closest localities with our program.
