'''
@Project: algorithm   
@Description: TODO          
@Time:2022/7/10 1:52       
@Author:ZHANG               
 
'''
import sys
sys.setrecursionlimit(10 ** 6)


# dp[i][1] means get at most d[i]-1 weights, dp[i][0] means get at most d[i] weights
# this is a traversal version
def main(lines):
    # Tree dp
    def dfs(u, par):
        res = 0
        choose = []
        for nxt, w in graph[u]:
            if nxt == par:
                continue
            dfs(nxt, u)
            # if w is useful, add it to the list
            if dp[nxt][1] + w > dp[nxt][0]:
                choose.append(dp[nxt][1] + w - dp[nxt][0])
            res += dp[nxt][0]

        # sorted the list to get the most useful value
        choose.sort(reverse=True)
        dp[u][1], dp[u][0] = res, res
        for i in range(min(len(choose), d[u-1])):
            if i == d[u-1]-1:
                dp[u][0] += choose[i]
            else:
                dp[u][1] += choose[i]
                dp[u][0] += choose[i]
        # if d[u-1] equal to 0, dp[u][1] become not valid , so change it to -INF
        if d[u-1] == 0:
            dp[u][1] = float("-inf")

    N = int(lines[0])
    d = list(map(int, lines[1].split(" ")))
    dp = [[0, 0] for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for line in lines[2:]:
        u, v, w = map(int, line.split(" "))
        graph[u].append([v, w])
        graph[v].append([u, w])
    dfs(1, 0)
    print(dp[1][0])


# other's method
def main1(lines):
    N = int(lines[0])
    deg_limit = list(map(int, lines[1].split(" ")))

    adj = [[] for _ in range(N)]
    for line in lines[2:]:
        u, v, w = map(int, line.split(" "))
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    par = [-1] * N  # parent
    v_order = []  # top-down ordering
    stack = [0]  # u
    while stack:  # stacked-dfs
        u = stack.pop()
        v_order.append(u)
        for v, _ in adj[u]:
            if v != par[u]:
                par[v] = u  # v->u: to parent
                stack.append(v)

    INF = float('inf')
    no_select, selectable = [-INF] * N, [-INF] * N
    for u in v_order[::-1]:  # bottom up
        base = 0
        diff = [0]
        for v, w in adj[u]:
            if v != par[u]:
                base += no_select[v]
                diff.append(max(0, w + selectable[v] - no_select[v]))
        no_select[u] = base
        if deg_limit[u] > 0:
            diff.sort(reverse=True)
            no_select[u] += sum(diff[:deg_limit[u]])
            selectable[u] = no_select[u] - diff[deg_limit[u] - 1]
    print(no_select[0])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main1(lines)