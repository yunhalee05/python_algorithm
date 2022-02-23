n, m = map(int, input().split())
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]  =a
    else parent[a] = b
result = []
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    cnt , a, b = map(int, input().split())
    if cnt == 0:
        union_parnet(parent, a, b)
    elif cnt == 1:
        if find_parent(parent, a) =find_parent(parent,b):
            result.append('YES')
        else :result.append('NO')

for i in result:
    print(i)
