import ast
import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="yourpassword",
     database="Kolkata"
)

mycursor=mydb.cursor()

Adjacency_list={}

mycursor.execute("select * from Kolkata_Main_Graph;")
rows=mycursor.fetchall()
for i in rows:
    x=i[1]
    res=ast.literal_eval(x)
    Adjacency_list[i[0]]=res

    
#for finding out the Adjacent_nodes_list for a particular vertex

def find_adjacent_vertices(Adjacency_list,Adjacent_nodes_list,ivertex):
    for j in Adjacency_list[ivertex]:
        Adjacent_nodes_list.append(j[0])
    return Adjacent_nodes_list

#for finding out the minimum unprocessed element

def min_weight(label_and_value_dict,processed_and_visited_dict,vertex_List,ivertex):
    
    minimum=9999
    vertex=ivertex
    for i in vertex_List:
        if processed_and_visited_dict[i]==False and label_and_value_dict[i]<minimum:
            vertex=i
            minimum=label_and_value_dict[i]
        
    return vertex

#for finding the weight of an edge

def find_weight_of_edge(Adjacency_list,i,j):
    for k in Adjacency_list[i]:
        if k[0]==j:
            return k[1]

#for finding the shortest paths from single source
    
def dijkstra(Adjacency_list,ivertex):
    
    vertex_List=list(Adjacency_list.keys())
    
    label_and_value_dict={}
    parent_dict={}
    processed_and_visited_dict={}
    for i in vertex_List:
        parent_dict[i]=-1
        processed_and_visited_dict[i]=False
        if i==ivertex:
            label_and_value_dict[i]=0
        else:
            label_and_value_dict[i]=9999
    
    for i in vertex_List:
        vertex=min_weight(label_and_value_dict,processed_and_visited_dict,vertex_List,i)
        processed_and_visited_dict[vertex]=True
        
        Adjacent_nodes_list=[]
        Adjacent_nodes_list=find_adjacent_vertices(Adjacency_list,Adjacent_nodes_list,vertex)
        
        for j in Adjacent_nodes_list:
            weight_of_edge=find_weight_of_edge(Adjacency_list,vertex,j)
            
            if label_and_value_dict[vertex]+weight_of_edge<label_and_value_dict[j]:
                label_and_value_dict[j]=label_and_value_dict[vertex]+weight_of_edge
                parent_dict[j]=vertex
            else:
                continue
    label_and_value_dict=dict(sorted(label_and_value_dict.items(), key=lambda item: item[1]))
    print("Shortest Paths from the given Source: ")
    k=list(label_and_value_dict.keys())
    for i in k:
        print("Distance from Source: ",ivertex," to destination: ",i," is: ",label_and_value_dict[i])

ivertex=int(input("Enter the Pin Code to search the closest places: "))
dijkstra(Adjacency_list,ivertex)     
