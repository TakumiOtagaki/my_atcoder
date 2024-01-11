import sys

def topological_sort(nodes, edges):
    """
    nodes = ['a, 'b', 'c'] # 頂点
    edges = [['a', 'b'], ['b', 'c']] # 辺
    この問題では閉路がないことが保証されている。
    """

    input_edges = [[] for _ in range(len(nodes))]
    output_edges = [[] for _ in range(len(nodes))]
    for edge in edges:
        input_edges[nodes.index(edge[1])].append(nodes.index(edge[0]))
        output_edges[nodes.index(edge[0])].append(nodes.index(edge[1]))

    # 入次数が0の頂点をキューに入れる
    queue = []
    for i in range(len(nodes)):
        if len(input_edges[i]) == 0:
            queue.append(i)

    # 幅優先探索
    sorted_nodes = []
    while len(queue) > 0:
        node = queue.pop(0)
        sorted_nodes.append(node)
        for output_node in output_edges[node]:
            input_edges[output_node].remove(node)
            if len(input_edges[output_node]) == 0:
                queue.append(output_node)

    return sorted_nodes



H, W = map(int, input().split()) # 長方形領域。
# A[H][W]: string list
A = [list(map(str, input().split())) for _ in range(H)]

N = int(input()) # 被食者捕食者関係（edges） の数
edges = [list(map(str, input().split())) for _ in range(N)]
# print(edges)

# 頂点のリスト
nodes = [] # edges を flatten したものの set
for edge in edges:
    nodes.append(edge[0])
    nodes.append(edge[1])
nodes = sorted(list(set(nodes)))
# print(nodes)

# topological sort
sorted_nodes_index = topological_sort(nodes, edges)
# print(sorted_nodes_index) # これは nodes の index になっている。 nodes の要素に対応させる必要がある。
sorted_nodes = [nodes[i] for i in sorted_nodes_index]
# print(sorted_nodes)

# sorted nodes の順番に、A の要素を life game のように更新していく。
# edges[i][0] が edges[i][1] を食べる。食べられたら、edges[i][1] は A 上で "-" になる。
# A[i][j] の周囲 8 マスで被食関係は生じる。


# 計算量削減のために、A[i][j] のどこがどの node になっているかの辞書を作っておく。
# これは、A の要素が変化しても変化しない。loop の中で skip すればよい。

A_dict = {}
for i in range(H):
    for j in range(W):
        node_ij = A[i][j]
        if node_ij in A_dict:
            A_dict[node_ij].append((i, j))
        else:
            A_dict[node_ij] = [(i, j)]

# 被食者のリスト
preys_dict = {} #preys_dict[predator] = [prey1, prey2, ...]
for edge in edges:
    if edge[0] in preys_dict:
        preys_dict[edge[0]].append(edge[1])
    else:
        preys_dict[edge[0]] = [edge[1]]

# print(preys_dict)



# main loop
for node in sorted_nodes:
    for i, j in A_dict[node]:
        # A[i][j] の周囲 8 マスで被食関係は生じる。
        if A[i][j] == "-":
            continue
        if node not in preys_dict.keys():
            continue
        preys = preys_dict[node]
        for k in range(-1, 2):
            for l in range(-1, 2):
                if 0 <= i+k < H and 0 <= j+l < W:
                    if A[i+k][j+l] in preys:
                        A[i+k][j+l] = "-"
                        if len(A_dict[node]) == 0:
                            break



# print
for i in range(H): # space separated
    print(" ".join(A[i]))
    
