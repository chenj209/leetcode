class Node:
    def __init__(self,idx):
        self.idx = idx
        self.neigs = []

    def add_neig(self,node):
        self.neigs.append(node)

    def get_coord(self,):
        return self.idx % 3, self.idx // 3

    def __str__(self):
        return f"Node({self.idx}, neigs:{[neig.idx for neig in self.neigs]}"

if __name__ == "__main__":
    graph = [Node(i) for i in range(1,9)]

    possible_neigs = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
    # init graph
    for idx in len(graph):
        cur_node = graph[idx]
        x, y = cur_node.get_coord()
        for pn in possible_neigs:
            neig_x, neig_y = x+pn[0], y+pn[1]
            if neig_x <= 3 and neig_y <= 3:
                cur_node.add_neig(graph[neig_x+neig_y*3])

    for node in graph:
        print(node)

