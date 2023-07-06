# User function Template for python3

from collections import deque


def dfsOfGraph(V, adj):
    visited = {}
    stack = deque()
    stack.append(0)
    traversal = []

    while len(stack):
        node = stack.pop()

        if visited.get(node, False):
            continue

        visited[node] = True
        traversal.append(node)

        for neigh in adj[node][::-1]:
            # print(node, neigh)
            if not visited.get(neigh, False):
                stack.append(neigh)

    return traversal


def dfsOfGraphRec(V, adj):
    visited = {}
    traversal = []

    def helper(node):
        if visited.get(node, False):
            return

        visited[node] = True
        traversal.append(node)

        for neigh in adj[node]:
            if not visited.get(neigh, False):
                helper(neigh)

    helper(0)
    return traversal



print(dfsOfGraphRec(None, [[2, 3, 1], [], [4], [], [4]]))
