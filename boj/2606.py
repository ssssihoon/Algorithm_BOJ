
com_n = int(input())
link = int(input())
graph = [[] for i in range(com_n+1)]
visited = [0]*(com_n+1)
for j in range(1, link+1):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(x):
    visited[x] = 1
    for k in graph[x]:
        if visited[k] == 0:
            dfs(k)


dfs(1)
print(sum(visited)-1)


