'''
@Project: algorithm   
@Description: TODO          
@Time:2022/08/01 10:44       
@Author:ZHANG               

the algorithm is referring to https://www.redblobgames.com/pathfinding/a-star/introduction.html#greedy-best-first
the graph in this file is adjacency list
the cost in this file is adjacency matrix
the direction in this file is [up, down, left, right]
A better option is to use object-oriented thinking
I will think about the "Ugly path" in the future.
'''
from implementation import *


def bfs(graph, start, end):
    q = collections.deque([[start, 0]])
    came_from = dict()
    came_from[start] = None
    while q:
        i, s = q.popleft()
        if i == end:
            return s, came_from

        # get the (i, j)'s neighbors
        for d in graph[i]:
            if came_from.get(d, -1) == -1:
                q.append([d, s+1])
                came_from[d] = i
    return -1, -1


def dijkstra(graph, cost, start, end):
    q = [[0, start]]
    came_from = dict()
    came_from[start] = None
    cost_so_far = dict()
    cost_so_far[start] = 0

    while q:
        s, i = heapq.heappop(q)
        if i == end:
            return s, came_from

        # get the (i, j)'s neighbors
        for d in graph[i]:
            if cost_so_far.get(d, -1) == -1 or cost_so_far[d] > s + cost[i][d]:
                heapq.heappush(q, [s + cost[i][d], d])
                came_from[d] = i
                cost_so_far[d] = s + cost[i][d]
    return -1, -1


if __name__ == '__main__':
    list = [[1, 2], [5], [3, 4], [6], [7], [6], [7]]
    s, ret = bfs(list, 0, 7)
    print(s, ret)

    cost = [
        [0, 1, 100, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 5, 3, 0, 0, 0],
        [0, 1, 100, 0, 0, 0, 10, 0],
        [0, 1, 100, 0, 0, 0, 0, 1],
        [0, 1, 100, 0, 0, 0, 10, 0],
        [0, 1, 100, 0, 0, 0, 0, 500],
        [0, 1, 100, 0, 0, 0, 10, 0],
        ]
    s, ret = dijkstra(list, cost, 0, 7)
    print(s, ret)

    print('Reachable from A:')
    breadth_first_search(example_graph, 'A')
    print('Reachable from E:')
    breadth_first_search(example_graph, 'E')

    # plot the graph
    g = SquareGrid(30, 15)
    g.walls = DIAGRAM1_WALLS  # long list, [(21, 0), (21, 2), ...]
    # draw_grid(g)

    start = (8, 7)
    # parents = breadth_first_search(g, start)
    # draw_grid(g, point_to=parents, start=start)

    goal = (17, 2)
    parents = breadth_first_search(g, start, goal)
    draw_grid(g, point_to=parents, start=start, goal=goal)

    start, goal = (1, 4), (8, 3)
    came_from, _ = dijkstra_search(diagram4, start, goal)
    draw_grid(diagram4, point_to=came_from, start=start, goal=goal)
    print()
    draw_grid(diagram4, path=reconstruct_path(came_from, start=start, goal=goal))

    start, goal = (1, 4), (8, 3)
    _, cost_so_far = dijkstra_search(diagram4, start, goal)
    draw_grid(diagram4, number=cost_so_far, start=start, goal=goal)

    came_from, cost_so_far = a_star_search(diagram4, start, goal)
    draw_grid(diagram4, point_to=came_from, start=start, goal=goal)
    print()
    draw_grid(diagram4, path=reconstruct_path(came_from, start=start, goal=goal))


