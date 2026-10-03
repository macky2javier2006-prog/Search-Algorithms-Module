# Search Algorithms Module

This project demonstrates three graph-search algorithms on a small map of locations leading to dinner.

## Algorithms

- `bfs.py` - breadth-first search; returns a path with the fewest edges.
- `dfs.py` - depth-first search; returns the first path found using the map's neighbor order.
- `astar.py` - A* search; returns a path and its total travel time using the heuristic in `food_map.py`.
- `food_map.py` - shared graph and A* heuristic data.

Run each algorithm from this directory:

```powershell
python bfs.py
python dfs.py
python astar.py
```
