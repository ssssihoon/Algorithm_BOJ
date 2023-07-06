def dfs(y, x):
    # print(graph[y][x])
    # print(graph[y][x] == ['-'])
    # print(graph[y][x] == '-')

    if y > N - 1 or y < 0 or x < 0 or x > M - 1 or visited[y][x] == 1:
        return

    visited[y][x] = 1

    if graph[y][x] == '-':
        if M - 1 >= x + 1 >= 0 and graph[y][x + 1] == graph[y][x]:
            dfs(y, x+1)
    elif graph[y][x] == '|':
        if N - 1 >= y + 1 >= 0 and graph[y + 1][x] == graph[y][x]:
            dfs(y+1, x)


N, M = map(int, input().split())

graph = []
for y in range(N):
    graph.append(list(input()))

count = 0
visited = [[0 for q in range(M)] for p in range(N)]


for y in range(N):
    for x in range(M):
        if visited[y][x] == 0:
            count += 1
        dfs(y,x)

print(count)


'''
6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-

'''