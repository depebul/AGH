from zad2testy import runtests


from collections import deque

def robot(L, A, B):
    # Define directions as (dx, dy) for North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # Map directions to a readable format
    direction_names = ["N", "E", "S", "W"]

    def is_valid(x, y):
        return 0 <= x < len(L) and 0 <= y < len(L[0]) and L[x][y] == ' '

    # BFS queue: (x, y, direction, time, moves_since_last_turn)
    queue = deque([(A[0], A[1], 1, 0, 0)]) # starting facing East
    visited = set([(A[0], A[1], 1)]) # visited states with direction

    while queue:
        x, y, direction, time, moves = queue.popleft()

        # Check if we've reached the target
        if (x, y) == (B[0], B[1]):
            return time

        # Explore forward movement
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if is_valid(nx, ny):
            # Time for the next move
            if moves == 0:
                next_time = time + 60
            elif moves == 1:
                next_time = time + 40
            else:
                next_time = time + 30

            if (nx, ny, direction) not in visited:
                visited.add((nx, ny, direction))
                queue.append((nx, ny, direction, next_time, moves + 1))

        # Explore rotations
        for turn in [-1, 1]: # -1 for counter-clockwise, 1 for clockwise
            new_direction = (direction + turn) % 4
            if (x, y, new_direction) not in visited:
                visited.add((x, y, new_direction))
                queue.append((x, y, new_direction, time + 45, 0))

    return None



runtests( robot )

