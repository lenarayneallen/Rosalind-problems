s = open('tree5.txt', 'r')
p = s.read()
psplit = p.split()

#define number of nodes and format adjacency list
num_nodes = int(psplit[0])
num_str_list = psplit[1:]
num_list = []
for num in num_str_list:
    num_list.append(int(num))
adj_list = [num_list[i:i + 2] for i in range(0, len(num_list), 2)]  


def min_num_edges_for_tree(n, adj):
    #get number of edges by counting entries in adjacency list
    num_edges = len(adj)

    #calculate minimum number of edges needed to produce a tree
    #this method accounts for the missing nodes without having to identify and count them
    min_num_edges = n - num_edges - 1

    return min_num_edges

print(min_num_edges_for_tree(num_nodes, adj_list))
