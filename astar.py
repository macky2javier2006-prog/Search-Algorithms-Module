# astar.py
import heapq
from food_map import MAP, SMELL_DISTANCE

def find_food_astar(start, goal):
    # Priority Queue stores: (total_estimated_effort, minutes_spent, path)
    pq = [(SMELL_DISTANCE[start], 0, [start])]
    visited = {}

    while pq:
        f_score, minutes_spent, path = heapq.heappop(pq)
        current_spot = path[-1]

        if current_spot == goal:
            return path, minutes_spent

        if current_spot in visited and visited[current_spot] <= minutes_spent:
            continue
        visited[current_spot] = minutes_spent

        for neighbor, minutes in MAP[current_spot]:
            new_minutes = minutes_spent + minutes
            total_estimate = new_minutes + SMELL_DISTANCE[neighbor]
            heapq.heappush(pq, (total_estimate, new_minutes, path + [neighbor]))

    return None, 0

if __name__ == "__main__":
    path, total_time = find_food_astar('Bed', 'Dinner')
    print("A* Path  :", path)
    print("Total Effort/Time:", total_time)