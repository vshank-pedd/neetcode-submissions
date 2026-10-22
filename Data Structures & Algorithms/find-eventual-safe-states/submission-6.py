class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse = [[] for _ in graph]
        degree = [len(row) for row in graph]
        for source,row in enumerate(graph):
            for target in row: reverse[target].append(source)
        queue = [i for i,d in enumerate(degree) if d == 0]
        for node in queue:
            for previous in reverse[node]:
                degree[previous] -= 1
                if degree[previous] == 0: queue.append(previous)
        return [i for i,d in enumerate(degree) if d == 0]
