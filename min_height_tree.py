from collections import defaultdict
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    adj_mat = defaultdict(list)
    degree = defaultdict(int)
    vertices = n

    for i in range(n - 1):
        ends = edges[i]
        adj_mat[ends[0]].append(ends[1])
        adj_mat[ends[1]].append(ends[0])
        degree[ends[0]] += 1
        degree[ends[1]] += 1

    leaves = []
    for node, neighbors in adj_mat.items():
        if len(neighbors) == 1:
            leaves.append(node)

    while vertices > 2:
        current_leaves = len(leaves)
        vertices -= current_leaves
        for i in range(current_leaves):
            leaf = leaves.pop(0)
            for branch in adj_mat[leaf]:
                degree[branch] -= 1
                if degree[branch] == 1:
                    leaves.append(branch)

    return leaves


if __name__ == '__main__':
    print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
    print(findMinHeightTrees(1, []))
    print(findMinHeightTrees(2, [[0, 1]]))
