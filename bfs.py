# bfs.py
from collections import deque
from food_map import MAP

def find_food_bfs(start, goal):
    # Queue stores full paths to check
    queue = deque([[start]])
    seen = set()

    while queue:
        # Take the oldest path out of the queue
        path = queue.popleft()
        current_spot = path[-1]

        # Did we reach dinner?
        if current_spot == goal:
            return path

        if current_spot not in seen:
            seen.add(current_spot)
            # Look at all direct neighbors
            for neighbor, _ in MAP[current_spot]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

if __name__ == "__main__":
    result = find_food_bfs('Bed', 'Dinner')
    print("BFS Path:", result)