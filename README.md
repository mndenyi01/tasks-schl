# Tasks Repository Summary

This repository contains several task folders, each with its own README describing the task contents and usage.

## task1-mnist
- Demonstrates loading the MNIST dataset from Keras.
- Trains a simple feedforward neural network with 2 hidden layers.
- Uses ReLU activations in hidden layers and Softmax in the output layer.
- Reports ~97.6% training and test accuracy, with a training loss of ~0.0788.
- Notes that exact scores vary each run.

## task2-CSP
- Contains two geography-based graph coloring projects:
  - `Australia-q` analyzes Australia regions and performs greedy graph coloring on regions.
  - `Nairobi-q` analyzes Nairobi sub-counties and performs graph coloring on adjacent sub-counties.
- Recommended use of a Python virtual environment and installation libraries like `geopandas`, `networkx`, `matplotlib`, and `ipykernel`.
- `Australia-q` includes:
  - `code/aus_idk.ipynb`: loads Australia region GeoJSON, finds neighbors, builds a NetworkX graph, applies DSATUR greedy coloring, and visualizes the colored map.
  - `code/aus_plt.py`: standalone script performing the same graph coloring and plotting with a predefined palette.
- `Nairobi-q` includes:
  - `code/eda1.ipynb`: exploratory data analysis and plotting of Nairobi sub-counties.
  - `code/idk.ipynb`: neighbor detection, graph construction, DSATUR greedy coloring, and colored map visualization.
  - `code/idk.py`: standalone script version of the Nairobi coloring workflow, adapted from the notebook and intended to run end-to-end.
- Outputs include colored map visualizations for Australia regions and Nairobi sub-counties.

## task3-prolog
- A Prolog practice task with a family tree source file.
- Defines relationships for grandparents, parents, grandchildren, uncles, aunts, and cousins.
- Includes a Prolog demo screenshot showing queries such as:
  - Charlie's cousin.
  - Whether Albert is Edward's grandparent.
  - Who is Eliza's uncle.

## task4-search
- Contains three separate search algorithm implementations:
  - `a_search/`: Implements the A* search algorithm to find optimal paths between nodes using priority queues with f(n) = g(n) + h(n), where g(n) is actual cost and h(n) is heuristic estimate. Returns optimal path and cost, or None if no path exists.
  - `vacuum_agent/`: A simple reflex agent that cleans dirty locations in an environment. Takes an environment layout dictionary, iterates through locations, detects dirty areas, and cleans them. Each agent instance is auto-numbered via a class variable.
  - `bfs_dfs/`: Implements breadth-first search (using deque from collections) and depth-first search (using a stack). BFS explores level-by-level while DFS follows one branch deeply before backtracking. Both tested on simple and complex graphs.

## Notes
- This root `README.md` is a high-level summary only.
- For full details, see each folder's README and source files directly.
