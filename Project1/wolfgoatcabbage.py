from search import Problem, depth_first_graph_search, breadth_first_graph_search

# YOUR CODE GOES HERE


class WolfGoatCabbage(Problem):
    def __init__(self):
        pass


if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
