from collections import defaultdict
import math
def solution(n, wires):
    answer = math.inf
    
    def find_answer(parents, not_visited) :
        for index, wire in enumerate(wires):
            a, b = wire[0], wire[1]
            if index != not_visited:
                union_parent(parents, a, b)
                
        group_value = defaultdict(int)
        for i in range(1, n+1):
            group_value[find_parent(i, parents)] += 1
        values = list(group_value.values())
        groupA, groupB = values[0], values[1]
        return abs(groupA - groupB)
        
    def union_parent(parents, a, b):
        parent_a, parent_b = find_parent(a, parents), find_parent(b, parents) 
        if parent_a != parent_b : 
            if parent_a < parent_b:
                parents[parent_b] = parent_a
            else :
                parents[parent_a] = parent_b
    
    def find_parent(a, parents) :
        if a != parents[a] : 
            parents[a] = find_parent(parents[a], parents)
        return parents[a]
    
    
    for i in range(len(wires)) :
        parents = [i for i in range(n+1)]
        answer = min(answer, find_answer(parents, i))
        
    return answer


# from collections import deque

# def bfs(start,visited,graph):
#     queue = deque([start])
#     res = 1
#     visited[start] = True
#     while queue:
#         current = queue.popleft()
#         for i in graph[current]:
#             if visited[i] == False:
#                 res += 1
#                 queue.append(i)
#                 visited[i] = True
#     return res
        

# def solution(n, wires):
#     answer = n
#     graph = [[] for _ in range(n+1)]
#     for a,b in wires:
#         graph[a].append(b)
#         graph[b].append(a)
        
#     for start, not_visit in wires:
#         visited = [False]*(n+1)
#         visited[not_visit] = True
#         res = bfs(start,visited,graph)
#         if abs(res - (n-res)) < answer:
#             answer = abs(res - (n-res))
        
#     return answer