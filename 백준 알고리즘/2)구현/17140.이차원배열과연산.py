import sys 
r, c, k = map(int, sys.stdin.readline().split())
r-= 1
c-=1
graph = []

for i in range(3):
    graph.append(list(map(int, sys.stdin.readline().split())))

cnt = 0 
def sort_graph(a) :
    l = []
    for i in set(a) : 
        if i == 0 : 
            continue
        l.append((i, a.count(i)))
    l = sorted(l, key = lambda x: (x[1], x[0]))
    result = []
    for j in l : 
        result.append(j[0])
        result.append(j[1])
    return result

while True : 
    if cnt > 100 : 
        cnt = -1
        break
    if 0<=r<len(graph) and 0<=c<len(graph[0]) and graph[r][c] == k : 
        break
    maximum = 0 
    if len(graph)>= len(graph[0]) :
        for i in range(len(graph)) :
            graph[i] = sort_graph(graph[i])
            maximum = max(maximum, len(graph[i]))
        for i in range(len(graph)) :
            if len(graph[i])<maximum : 
                while len(graph[i])< maximum : 
                    graph[i].append(0)
        for i in range(len(graph)) :
            if len(graph[i])>100 : 
                graph[i] = graph[i][:100]
    else : 
        new_graph= []
        for j in range(len(graph[0])):
            l = []
            for i in range(len(graph)):
                l.append(graph[i][j])
            new_graph.append(sort_graph(l))
            maximum = max(maximum, len(new_graph[j]))
        for i in range(len(new_graph)) :
            if len(new_graph[i])<maximum : 
                while len(new_graph[i])< maximum : 
                    new_graph[i].append(0)
        for i in range(len(new_graph)) :
            if len(new_graph[i])>100 : 
                new_graph[i] = new_graph[i][:100]
        graph = list(zip(*new_graph))
    cnt += 1

print(cnt)



    