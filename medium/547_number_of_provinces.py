class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = {}
        n = len(isConnected)
        provinces = 0
        for i in range(n):
            q = deque()

            if visited.get(i, False) is True:
                continue

            provinces += 1
            q.append(i)
            visited[i] = True

            # can be either bfs or dfs, the idea is just to visit all connected nodes in order to
            # completely traverse a component / province
            while q:
                node = q.popleft()

                for idx, neigh in enumerate(isConnected[node]):
                    if neigh == 1 and visited.get(idx, False) is False:
                        visited[idx] = True
                        q.append(idx)

        return provinces