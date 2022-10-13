from search import (EightPuzzle, astar_search, breadth_first_graph_search,
                    depth_first_graph_search)

if __name__ == "__main__":
    eight_puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0))
    print(astar_search(eight_puzzle, h=None, display=True).solution())
    print(breadth_first_graph_search(eight_puzzle).solution())
    print(depth_first_graph_search(eight_puzzle).solution())
