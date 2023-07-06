def dfs(y, x):
    if x < 0 or x > (n - 1) or y < 0 or y > (n - 1) or visited[y][x] == 1:
        return

    if graph[y][x] == -1:
        visited[y][x] = 1
        return

    visited[y][x] = 1
    dfs(y + int(graph[y][x]), x)
    dfs(y, x + int(graph[y][x]))


n = int(input())
graph = []
visited = [[0 for q in range(n)] for p in range(n)]

for i in range(n):
    graph.append(list(input().split()))

for y in range(0, n):
    for x in range(0, n):
        dfs(0, 0)

if visited[- 1][- 1] == 1:
    print("HaruHaru")
else:
    print("Hing")

'''
3
2 2 1
2 2 2
1 2 -1
'''
