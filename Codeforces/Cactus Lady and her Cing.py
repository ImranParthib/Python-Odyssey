import sys
from collections import deque

def solve():
    t = int(sys.stdin.readline())  # Number of test cases

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())  # Number of vertices and edges
        adj = {i: [] for i in range(1, n + 1)}

        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)

        # BFS to assign positions
        queue = deque()
        positions = {}
        visited = set()

        queue.append((1, 0, 0))  # Start BFS from node 1, assigning (0,0)
        positions[1] = (0, 0)
        visited.add(1)

        y = 1  # Start from y = 1
        success = True

        while queue and success:
            node, x, y = queue.popleft()

            for neighbor in adj[node]:
                if neighbor not in visited:
                    new_x = 1 - x  # Alternate between 0 and 1
                    new_y = y + 1  # Move forward in y
                    if new_y > 200000:  # Out of range
                        success = False
                        break
                    positions[neighbor] = (new_x, new_y)
                    queue.append((neighbor, new_x, new_y))
                    visited.add(neighbor)
                else:
                    # Check for valid placement in case of a cycle
                    nx, ny = positions[neighbor]
                    if abs(nx - x) + abs(ny - y) != 1:
                        success = False
                        break

        if not success:
            print("No")
        else:
            print("Yes")
            for i in range(1, n + 1):
                print(*positions[i])

