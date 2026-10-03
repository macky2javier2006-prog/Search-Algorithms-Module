# dfs.py
from food_map import MAP

def find_food_dfs(start, goal):
    # Stack stores paths to explore
    stack = [[start]]
    seen = set()

    while stack:
        # Take the newest path off the stack
        path = stack.pop()
        current_spot = path[-1]

        # Did we reach dinner?
        if current_spot == goal:
            return path

        if current_spot not in seen:
            seen.add(current_spot)
            # Add neighbors into the stack
            for neighbor, _ in MAP[current_spot]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None

if __name__ == "__main__":
    result = find_food_dfs('Bed', 'Dinner')
    print("DFS Path:", result)